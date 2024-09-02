from decouple import config
from openai import OpenAI


OPENAI_MODEL = "gpt-4o-mini"
OPENAI_API_KEY = config("OPENAI_API_KEY", cast=str, default=None)


def get_client():
    return OpenAI(api_key=OPENAI_API_KEY)


def get_llm_response(gpt_messages):
    client = get_client()
    completion = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=gpt_messages
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    if OPENAI_API_KEY is None:
        print("OPENAI_API_KEY is not set. Please check your environment variables.")
    else:
        # Print only the first few characters for security reasons.
        print(f"OPENAI_API_KEY is set correctly: {OPENAI_API_KEY[:10]}...")
