from elasticsearch8 import Elasticsearch

from a01_intro.homework.getting_data import get_data

def index_data(documents):
    es_client = Elasticsearch('http://localhost:9200')

    index_settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "text": {"type": "text"},
                "section": {"type": "text"},
                "question": {"type": "text"},
                "course": {"type": "keyword"}
            }
        }
    }

    index_name = "course-questions"

    es_client.indices.create(index=index_name, body=index_settings)

    from tqdm import tqdm

    for doc in tqdm(documents):
        es_client.index(index=index_name, document=doc)

if __name__ == "__main__":
    documents = get_data()
    index_data(documents)