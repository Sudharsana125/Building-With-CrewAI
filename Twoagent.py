import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM


load_dotenv()

gemini_llm = LLM(
    model="gemini/gemini-3.5-flash-lite",
    api_key=os.getenv("GEMINI_API_KEY")
)



designer = Agent(
    role="A Designer",
    goal="Design a simple and visually appealing web page layout for a personal portfolio.",
    backstory="You are a creative designer who enjoys making visually appealing and user-friendly web pages.",
    llm=gemini_llm
)


developer = Agent(
    role="A Developer",
    goal="Develop a functional web page based on the provided design.",
    backstory="You are a skilled developer who enjoys turning designs into functional websites.",
    llm=gemini_llm
)


design_task = Task(
    description="Design a simple and visually appealing web page layout for a personal portfolio.",
    expected_output="A well-structured and visually appealing web page layout for a personal portfolio.",
    agent=designer
)

development_task = Task(
    description="Develop a functional web page based on the design created by the designer.",
    expected_output="A fully functional web page that matches the provided design layout.",
    agent=developer
)

crew = Crew(
    agents=[designer, developer],
    tasks=[design_task, development_task],
    process=Process.sequential
)

result = crew.kickoff()


print("\n--- FINAL RESULT ---")
print(result)