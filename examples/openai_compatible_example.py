from openai import OpenAI

client = OpenAI(
    base_url="https://your-umoja-url",
    api_key="none"
)

response = client.chat.completions.create(
    model="gpt-oss:20b",
    messages=[
        {"role": "user", "content": "What is Umoja Compute?"}
    ]
)

print(response.choices[0].message.content)