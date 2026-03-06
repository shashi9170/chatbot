from langchain_core.messages import HumanMessage
from src.graph.chatbot_graph import build_graph


class ChatService:

    def __init__(self, memory):
        self.graph = build_graph(memory)

    def chat(self, message, thread_id):

        config = {"configurable": {"thread_id": thread_id}}

        result = self.graph.invoke(
            {"messages": [HumanMessage(content=message)]},
            config=config
        )

        return result["messages"][-1].content