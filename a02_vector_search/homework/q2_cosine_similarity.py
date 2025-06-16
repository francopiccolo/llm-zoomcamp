from contextlib import closing

from a02_vector_search.homework.q1_embedding_the_query import embed_documents

def cosine_similarity(v1, v2):
    return v1.dot(v2)

if __name__ == "__main__":
    documents: list[str] = [
        "I just discovered the course. Can I join now?'",
        'Can I still join the course after the start date?'
    ]

    vectors = embed_documents(documents)
    print(cosine_similarity(vectors[0], vectors[1]))
