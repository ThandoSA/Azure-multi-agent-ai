from crewai import Task
from agents import research_agent, writer_agent, reviewer_agent

research_task = Task(
    description="Research what multi-agent AI systems are and their benefits.",
    expected_output="A list of key research insights.",
    agent=research_agent
)

writing_task = Task(
    description="Write a clear explanation based on the research.",
    expected_output="A structured and easy-to-understand explanation.",
    agent=writer_agent
)

review_task = Task(
    description="Review and improve the explanation for clarity and accuracy.",
    expected_output="A polished final version.",
    agent=reviewer_agent
)
