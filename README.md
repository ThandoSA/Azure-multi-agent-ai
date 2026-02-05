Designed and implemented a multi-agent AI system using CrewAI with a pluggable LLM architecture.
The system supports mock and cloud-based LLM providers, enabling seamless migration to Azure OpenAI for production use.

Multi-agent-AI-system/
│
├── llm/
│   ├── __init__.py
│   ├── base.py
│   ├── mock_llm.py
│
├── agents.py
├── tasks.py
├── main.py
├── README.md
└── venv/
