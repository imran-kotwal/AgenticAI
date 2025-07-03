from langchain_community.document_loaders import TextLoader,PyPDFLoader

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI
import os 
load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './daring-atrium-448311-p9-bb3f69b98364.json'

llm = ChatVertexAI(model_name='gemini-1.5-flash')

loader = PyPDFLoader('./sample-report.pdf')

docs = loader.load()

print(docs)
print(docs[0].page_content)
print(docs[0].metadata)