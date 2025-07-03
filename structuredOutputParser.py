from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
from langchain_core.prompts import PromptTemplate


load_dotenv('../app/.env')

llm = ChatOpenAI(model='gpt-4o-mini')

schema = [
    ResponseSchema(name='fact1',description='Fact 1 about the topic'),
    ResponseSchema(name='fact2',description='Fact 2 about the topic'),
    ResponseSchema(name='fact3',description='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

format_instructions = parser.get_format_instructions()

template = PromptTemplate(
    template="Generate a facts about Football\n {format_instructions}",
    input_variables=['format_instructions'],
    partial_variables={'format_instructions' : format_instructions}
)

chain = template | llm | parser

result = chain.invoke({})

print(result)