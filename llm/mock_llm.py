from llm.base import BaseLLM

class MockLLM(BaseLLM):
    def invoke(self, prompt: str):
        class Response:
            def __init__(self, content):
                self.content = content

        return Response(
            content=(
                "[MOCK LLM RESPONSE]\n\n"
                "This response simulates an LLM output.\n\n"
                f"Prompt received:\n{prompt}\n\n"
                "Generated reasoning:\n"
                "- Identified key concepts\n"
                "- Structured information logically\n"
                "- Produced a coherent response\n"
            )
        )
