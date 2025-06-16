from qdrant_client import QdrantClient, models

def delete_qd_collection(collection):
    qd_client = QdrantClient("http://localhost:6333")
    qd_client.delete_collection(collection_name=collection)

def create_qd_collection(name, dim):
    qd_client = QdrantClient("http://localhost:6333")
    qd_client.create_collection(
        collection_name=collection,
        vectors_config=models.VectorParams(
            size=EMBEDDING_DIMENSIONALITY,
            distance=models.Distance.COSINE
        )
    )

def create_payload_index():
    qd_client = QdrantClient("http://localhost:6333")
    qd_client.create_payload_index(
        collection_name=collection,
        field_name="course",
        field_schema="keyword"
    )

def index_documents(docs, collection_name, model_handle):
    qd_client = QdrantClient("http://localhost:6333")
    points = []

    for i, doc in enumerate(docs):
        text = doc['question'] + ' ' + doc['text']
        vector = models.Document(text=text, model=model_handle)
        point = models.PointStruct(
            id=i,
            vector=vector,
            payload=doc
        )
        points.append(point)

    qd_client.upsert(
        collection_name=collection_name,
        points=points
    )


def vector_search(question, collection, limit=1):
     qd_client = QdrantClient("http://localhost:6333")
     query_points = qd_client.query_points(
         collection_name=collection,
         query=models.Document(
             text=question,
             model=model_handle
         ),
         # query_filter=models.Filter(
         #     must=[
         #         models.FieldCondition(
         #             key="course",
         #             match=models.MatchValue(value=course)
         #         )
         #     ]
         # ),
         limit=limit,
         with_payload=True
     )

     return query_points.points

if __name__ == "__main__":
    import requests

    docs_url = 'https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json'
    docs_response = requests.get(docs_url)
    documents_raw = docs_response.json()


    documents = []

    for course in documents_raw:
        course_name = course['course']
        if course_name != 'machine-learning-zoomcamp':
            continue

        for doc in course['documents']:
            doc['course'] = course_name
            documents.append(doc)

    collection = "zoomcamp-faq"
    EMBEDDING_DIMENSIONALITY = 384
    model_handle = "BAAI/bge-small-en"

    delete_qd_collection(collection)
    create_qd_collection(collection, EMBEDDING_DIMENSIONALITY)

    index_documents(documents, collection, model_handle)

    print(vector_search("I just discovered the course. Can I join now?'", collection)[0].score)

