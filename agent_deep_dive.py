import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

gemini_llm = LLM(
    model="gemini/gemini-3.8-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

teacher = Agent(
    role="Python Teacher",
    goal="Teach Python concepts in a simple way for beginners",
    backstory="You are a patient Python teacher who enjoys helping beginners understand programming.",
    llm=gemini_llm
)

teaching_task = Task(
    description="Explain what a Python variable is to a complete beginner. Use a simple example.",
    expected_output="A simple explanation of Python variables with one easy example.",
    agent=teacher
)

crew = Crew(
    agents=[teacher],
    tasks=[teaching_task],
    process=Process.sequential
)

result = crew.kickoff()
print(result)
