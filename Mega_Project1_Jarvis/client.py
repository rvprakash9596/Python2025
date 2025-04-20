from openai import OpenAI

client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "Tell me a joke."}
    ]
)

print(completion.choices[0].message.content)
