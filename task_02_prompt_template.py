from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly {subject} computer science teacher."),
    ("human", "{question}")
])

prompt = prompt_template.invoke(
    {
    "subject": "computer science",
    "question": "What is Python?"
    }
)

llm = ChatOllama(model="llama3.2:latest")
response = llm.invoke(prompt)

print(response.content)