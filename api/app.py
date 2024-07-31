from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn 
import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
#from ollama import model
from langchain_community.chat_models import ChatOpenAI

load_dotenv()

#os.environ["OPEN_API_KEY"]=os.getenv("OPEN_API_KEY")

app=FastAPI(
        title="Langchain Server",
        version="1.0",
        description="A simple API Server"
)

# add_routes(
#     app,
#     ChatOpenAI(),
#     path="/openai"
# )
#model=ChatOpenAI()

##ollama llama2
llm=Ollama(model="llama2")
#llm = model("llama2")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
#prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words")

# add_routes(
#     app,
#     prompt1|model,
#     path="/essay"
# )

add_routes(
    app,
    prompt1|llm,
    path="/essay"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)