from openai import OpenAI

client = OpenAI(
    api_key="API KEY rahega Yahan"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "Tell me a joke."}
    ]
)

print(completion.choices[0].message.content)
