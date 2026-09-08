import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

gemini_llm = LLM(
    model="gemini/gemini-3.8-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

researcher = Agent(
    role="AI Researcher",
    goal="Explain AI concepts in a simple and clear way",
    backstory="You are an AI researcher who loves making complex topics easy to understand.",
    llm=gemini_llm
)

research_task = Task(
    description="Explain what Agentic AI is in simple terms for a beginner.",
    expected_output="A clear explanation of Agentic AI with a simple real-world example.",
    agent=researcher
)

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    process=Process.sequential
)

result = crew.kickoff()

print("\n--- FINAL RESULT ---\n")
print(result)