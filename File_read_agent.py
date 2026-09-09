import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import FileReadTool

load_dotenv()

gemini_llm = LLM(
    model="gemini/gemini-3.5-flash-lite",
    api_key=os.getenv("GEMINI_API_KEY")
)

file_tool = FileReadTool()

assistant = Agent(
    role="File Assistant",
    goal="Read and understand files accurately",
    backstory="You are a careful assistant who reads files and explains their contents clearly.",
    tools=[file_tool],
    llm=gemini_llm
)

task = Task(
    description="Read sample.txt and explain what it says.",
    expected_output="A simple summary of the file.",
    agent=assistant
)

crew = Crew(
    agents=[assistant],
    tasks=[task],
    process=Process.sequential
)

result = crew.kickoff()

print("\n--- RESULT ---")
print(result)