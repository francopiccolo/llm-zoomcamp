from a02_vector_search.homework.q1_embedding_the_query import embed_documents
from a02_vector_search.homework.q2_cosine_similarity import cosine_similarity

if __name__ == "__main__":
    query_document = [
        "I just discovered the course. Can I join now?'",
    ]
    query_vector = embed_documents(query_document)[0]
    documents = [
        {
            'text': "Yes, even if you don't register, you're still eligible to submit the homeworks.\nBe aware, however, that there will be deadlines for turning in the final projects. So don't leave everything for the last minute.",
            'section': 'General course-related questions',
            'question': 'Course - Can I still join the course after the start date?',
            'course': 'data-engineering-zoomcamp'
        },
        {
            'text': 'Yes, we will keep all the materials after the course finishes, so you can follow the course at your own pace after it finishes.\nYou can also continue looking at the homeworks and continue preparing for the next cohort. I guess you can also start working on your final capstone project.',
            'section': 'General course-related questions',
            'question': 'Course - Can I follow the course after it finishes?',
            'course': 'data-engineering-zoomcamp'
        },
        {
            'text': "The purpose of this document is to capture frequently asked technical questions\nThe exact day and hour of the course will be 15th Jan 2024 at 17h00. The course will start with the first  “Office Hours'' live.1\nSubscribe to course public Google Calendar (it works from Desktop only).\nRegister before the course starts using this link.\nJoin the course Telegram channel with announcements.\nDon’t forget to register in DataTalks.Club's Slack and join the channel.",
            'section': 'General course-related questions',
            'question': 'Course - When will the course start?',
            'course': 'data-engineering-zoomcamp'
        },
        {
            'text': 'You can start by installing and setting up all the dependencies and requirements:\nGoogle cloud account\nGoogle Cloud SDK\nPython 3 (installed with Anaconda)\nTerraform\nGit\nLook over the prerequisites and syllabus to see if you are comfortable with these subjects.',
            'section': 'General course-related questions',
            'question': 'Course - What can I do before the course starts?',
            'course': 'data-engineering-zoomcamp'
        },
        {
            'text': 'Star the repo! Share it with friends if you find it useful ❣️\nCreate a PR if you see you can improve the text or the structure of the repository.',
            'section': 'General course-related questions',
            'question': 'How can we contribute to the course?',
            'course': 'data-engineering-zoomcamp'
        }
    ]
    docs_text = [doc["question"] + doc["text"] for doc in documents]
    vectors = embed_documents(docs_text)
    for i, v in enumerate(vectors):
        print(i, cosine_similarity(v, query_vector))