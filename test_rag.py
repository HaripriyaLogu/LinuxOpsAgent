from app.rag import RAG

rag = RAG()

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    docs = rag.retrieve(question)

    print("\nRetrieved Context:\n")

    for doc in docs:
        print(doc)
        print("-" * 50)