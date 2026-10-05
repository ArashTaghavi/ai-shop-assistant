from shop_assistant import (
    Document,
    Embedder,
    VectorStore,
    ContextBuilder,
    PromptBuilder,
    Generator,
    ChatHistory,
    HistorySummarizer,
)
from shop_assistant.utils import rtl_print


def pipeline(model="gemma4:e4b-it-qat"):

    # Run once
    document = Document(file_path="./rules.txt")
    documents = document.load()

    embedder = Embedder()
    embeddings = embedder.embed(texts=documents)

    store = VectorStore(
        documents=documents,
        embeddings=embeddings,
    )

    generator = Generator(model=model)

    summarizer = HistorySummarizer(generator=generator)

    history = ChatHistory(
        summarizer=summarizer,
        max_messages=10,
        keep_recent=4,
    )

    # Run for each query
    while True:
        query = input("شما: ").strip()

        if query.lower() == "q":
            rtl_print("Goodbye!")
            break

        if query.lower() == "h":
            rtl_print(history.get_messages(for_history=True), title="خلاصه مکالمه")
            continue

        rtl_print(f"\nشما: {query}\n")

        # Query embedding
        query_embedding = embedder.embed(texts=[query])

        # Retrieval
        retrieved_documents = store.search(query_embedding=query_embedding[0])

        # Build context
        context_builder = ContextBuilder(retrieved_documents=retrieved_documents)
        context = context_builder.build()

        # Build prompt
        prompt_builder = PromptBuilder(
            query=query,
            context=context,
            chat_history=history.get_messages(for_history=True),
        )
        prompt = prompt_builder.build()

        # Generate answer
        answer = generator.answer(prompt=prompt)

        # Update Chat History
        history.add_user_message(query)
        history.add_ai_message(answer)

        rtl_print(f"\n🤖: {answer}\n")
