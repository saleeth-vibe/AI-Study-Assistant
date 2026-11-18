from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

llm = ChatOllama(model="llama3.2:latest")
parser = StrOutputParser()

question_prompt_Template = ChatPromptTemplate.from_template(
    "Explain a topic in 3 simple lines: {question}"
)

rate_prompt_Template = ChatPromptTemplate.from_template(
    "Question: {question}\nAnswer: {answer}\n\n"
    "Evaluate how clear the explanation is for a 15-year-old. Give a score out of 10 and one line of feedback."
)

explain_chain = question_prompt_Template | llm | parser

feedback_chain = RunnablePassthrough.assign(answer = explain_chain) | rate_prompt_Template | llm | parser

print(feedback_chain.invoke({"question": "What is Machine Learning?"}))