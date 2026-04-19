from langgraph.graph import StateGraph
from typing import TypedDict
from .llm import route_llm
from .rag import retrieve


class State(TypedDict):
    query: str
    context: str
    answer: str


def retriever_node(state: State):
    docs = retrieve(state["query"])
    return {"context": "\n".join(docs)}


def generator_node(state: State):
    prompt = f"""
    Context:
    {state['context']}

    Question:
    {state['query']}

    Answer:
    """
    answer = route_llm(prompt)
    return {"answer": answer}


def build_graph():
    builder = StateGraph(State)

    builder.add_node("retrieve", retriever_node)
    builder.add_node("generate", generator_node)

    builder.set_entry_point("retrieve")
    builder.add_edge("retrieve", "generate")

    return builder.compile()