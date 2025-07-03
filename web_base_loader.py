from langchain_community.document_loaders import TextLoader,PyPDFLoader,WebBaseLoader

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI
import os 

load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './daring-atrium-448311-p9-bb3f69b98364.json'

llm = ChatVertexAI(model_name='gemini-1.5-flash')

url = 'https://www.msn.com/en-in/sports/cricket/yashasvi-jaiswal-the-culprit-again-drops-ben-duckett-on-97-fourth-of-the-match-avoids-coming-near-mohammed-siraj/ar-AA1Hkl22?ocid=entnewsntp&pc=U531&cvid=eaa6df4e8c6542c9aa6bff5f319f6c60&ei=13'
loader = WebBaseLoader(url)

docs = loader.load()

prompt = PromptTemplate(
    template='Answer the following question \n {question} \n based on below text \n {text}',
    input_variables=['text','question']
)

parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({'question' : 'What is the product we are talking about in text','text' : docs[0].page_content})

print(result)

print(docs[0].page_content)
