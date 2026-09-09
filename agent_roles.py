from crewai import Agent, Crew, Process

researcher = Agent(
    role="AI Researcher",
    goal="Find simple information about AI",
    backstory="You are curious about AI."
)

writer = Agent(
    role="AI Writer",
    goal="Explain AI topics simply",
    backstory="You explain technical topics clearly."
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[],
    process=Process.sequential
)

print(crew)