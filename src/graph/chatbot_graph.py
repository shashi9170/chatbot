from typing import TypedDict, Annotated

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from langchain_core.messages import BaseMessage, ToolMessage
from langchain_core.runnables import RunnableLambda

from src.tools.tavily_search import tavily_search
from src.tools.db_search import DB_search
from src.llm.gemini_client import get_llm


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def agent_node(state: AgentState):

    llm = get_llm()
    tools = [tavily_search, DB_search]

    llm_with_tools = llm.bind_tools(tools)

    response = llm_with_tools.invoke(state["messages"])

    return {"messages": [response]}


def tool_router(state: AgentState):

    last_message = state["messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tools"

    return END


def tools_node(state: AgentState):

    tools = {
        "tavily_search": tavily_search,
        "DB_search": DB_search,
    }

    last_message = state["messages"][-1]

    tool_call = last_message.tool_calls[0]

    tool_name = tool_call["name"]
    tool_args = tool_call["args"]
    tool_id = tool_call["id"]

    result = tools[tool_name].invoke(tool_args)

    return {
        "messages": [
            ToolMessage(
                content=str(result),
                tool_call_id=tool_id
            )
        ]
    }


def build_graph(memory):

    builder = StateGraph(AgentState)

    builder.add_node("agent", RunnableLambda(agent_node))
    builder.add_node("tools", RunnableLambda(tools_node))

    builder.add_edge(START, "agent")

    builder.add_conditional_edges(
        "agent",
        tool_router
    )

    builder.add_edge("tools", "agent")

    return builder.compile(checkpointer=memory)