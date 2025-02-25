from fastapi import FastAPI
from langserve import add_routes
import uvicorn

from chain import get_chain

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(title="LangServe Launch Example")

add_routes(app, get_chain())

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)