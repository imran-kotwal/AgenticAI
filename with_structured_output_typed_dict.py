from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional
import os

load_dotenv('../app/.env')

api_key = os.getenv('GROQ_API_KEY')
# print(api_key)

llm = ChatGroq(api_key=api_key,model='meta-llama/llama-4-scout-17b-16e-instruct')
model = ChatOpenAI(model='gpt-4o-mini')

class Review(TypedDict):
    keyThemes : Annotated[list[str],"Write down all the key themes in the review"]
    summary : Annotated[str,"A brief summary of product review"]
    sentiment : Annotated[str,"Returned Sentiment of product review"]
    pros : Annotated[Optional[list[str]],"All the pros related to the review"]
    cons : Annotated[Optional[list[str]],"All the cons related to the review"]
    name : Annotated[Optional[str],"Name of reviewer"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(""" 
    The Apple AirPods Pro are a fantastic choice for anyone looking for high-quality wireless earbuds. They offer excellent sound quality, with rich bass and clear highs. The active noise cancellation feature is impressive, effectively blocking out background noise, making them perfect for commuting or working in noisy environments
    Reviewer Name : Imran 
""")

print(result)
