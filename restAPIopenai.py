import openai


# OpenAI API 키 설정
openai.api_key = ""  # 여기에 자신의 OpenAI API 키를 넣으세요.

def ask_gpt_about_menu(menu):
   # ChatGPT API 호출
   response = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages=[
           {"role": "system", "content": "You are a helpful assistant."},
           {"role": "user", "content": f"Can you tell me more about '{menu}' and suggest a way to prepare it?"}
       ]
   )

   # 응답 반환
   return response.choices[0].message['content']

def main():
   # 사용자에게 메뉴 입력 받기
   menu = input("Please enter a menu item you'd like to know about: ")

   # 메뉴에 대해 GPT에게 질의
   response = ask_gpt_about_menu(menu)

   # 응답 출력
   print("\nGPT's Response:")
   print(response)

if __name__ == "__main__":
   main()