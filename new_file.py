import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

gemini_llm = LLM(
    model="gemini/gemini-3.8-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

Maths_agent = Agent(
    role = "Maths Teacher",
    goal = "Teach the maths addition sum kindly to studentsin simple way",
    backstory = "You are a patient Maths teacher who enjoys helping students understand basic arithmetic.",
    llm = gemini_llm
)

maths_task = Task(
    description = "Explain what a Maths addition sum is to a complete beginner. Use a simple example.",
    expected_output = "A simple explanation of Maths addition sum with one easy example.",
    agent = Maths_agent
)

crew = Crew(
    agents = [Maths_agent],
    tasks = [maths_task],
    process = Process.sequential
)
result = crew.kickoff()
print("\n--- FINAL RESULT ---\n")
print(result)
