#LLm can thi

# When to use custome tools Different usecase for creating Tools
from langchain_community.tools import tool,StructuredTool,BaseTool
from pydantic import BaseModel,Field
from typing import TypedDict,Type
# When you have to call your own API's
# 3 step process for making tools

#Style 1 of making tool using @tool decorator
@tool
def multiply(a:int,b:int) -> int:
    """Multiply two numbers"""
    return a*b

@tool
def add(a:int,b:int) -> int:
    """Add two numbers"""
    return a+b

print(multiply.invoke({'a' : 2,'b' : 3}))
print(multiply.name)
print(multiply.description)
print(multiply.args)

#structured Tool:
# Special type of way of making tool, it is more structured form for making tools
# Strict constraint

class MultiplyInput(BaseModel):
    a : int = Field(description='First Number to be multipled')
    b : int = Field(description='Second number to be multipled')

def multiply_function(a:int,b:int) -> int:
    return a*b

multiply_tool = StructuredTool.from_function(
    func=multiply_function,
    name='multiply',
    description='Multiply two numbers',
    args_schema=MultiplyInput
)

result3 = multiply_tool.invoke({'a' : 3,'b':10})
print(result3)

#Use BaseTool Class :
#BaseTool :It is a abstract class all tools inherit this class 

class MultiplyTool(BaseTool):
    name : str = "Multiply"
    description : str = 'Multiply two numbers'

    args_schema : Type[BaseModel] = MultiplyInput

    def _run(self,a:int,b:int) -> int:
        return a*b

multiply_tool2 = MultiplyTool()

print(multiply_tool2.invoke({'a':4,'b':2}))

#Toolkit : A collection of reltaed tools that serve a common purpose

class MathToolkit:

    def get_tools(self):
        return [add,multiply]
    
toolkit = MathToolkit()

for tool in toolkit.get_tools():
    print(tool.name)

