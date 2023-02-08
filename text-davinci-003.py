import os
import openai
import sys


openai.api_key = os.getenv("OPENAI_API_KEY")
# title = sys.argv[1]
title = input ("What you would like to talk about?")
# print (title)
print ("Your title is:" + title)

new_prompt = "I want to write a blog posy about" + title 

synopsis = openai.Completion.create(
            model="text-davinci-003",
            # below we have a manually inputed question to GPT-3
            ################# prompt="I want to write a blog post of healthcare",
            # Below we ask for an input of that title or question 

            prompt = new_prompt,

            # print (prompt),

            # The end of the title fix and caall

            max_tokens=3000,
            temperature=0.7
          )
print (synopsis.choices[0].text)