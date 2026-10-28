import os
from dotenv import load_dotenv
from openai import OpenAI

# ক্লায়েন্ট কনফিগারেশন
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY1"),  # আপনার প্রকৃত Groq API কী দিয়ে প্রতিস্থাপন করুন
    base_url="https://api.groq.com/openai/v1",
)

# চ্যাট কমপ্লিশন তৈরি (এখানে মডেলের নাম Groq-এর সমর্থিত মডেলে পরিবর্তন করা হয়েছে)
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",  # অথবা আপনার পছন্দের Groq সমর্থিত মডেল নাম দিন
    messages=["openai/gpt-oss-20b",
        {
            "role": "user",
            "content": "hi\n"
        },
        {
            "role": "assistant",
            "content": "Hello! How can I help you today?"
        },
        {
            "role": "user",
            "content": "Tell me a short joke." # এখানে আপনার প্রশ্নটি লিখুন
        }
    ],
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    stream=True,
    stop=None
)

# রেসপন্স স্ট্রিম প্রিন্ট করা
for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
