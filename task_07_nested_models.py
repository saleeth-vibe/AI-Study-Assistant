# from langchain_ollama import ChatOllama
# from pydantic import BaseModel, Field
# from typing import List

# llm = ChatOllama(model="llama3.2:latest")

# class Quiz(BaseModel):
#     topic: str = Field(description="Topic name")
#     question: str = Field(description="Quiz question")
#     options: list[str] = Field(description="Four multiple-choice options")
#     correct_answer: str = Field(description="Correct option")
#     explanation: str = Field(description="Explanation of the correct answer")

# class QuizCollection(BaseModel):
#     quiz: List[Quiz] = Field(description="A list of three quiz questions")

# structured_llm = llm.with_structured_output(QuizCollection)

# response = structured_llm.invoke(
#     "Generate exactly 3 multiple-choice quiz questions about Python programming. "
#     "Each question must have four options, one correct answer, and an explanation."
# )

# print(response.quiz)

from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field

llm = ChatOllama(model="llama3.2:latest")


class Quiz(BaseModel):
    topic: str = Field(description="Topic name")
    question: str = Field(description="Quiz question")
    options: list[str] = Field(description="Four multiple-choice options")
    correct_answer: str = Field(description="Correct option")
    explanation: str = Field(description="Explanation of the correct answer")


class QuizCollection(BaseModel):
    quizzes: list[Quiz] = Field(description="A collection of quiz questions")


structured_llm = llm.with_structured_output(QuizCollection)

response = structured_llm.invoke(
    "Generate exactly 3 multiple-choice quiz questions about Python. "
    "Each question must have four options, one correct answer, and an explanation."
)

for index, quiz in enumerate(response.quizzes, start=1):
    print(f"\nQUIZ {index}")
    print("Topic:", quiz.topic)
    print("Question:", quiz.question)
    print("Options:", quiz.options)
    print("Correct Answer:", quiz.correct_answer)
    print("Explanation:", quiz.explanation)
    print("------------------------")