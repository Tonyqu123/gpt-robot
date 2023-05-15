import openai
import os
api_key = os.getenv("API_KEY")


openai.api_key = api_key

prefix = "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\"."
usa="Q: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years."
user_question="Q: Where is the Valley of Kings?\n"
mytuple=(prefix,usa,user_question)
raw='\r\n'.join(mytuple)
print(raw)
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=raw,

  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)
print(response)