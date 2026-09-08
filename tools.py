from crewai import Agent

researcher = Agent(
    role="AI Researcher",
    goal="Find simple information about artificial intelligence",
    backstory="You are curious and good at understanding AI topics."
)

writer = Agent(
    role="AI Writer",
    goal="Explain AI topics in simple language",
    backstory="You are a clear and friendly technical writer."
)

print("Researcher:")
print(researcher)

print("\nWriter:")
print(writer)