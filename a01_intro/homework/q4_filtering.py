from elasticsearch8 import Elasticsearch

def _filter():
    es_client = Elasticsearch('http://localhost:9200')
    query = "How do I execute a command in a running docker container?"

    search_query = {
        "size": 3,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^4", "text"],
                        "type": "best_fields"
                    }
                },
                "filter": {
                    "term": {
                        "course": "machine-learning-zoomcamp"
                    }
                }
            }
        }
    }


    response = es_client.search(index="course-questions", body=search_query)
    return response

if __name__ == "__main__":
    response = _filter()
    print(response[['hits']['hits'][-1]])