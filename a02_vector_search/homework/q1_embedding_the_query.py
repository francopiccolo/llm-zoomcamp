from fastembed import TextEmbedding


documents: list[str] = [
    "I just discovered the course. Can I join now?'",
]

def embed_documents(documents: list[str]):
    embedding_model = TextEmbedding(model_name="jinaai/jina-embeddings-v2-small-en")
    return list(embedding_model.embed(documents))

if __name__ == "__main__":
    documents: list[str] = [
        "I just discovered the course. Can I join now?'",
    ]
    embeddings_list = embed_documents(documents)
    print(len(embeddings_list[0]))
    print(min(embeddings_list[0]))