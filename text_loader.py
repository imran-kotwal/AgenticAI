from langchain_community.document_loaders import TextLoader
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI
import os 
load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './daring-atrium-448311-p9-bb3f69b98364.json'

llm = ChatVertexAI(model_name='gemini-1.5-flash')

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write the summary for following text\n {text}',
    input_variables=['text']
)

loader = TextLoader('cricket.txt',encoding='utf-8')

docs =  loader.load()

# print(len(docs))
# print(docs[0])

# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt|llm|parser

result = chain.invoke({'text' : docs[0].page_content})

print(result)

#print(type(docs[0]))