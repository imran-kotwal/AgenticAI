from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv('../app/.env')

llm = ChatOpenAI(model='gpt-4o-mini')
llm2 = ChatAnthropic(model_name='claude-3')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate short and simple notes from following text \n {text}',
    input_variables=['text'],
)

prompt2 = PromptTemplate(
    template='Generate 5 small questions from following text \n {text}',
    input_variables=['text'],
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into single document\n -> {notes} \n {quiz}',
    input_variables=['notes','quiz'],

)


parallel_chain = RunnableParallel({
    'notes' : prompt1 | llm | parser,
    'quiz' : prompt2 | llm | parser
})

merge_chain = prompt3 | llm | parser

parallel_chain = parallel_chain | merge_chain

text = """
Supervised Learning: The model is trained on labeled data. Common algorithms include linear regression, decision trees, and support vector machines.
Unsupervised Learning: The model is trained on unlabeled data to find hidden patterns. Examples include clustering algorithms like K-means and hierarchical clustering.
Reinforcement Learning: The model learns by interacting with an environment and receiving feedback. It's used in applications like game playing and robotics.
Deep Learning: A subset of ML that uses neural networks with many layers (deep networks) to model complex patterns in data. It's particularly effective for image and speech recognition.
Applications of Machine Learning
Healthcare: Predicting diseases, optimizing treatment plans, and personalizing medicine using patient data 1.
Finance: Fraud detection, stock price prediction, and risk management 1.
Retail: Sales forecasting, customer segmentation, and sentiment analysis of product reviews 1.
Transportation: Predicting vehicle counts, optimizing routes, and forecasting ride requests 1.
Environmental Science: Monitoring pollution, predicting rainfall, and analyzing satellite imagery for deforestation
"""

result = parallel_chain.invoke({'text' : text})

print(result)