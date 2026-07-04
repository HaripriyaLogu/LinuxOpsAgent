from typing import TypedDict

from langgraph.graph import StateGraph, END

from app.nodes.classifier_node import classifier_node
from app.nodes.knowledge_node import knowledge_node
from app.nodes.diagnostic_node import diagnostic_node
from app.nodes.action_node import action_node
from app.nodes.response_node import response_node


class AgentState(TypedDict):

    user_prompt: str
    intent: str
    response: str


graph = StateGraph(AgentState)


graph.add_node("classifier", classifier_node)
graph.add_node("knowledge", knowledge_node)
graph.add_node("diagnostic", diagnostic_node)
graph.add_node("action", action_node)
graph.add_node("response", response_node)


def router(state):

    return state["intent"]


graph.set_entry_point("classifier")


graph.add_conditional_edges(
    "classifier",
    router,
    {
        "knowledge": "knowledge",
        "diagnostic": "diagnostic",
        "action": "action"
    }
)


graph.add_edge("knowledge", "response")
graph.add_edge("diagnostic", "response")
graph.add_edge("diagnostic", "response")
graph.add_edge("action", "response")

graph.add_edge("response", END)

app = graph.compile()