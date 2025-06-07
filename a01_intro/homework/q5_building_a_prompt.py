from a01_intro.homework.q4_filtering import _filter
CONTEXT_TEMPLATE = """
Q: {question}
A: {text}
"""

PROMPT_TEMPLATE = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
"""

def build_prompt():
    context_template = CONTEXT_TEMPLATE.strip()

    context = ""
    response = _filter()
    for resp in response['hits']['hits']:
        question = resp['_source']['question']
        ans = resp['_source']['text']
        context = context + context_template.format(question=question, text=ans) + "\n\n"


    prompt_template = PROMPT_TEMPLATE.strip()

    query = "How do I execute a command in a running docker container?"

    return prompt_template.format(question=query, context=context)

if __name__ == "__main__":
    prompt = build_prompt()
    print(prompt)
    print(len(prompt))