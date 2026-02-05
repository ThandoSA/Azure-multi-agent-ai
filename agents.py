from crewai import Agent
from llm.mock_llm import MockLLM

llm = MockLLM()

research_agent = Agent(
    role="Research Analyst",
    goal="Gather accurate and relevant information on a given topic",
    backstory="You are a meticulous researcher focused on accuracy.",
    llm=llm,
    verbose=True
)

writer_agent = Agent(
    role="Technical Writer",
    goal="Transform research into clear and structured explanations",
    backstory="You excel at explaining complex concepts simply.",
    llm=llm,
    verbose=True
)

reviewer_agent = Agent(
    role="Quality Reviewer",
    goal="Ensure outputs are clear, correct, and complete",
    backstory="You carefully review work to maintain high quality.",
    llm=llm,
    verbose=True
)
