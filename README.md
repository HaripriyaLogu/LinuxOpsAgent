<div align="center">

# 🚀 LinuxOps AI Agent

### AI-Powered Cloud Operations Assistant for Linux Infrastructure using Azure OpenAI, LangGraph, RAG & MCP

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-0078D4?logo=microsoftazure)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20Workflow-success)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-FCC624?logo=linux)
![SSH](https://img.shields.io/badge/SSH-Enabled-green)
![License](https://img.shields.io/badge/License-MIT-blue)

</div>

---

# 📌 1. One-Line Description

LinuxOps AI Agent is an intelligent Cloud Operations Assistant that understands natural language, performs Linux diagnostics, securely executes administrative tasks on Linux Virtual Machines, retrieves enterprise knowledge using RAG, integrates external tools through MCP, and provides AI-powered recommendations using Azure OpenAI.

---

# 📖 2. Abstract

LinuxOps AI Agent is an enterprise-grade Agentic AI solution designed to simplify Linux administration and cloud operations.

The system enables administrators to interact with Linux servers using natural language instead of manually executing commands. The agent classifies user requests, determines the appropriate workflow using LangGraph, retrieves organization-specific documentation using Retrieval-Augmented Generation (RAG), accesses enterprise tools via Model Context Protocol (MCP), securely connects to Azure Linux Virtual Machines over SSH, executes approved commands, analyzes the command outputs using Azure OpenAI, and provides professional recommendations.

The architecture emphasizes modularity, safety, extensibility, and explainability, making it suitable for modern CloudOps, DevOps, and Site Reliability Engineering (SRE) environments.

---

# 🏗️ 3. Architecture Diagram

<p align="center">

<img src="C:\Users\HP\Downloads\Haripriya_Personal\AI Projects\LinuxOpsAgent\docs\architect.png" width="1000">

</p>

---

# 📂 4. Project Structure

```text
LinuxOpsAgent
│
├── app
│   ├── action_engine.py
│   ├── agent.py
│   ├── classifier.py
│   ├── config.py
│   ├── langgraph_agent.py
│   ├── langgraph_planner.py
│   ├── llm.py
│   ├── logger.py
│   ├── memory.py
│   ├── planner.py
│   ├── prompts.py
│   ├── rag.py
│   ├── vector_store.py
│   ├── safety.py
│   ├── ssh_client.py
│   ├── tools.py
│   │
│   ├── nodes
│   │     ├── classifier_node.py
│   │     ├── knowledge_node.py
│   │     ├── diagnostic_node.py
│   │     ├── action_node.py
│   │     └── response_node.py
│   │
│   └── knowledge
│
├── docs
│     └── images
│           ├── architecture.png
│           └── workflow.png
│
├── main.py
├── main_langgraph.py
├── requirements.txt
├── README.md
└── .env.example
```

---

# 📘 5. Project Explanation

## 🎯 Purpose

The primary objective of this project is to automate Linux system administration using Generative AI while maintaining enterprise-level security and approval workflows.

Instead of manually connecting to servers and executing commands, administrators can communicate with the AI agent using natural language.

---

## ⚙️ How It Works

1. User submits a request in natural language.
2. LangGraph orchestrates the workflow.
3. Intent Classifier identifies the request type.
4. Planner determines the required Linux tools.
5. RAG retrieves organization-specific knowledge.
6. MCP communicates with external enterprise tools.
7. Action Engine generates Linux commands.
8. Safety Engine validates commands.
9. User approval is requested before execution.
10. SSH Client securely connects to Azure Linux VM.
11. Linux command output is collected.
12. Azure OpenAI analyzes the results.
13. Professional recommendations are returned.

---

## 🧩 Core Components

- Intent Classifier
- LangGraph Workflow Engine
- Planner Engine
- Tool Registry
- SSH Client
- Action Engine
- Safety Engine
- Azure OpenAI Integration
- Conversation Memory
- Logger
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Database
- Model Context Protocol (MCP)

---

## 🌟 Benefits

- AI-assisted Linux Administration
- Natural Language Interface
- Secure SSH Execution
- Enterprise Knowledge Retrieval
- Safe Command Validation
- Modular Agent Architecture
- Faster Incident Resolution
- Reduced Manual Operations
- Extensible Design for Enterprise Systems

---

# 🔄 6. Workflow Diagram

<p align="center">

<img src="C:\Users\HP\Downloads\Haripriya_Personal\AI Projects\LinuxOpsAgent\docs\workflow.png" width="1100">

</p>

---

# ⭐ 7. Features

### 🤖 AI Features

- Natural Language Understanding
- Intent Classification
- Intelligent Planning
- Linux Knowledge Assistant
- AI-Powered Diagnostics
- Automated Command Generation
- Professional Report Generation

---

### ☁️ Cloud Features

- Azure OpenAI Integration
- Azure Linux VM Integration
- Secure SSH Communication

---

### 🧠 Agentic AI Features

- LangGraph Workflow Orchestration
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Search
- Model Context Protocol (MCP)
- Conversation Memory
- Logging
- Tool Registry
- Modular Architecture

---

### 🔒 Security Features

- Command Validation
- User Approval Workflow
- Safe Execution Policy
- Restricted Linux Operations
- Audit Logging

---

# 🛠️ 8. Technologies Used

| Category | Technology |
|------------|----------------|
| Programming Language | Python |
| LLM | Azure OpenAI GPT-4.1-mini |
| Agent Framework | LangGraph |
| Cloud Platform | Microsoft Azure |
| Operating System | Ubuntu Linux VM |
| Remote Execution | Paramiko (SSH) |
| AI Knowledge | Retrieval-Augmented Generation (RAG) |
| Vector Database | ChromaDB |
| Tool Integration | MCP (Model Context Protocol) |
| Configuration | python-dotenv |
| Version Control | Git & GitHub |

---

# 📷 9. Artifacts

### Linux Knowledge Assistant

- AI-based Linux Administration
- Linux Command Explanation
- Troubleshooting Guidance

---

### Diagnostic Workflow

- Filesystem Analysis
- Memory Analysis
- CPU Analysis
- Health Reports

---

### Action Workflow

- Linux Command Generation
- User Approval
- Secure SSH Execution
- AI Output Analysis

---

### Enterprise AI Features

- LangGraph Workflow
- Azure OpenAI
- RAG Knowledge Retrieval
- MCP Tool Integration

---

# 👩‍💻 Author

**Haripriya**

AI Engineer | Linux Administrator | Cloud & Generative AI Enthusiast

---

<div align="center">

### ⭐ If you found this project interesting, consider giving it a star!

</div>