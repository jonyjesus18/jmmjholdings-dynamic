import os
import openai
openai.api_key = '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'


response = openai.Completion.create(
  engine="text-davinci-001",
  prompt="Create a list of 8 questions for my interview as a senior mechanical engineer\n",
  temperature=0.5,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response['choices'])
