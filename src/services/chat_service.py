from langchain_core.messages import HumanMessage
from src.graph.chatbot_graph import build_graph


class ChatService:

    def __init__(self, memory):
        self.graph = build_graph(memory)

    def chat(self, message: str, thread_id: str) -> str:

        config = {"configurable": {"thread_id": thread_id}}

        result = self.graph.invoke(
            {"messages": [HumanMessage(content=message)]},
            config=config
        )

        last_message = result["messages"][-1]
        content = last_message.content
        print(result)
        # Gemini sometimes returns structured content
        if isinstance(content, list):
            return content[0]["text"]

        return content