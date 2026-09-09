import os
from dotenv import load_dotenv

from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai.rag.embeddings.providers.google.generative_ai import GenerativeAiProvider


load_dotenv()


# -------------------------
# Gemini LLM
# -------------------------

gemini_llm = LLM(
    model="gemini/gemini-3.5-flash-lite",
    api_key=os.getenv("GEMINI_API_KEY")
)


# -------------------------
# Gemini Embeddings
# -------------------------

google_embedder = GenerativeAiProvider(
    model_name="gemini-embedding-001",
    api_key=os.getenv("GEMINI_API_KEY"),
    task_type="RETRIEVAL_DOCUMENT"
)


# -------------------------
# Knowledge Source
# -------------------------

company_knowledge = TextFileKnowledgeSource(
    file_paths=["company_info.txt"]
)


# -------------------------
# Agent
# -------------------------

company_agent = Agent(
    role="Company Information Assistant",
    goal="Answer questions using the company information",
    backstory="You are an assistant who carefully uses company information to answer questions.",
    llm=gemini_llm,
    knowledge_sources=[company_knowledge]
)


# -------------------------
# Task
# -------------------------

task = Task(
    description="What is NovaFlow and when was NovaTech AI founded?",
    expected_output="A clear answer using the information from the company file.",
    agent=company_agent
)


# -------------------------
# Crew
# -------------------------

crew = Crew(
    agents=[company_agent],
    tasks=[task],
    process=Process.sequential,
    embedder=google_embedder
)


# -------------------------
# Run
# -------------------------

result = crew.kickoff()


print("\n--- RESULT ---")
print(result)