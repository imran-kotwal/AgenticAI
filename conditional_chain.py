from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from typing import Literal
from langchain.schema.runnable import RunnableBranch,RunnableLambda

#Based on the sentiment of feedback we would be giving reply to user as per their feedback sentiment

load_dotenv('../app/.env')

llm = ChatOpenAI(model='gpt-4o-mini')

class Feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description='The sentiment of feedback')

parser = StrOutputParser()

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt = PromptTemplate(
    template="Classify the sentiment of following feedback text as positive or negative \n {text} \n {format_instructions}",
    input_variables=['text'],
    partial_variables={'format_instructions' : parser2.get_format_instructions},
)

classifier_chain = prompt | llm | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate small message to this postive feedback\n {feedback}',
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template='Write an appropriate small message to this negative feedback\n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive',prompt2 | llm | parser),
    (lambda x : x.sentiment == 'negative',prompt3 | llm | parser),
    RunnableLambda(lambda x : "Could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'text' : 'This is a amazing phone'}))