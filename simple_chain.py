from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv('../app/.env')

llm = ChatOpenAI(model='gpt-4o-mini')

parser = StrOutputParser()

template = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

chain = template | llm | parser

result = chain.invoke({'topic' : 'Cricket'})

print(result)

chain.get_graph().print_ascii()
