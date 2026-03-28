import os
from dotenv import load_dotenv
from openai import OpenAI

# cargar variables del .env
load_dotenv()

# create client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Choose a mode:")
print("1. Python Tutor")
print("2. Math Tutor")
print("3. Simple Explainer")

choice = input("Enter 1, 2 or 3: ")

if choice == "1":
    system_prompt = "You are a Python tutor. Explain step by step with simple examples and include code."
elif choice == "2":
    system_prompt = "You are a math tutor. Explain clearly and step by step."
elif choice == "3":
    system_prompt = "Explain things in a very simple way for beginners."
else:
    system_prompt = "You are a helpful assistant."

messages = [{"role": "system", "content": system_prompt}]
print("\n")
print("Chat started (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input == "exit":
        break

    # save users messages
    messages.append({"role": "user", "content": user_input})
    if len(messages) > 20:
        messages = messages[-20:]

    # call AI
    response = client.chat.completions.create(model="gpt-4o-mini",messages=messages)

    ai_response = response.choices[0].message.content.strip()

    print("AI:", ai_response)

    # save AI answers
    messages.append({"role": "assistant", "content": ai_response})