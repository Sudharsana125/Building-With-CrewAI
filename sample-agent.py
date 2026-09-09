from crewai import Agent

teacher = Agent(
    role = "A teacher",
    goal = "Teaching Physics to 10 th std student",
    backstory = "You are a patient Physics teacher who enjoys helping students understand basic concepts."
)
print((teacher))