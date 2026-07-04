from app.rag import RAG
from app.llm import LLMClient

rag = RAG()
llm = LLMClient()


def knowledge_node(state):

    question = state["user_prompt"]

    documents = rag.retrieve(question)

    context = "\n\n".join(documents)

    prompt = f"""
You are a Senior Linux Administrator.

Answer ONLY using the retrieved context below.

If the context does not contain the answer, clearly say:

"I couldn't find this information in the knowledge base."

Retrieved Context:

{context}

Question:

{question}
"""

    answer = llm.ask(prompt)

    return {
        "response": answer
    }