from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser,ResponseSchema,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field

load_dotenv('../app/.env')

llm = ChatOpenAI(model='gpt-4o-mini')

class Person(BaseModel) :
    name : str = Field(description='Name of the person')
    age : int = Field(gt=18,description="Age of the person")
    city : str = Field(description="Place from where person comes from")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name,age and city of fictional {place} person \n {format_instr}',
    input_variables=['place'],
    partial_variables={'format_instr' : parser.get_format_instructions()}

)

chain = template | llm | parser

result = chain.invoke({'place' : "American"})

print(result)