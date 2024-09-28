from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "あなたは有能なアシスタントです."},
        {
            "role": "user",
            "content": "プログラミングにおける再帰についての俳句を作ってください."
        }
    ]
)

print(completion.choices[0].message)
