import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY1"),
    base_url="https://api.groq.com/openai/v1"
)

SYSTEM_PROMPT = "tumi ekjon antorik AI assistant. sob somoy sohoj banglish a uttor dibe. Technical word (jemon API, code) English- ei rakhbe. answer ojotha lomba korbe na"

messages = [{
"role": "system", 
"content": SYSTEM_PROMPT
}]

print("Chatbot chalu holo! kotha ses hole likhun: exit")

while True:
    user_input = input("\n You: ")          
    if user_input.strip().lower() in ["exit", "quit", "bye"]:       
        print("\n Chatbot: Aj tahole asi, abar kotha hobe!")
        break
        
    messages.append({
        "role": "user", 
        "content": user_input
    })
    
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages
    )

    reply = response.choices[0].message.content
    print(f"\n Chatbot: {reply}")

    messages.append({
        "role": "assistant", 
        "content": reply
    })

