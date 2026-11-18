from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly {subject} computer science teacher. Explain in under 100 words and include one real-life example."),
    ("human", "{question}")
])

llm = ChatOllama(model="llama3.2:latest")
parser = StrOutputParser()
chain = prompt_template | llm | parser

result = chain.invoke({
    "subject": "computer science",
    "question": "What is Python?"
})

print(result)

# for chunk in chain.stream(
#     {
#          "subject": "computer science",
#          "question": "What is Python?"
#     }
# ):
#     print(chunk, end="", flush=True)