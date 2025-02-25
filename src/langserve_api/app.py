from fastapi import FastAPI, APIRouter
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
# from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain

load_dotenv()

# os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)


# from langchain_community.llms import HuggingFaceEndpoint
# repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
# # repo_id = "HuggingFaceH4/zephyr-7b-beta"
# llm_test = HuggingFaceEndpoint(repo_id = repo_id, huggingfacehub_api_token = API_KEY)

##ollama llama2
llm=Ollama(model="mistral:instruct")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")
prompt3=ChatPromptTemplate.from_template("Write me a email {topic} for a 5 years child with 100 words")


llm_chain = LLMChain(prompt=prompt3, llm=llm)

add_routes(
    app,
    prompt1|llm,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

add_routes(
    app,
    llm_chain,
    path="/email"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8001)
