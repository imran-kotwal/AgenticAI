from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import ShellTool

search_tool = DuckDuckGoSearchRun()
shell_tool = ShellTool()

results = search_tool.invoke("ipl news")
results2 = shell_tool.invoke('Who i am')

print(results)
