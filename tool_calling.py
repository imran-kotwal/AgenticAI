#How to connect tool to LLM

#Tool Binding : Step of connecting/registering a tool with LLM
#LLM understands what has to be done
from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
import os;
from dotenv import load_dotenv

load_dotenv('../app/.env')

@tool
def multiply(a:int,b:int) -> int :
    """Given two numbers a and b this tool return their product"""
    return a*b

print(multiply.invoke({'a':10,'b':5}))

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './daring-atrium-448311-p9-bb3f69b98364.json'

llm = ChatVertexAI(model_name='gemini-1.5-flash')

#bind tool with llm
llm_with_tools = llm.bind_tools([multiply])

#Tool calling : Process in which llm decides during the conversation that it needs to use a specific tool for
#doing a particular task and what arguments are needed for calling the tools

query = HumanMessage('can you multiply 3 and 4')

messages = [query]

result = llm_with_tools.invoke(messages)

#print(result.tool_calls[0])

#IMP : In Tool calling LLM do not execute the tools on their own, they just advice which tool can be called 

#Tool Execution : The step where actual function/tool is run with the help of arguments given by LLM

tool_result = multiply.invoke(result.tool_calls[0])

messages.append(tool_result)

#print(result)

llm_with_tools.invoke(messages)


