from crewai import Crew
from tasks import research_task, writing_task, review_task

crew = Crew(
    agents=[
        research_task.agent,
        writing_task.agent,
        review_task.agent
    ],
    tasks=[
        research_task,
        writing_task,
        review_task
    ],
    verbose=True
)

result = crew.kickoff(
    inputs={
        "topic": "Multi-agent AI systems in enterprise environments"
    }
)

print("\n================ FINAL OUTPUT ================\n")
print(result)
