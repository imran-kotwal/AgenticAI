from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI
from langchain_core.tools import tool
import requests

#Simple conversion factor based Tool
#There would be 2 tools 
#First one would fetch the conversion factor from api 
#2nd tool would do the multiplcation

def getConversionFactor(baseCurr : str,targetCurr : str) -> float:
    """This function fetched currency conversion factor between given base currency and target currency"""
    