from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

load_dotenv('../app/.env')

llm = ChatOpenAI(model='gpt-4o-mini')

parser = JsonOutputParser()

format_instructions = parser.get_format_instructions()

template1 = PromptTemplate(
    template="Get the name and age of any fictional character \n  {format_instructions} ",
    input_variables=[],
    partial_variables={'format_instructions' : format_instructions}
)

template = template1.format()

chain = template1 | llm | parser

result = chain.invoke({})

print(result)