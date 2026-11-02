import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
resp = client.models.generate_content(
    model="gemini-3.7-flash",
    contents="Explain RAG in one sentence.",
)
print(resp.text)

# How to check for available models
# for m in client.models.list():
#     print(m.name)