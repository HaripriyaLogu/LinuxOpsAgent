from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

from app.llm import LLMClient
from app.tools import (
    check_disk,
    check_memory,
    check_cpu,
    check_hostname,
)

llm = LLMClient().langchain_llm

tools = [
    check_disk,
    check_memory,
    check_cpu,
    check_hostname,
]

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are CloudOps AI Assistant.

You are an expert Linux Administrator.

Use tools whenever the user asks about the Linux server.

Never invent Linux outputs.
""",
        ),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

agent = create_tool_calling_agent(
    llm,
    tools,
    prompt,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)