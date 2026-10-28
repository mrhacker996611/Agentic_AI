import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from a .env file
load_dotenv()

# to clear any existing environment variables that might interfere with the API calls
for key in ["OPENAI_BASE_URL", "GROQ_BASE_URL", "HTTP_PROXY", "HTTPS_PROXY"]:
    if key in os.environ:
        del os.environ[key]

# initialize the Groq client with the API key
client = Groq(
    api_key=os.getenv("GROQ_API_KEY2")
)

print("🤖 AI Chatbot started!(to exit, type 'exit' or 'quit')\n")

# to create a loop that continuously takes user input and generates AI responses
while True:
    try:
        # to take user input
        user_question = input("\nYou: ")
        
        # to 
        if user_question.lower() in ['exit', 'quit']:
            print("Chatbot closing... happy chatting!")
            break
            
        # if user_question.strip() is empty, skip to the next iteration
        if not user_question.strip():
            continue

        # to call Groq API 
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": user_question  # here we use the user's input directly
                }
            ],
            temperature=1,
            max_completion_tokens=2048,
            top_p=1,
            stream=True,
            stop=None
        )

        print("AI: ", end="")
        # to stream the response in real-time
        for chunk in completion:
            if chunk.choices and chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="")
        print() # to add a newline after the response
    except Exception as e:
        print(f"\nThere was an error:\n{e}")
        break
