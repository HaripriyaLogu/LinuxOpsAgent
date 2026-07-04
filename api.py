from fastapi import FastAPI
from pydantic import BaseModel

from app.langgraph_agent import app as graph

api = FastAPI(
    title="LinuxOps AI Agent",
    version="1.0"
)


class ChatRequest(BaseModel):
    message: str


@api.get("/")
def home():

    return {
        "message": "LinuxOps AI Agent API is Running"
    }


@api.post("/chat")
def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "user_prompt": request.message
        }
    )

    return {
        "response": result["response"]
    }