import openai

openai.api_key = "your-openai-api-key"

def generate_post(topic):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful social media content writer."},
            {"role": "user", "content": f"Write a short, engaging post about {topic}."}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    topic = "Benefits of using AI for business"
    print(generate_post(topic))
