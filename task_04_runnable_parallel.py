from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

text = "Artificial Intelligence (AI) is a technology that enables computers to perform tasks that usually require human intelligence. AI can understand language, recognize images, solve problems, and make predictions. Today, AI is used in smartphones, healthcare, education, and transportation. For example, Google Maps uses AI to predict traffic and suggest faster routes. AI helps people save time and make better decisions."

llm = ChatOllama(model="llama3.2:latest")
parser = StrOutputParser()

chain_1 = ChatPromptTemplate.from_template("explain the content in 3 simple lines: {text}") | llm | parser
chain_2 = ChatPromptTemplate.from_template("generate 3 important keywords with short meanings: {text}") | llm | parser
chain_3 = ChatPromptTemplate.from_template("create 2 multiple-choice questions with answers: {text}") | llm | parser

parallel_chain = RunnableParallel({ "explain": chain_1, "keywords": chain_2, "quiz": chain_3 })

result = parallel_chain.invoke({"text": text})


print("EXPLANATION:")
print(result["explain"])

print("\nKEYWORDS:")
print(result["keywords"])

print("\nQUIZ:")
print(result["quiz"])
