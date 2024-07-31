
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#os.environ["OPEN_API_KEY"]=os.getenv("OPEN_API_KEY")

## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"

# Similar check for LANGCHAIN_API_KEY
#if os.getenv("LANGCHAIN_API_KEY"):
#    os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
#else:
#    st.error("LANGCHAIN_API_KEY is not set in the environment. Please check your .env file.")

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##Prompt Template

prompt=ChatPromptTemplate.from_messages(
[
    ("system","You are a helpful assistant. Please response to the user's question"),
    ("user","Question:{question}")
]
)
##streamlit framework

st.title('Langchain Demo with LLAma2 API')
input_text = st.text_input("Search the topic you wish")

## ollama LLAma2 LLM
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
