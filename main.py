from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA

load_dotenv()

llm = ChatNVIDIA(model="meta/llama-3.3-70b-instruct")

response = llm.invoke("Explain Agentic AI in one line")

print(response.content)