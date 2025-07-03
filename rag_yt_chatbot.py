from langchain_community.vectorstores import Chroma,FAISS
from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI
import os 
from langchain_community.retrievers import WikipediaRetriever
#import vertexai
from langchain_google_vertexai import VertexAIEmbeddings
#from vertexai.language_models import TextEmbeddingModel
from langchain_core.documents import Document
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnableLambda,RunnableParallel,RunnablePassthrough


load_dotenv()

parser = StrOutputParser()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './daring-atrium-448311-p9-bb3f69b98364.json'

llm = ChatVertexAI(model_name='gemini-1.5-flash')

video_id = "Gfr50f6ZBvo" # only the ID, not full URL
try:
    # If you don’t care which language, this returns the “best” one
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])

    # Flatten it to plain text
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video.")

splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
chunks =  splitter.create_documents([transcript])

embedding = VertexAIEmbeddings(model_name='text-embedding-004')
vector_store = FAISS.from_documents(
    chunks,
    embedding
)

retriever = vector_store.as_retriever(search_type='similarity',search_kwargs = {'k' : 4})

print(retriever.invoke("What is deepmind?"))


prompt = PromptTemplate(
    template="""
    You are a helpful Assitant\n
    Answer only from the provided transcript context
    If context is insufficient just say you dont know

    {context}

    Question : {question}
""",
input_variables=['context','question']
)

question = 'What are the common highlights of topic discussed in this video?\n'

#retrieved_docs = retriever.invoke()

def format_docs(retrieved_docs):
  context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
  return context_text

parallel_chain = RunnableParallel(
   {
      'context' : retriever | RunnableLambda(format_docs),
      'question' : RunnablePassthrough()
   }
)

main_chain = parallel_chain | prompt | llm | parser

main_chain.invoke('Summarize the video')


