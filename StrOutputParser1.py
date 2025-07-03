from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv('../app/.env')

llm_model = ChatOpenAI(model="gpt-4o-mini")

template1 = PromptTemplate(
    template="Write a Paragraph on topic {text}\n",
    input_variables=['text']
)

parser = StrOutputParser()

template2 = PromptTemplate(
    template="Write a 5 line summary on {text}\n",
    input_variables=['text']
)

chain = template1 | llm_model | parser | template2 | llm_model | parser

result = chain.invoke({'text' : 'Artificial Intelligence'})

print(result)
