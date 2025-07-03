from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional
from pydantic import BaseModel,Field
import os

load_dotenv('../app/.env')

api_key = os.getenv('GROQ_API_KEY')
# print(api_key)

llm = ChatGroq(api_key=api_key,model='meta-llama/llama-4-scout-17b-16e-instruct')
model = ChatOpenAI(model='gpt-4o-mini')

#schema
class Review(BaseModel):
    keyThemes : list[str] = Field(description="Write down all the key themes as list")
    summary : str = Field(description="A brief summary of product review")
    sentiment : str = Field(description="A literal showing sentiment of review")
    pros : Optional[list[str]] = Field(description="A list showing all pros of the product")
    cons : Optional[list[str]] = Field(description="A list showing all cons of the product")
    name : Optional[str] = Field(description="Name of the reviewer")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke(""" 
    The Apple AirPods Pro are a fantastic choice for anyone looking for high-quality wireless earbuds. They offer excellent sound quality, with rich bass and clear highs. The active noise cancellation feature is impressive, effectively blocking out background noise, making them perfect for commuting or working in noisy environments
    Reviewer Name : Imran 
""")

print(result)
