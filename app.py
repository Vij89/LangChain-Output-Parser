from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    "Give me 5 names of {text}. Return only a comma-separated list."
)

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7
)

chain = prompt | model
response = chain.invoke({"text": "birds"})

print(response.content)