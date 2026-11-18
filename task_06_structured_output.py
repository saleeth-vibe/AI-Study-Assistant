from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field

llm = ChatOllama(model="llama3.2:latest")

text = """
Python is a popular high-level programming language known for its simple and readable syntax.
It is used in web development, artificial intelligence, machine learning, data science, and automation.
Python supports different programming styles, including object-oriented and functional programming.
It has many libraries, such as NumPy, Pandas, and TensorFlow, which help developers build applications efficiently.
Python is beginner-friendly and widely used by developers around the world.
"""

class QuizQuestion(BaseModel):
    topic: str = Field(description="Topic name")
    question: str = Field(description="Quiz question")
    options: list[str] = Field(description="Four multiple-choice options")
    correct_answer: str = Field(description="Correct option")
    explanation: str = Field(description="Explanation of the correct answer")

structured_output = llm.with_structured_output(QuizQuestion)

response = structured_output.invoke(
    f"""
    Based on the following text, generate one multiple-choice quiz question.
    Include exactly four options, one correct answer, and an explanation.

    Text: {text}
    """
)

dis_output = response.model_dump()
print(dis_output)
