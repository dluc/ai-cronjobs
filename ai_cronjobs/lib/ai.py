import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


def run_prompt(prompt, model):
    llm = ChatOpenAI(model_name=model, temperature=0, openai_api_key=openai_api_key)
    response = llm.invoke([{"role": "user", "content": prompt}])
    return response.content.strip()


def run_structured_prompt(prompt, model, output_type):
    llm = ChatOpenAI(model_name=model, temperature=0, openai_api_key=openai_api_key)
    structured_llm = llm.with_structured_output(output_type)
    response = structured_llm.invoke(prompt)
    return response
