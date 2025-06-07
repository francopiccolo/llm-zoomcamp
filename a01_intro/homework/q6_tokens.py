import tiktoken

from a01_intro.homework.q5_building_a_prompt import build_prompt

encoding = tiktoken.encoding_for_model("gpt-4o")
prompt = build_prompt()
print(len(encoding.encode(prompt)))
