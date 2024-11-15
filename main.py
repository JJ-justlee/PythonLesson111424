#from openai import OpenAI

import openai

# OpenAI API 키 설정
openai.api_key = ""

# ChatGPT API 호출 예제
response = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   messages=[
       {"role": "system", "content": "Can you recommend todays dinner menu?"}
   ]
)


# 응답 출력
print(response.choices[0].message['content'])