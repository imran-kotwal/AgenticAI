from langchain_community.document_loaders import TextLoader,PyPDFLoader,CSVLoader

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI
import os 

load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './daring-atrium-448311-p9-bb3f69b98364.json'

llm = ChatVertexAI(model_name='gemini-1.5-flash')

loader = CSVLoader('./path/to/csv')

docs = loader.load()

#Here every row in csv file is converted to document

print(len(docs))
print(docs[0])

#There are a large number of loaders available in langchain to get data from different sources
#For youtube transcript also there is a loader available for youtube transcript 
#We can also have a custome data loaders
#Create a class by inheriting base loader class 