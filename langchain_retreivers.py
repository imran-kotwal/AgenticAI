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

load_dotenv()

#vertexai.init()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './daring-atrium-448311-p9-bb3f69b98364.json'

llm = ChatVertexAI(model_name='gemini-1.5-flash')

# https://colab.research.google.com/drive/1vuuIYmJeiRgFHsH-ibH_NUFjtdc5D9P6?usp=sharing#scrollTo=tgMNKHnv6hD8
# https://colab.research.google.com/drive/1VwOywJ9LPSIpKWKj9vueVoexSCzGHXNC?usp=sharing#scrollTo=rIKW6J91c2Gw

retriever = WikipediaRetriever(top_k_results=2,lang="en")

query = "History of India"

docs = retriever.invoke(query)

for i,doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)
#print(type(docs))

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

embedding_model = VertexAIEmbeddings(model_name='text-embedding-005')

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name='my_collection'
)

vector_store2 = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

retriever = vector_store.as_retriever(search_kwargs={"k" : 2})
retriever2 = vector_store2.as_retriever(search_type='mmr',search_kwargs={'k':3,'lambda_mult' : 0.5})

query = 'What os Chroma used for?'
results = retriever.invoke(query)

query = 'What is langchain'
results2 = retriever2.invoke(query)

for i,doc in enumerate(results):
    print(f"\n---Result {i+1} ---")
    print(doc.page_content)


