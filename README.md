# Taiwan Stock Agent

## Overview
This project is an advanced intelligent assistant developed for the automated analysis of Taiwan stock market data. The system orchestrates OpenAI GPT-4o-mini via the LangChain framework, integrating directly with the Taiwan Stock Exchange (TWSE) OpenAPI. By implementing an Agentic Workflow, the system achieves autonomous task decomposition, real-time data retrieval, and financial reasoning.

---
## Demo
https://github.com/user-attachments/assets/0428bc90-d256-4c65-bc2b-f0f04eb52cab

---

## Key Features
- Autonomous Agentic Reasoning: Leverages LangChain and the ReAct framework to analyze user intent, enabling the agent to perform autonomous logical deduction and decision-making.
- Dynamic Tool Selection: The agent autonomously evaluates user intent to select the most appropriate tools for real-time data retrieval.
- Real-Time TWSE Integration: Directly interfaces with Taiwan Stock Exchange (TWSE) OpenAPI to fetch up-to-date market data and individual stock performance.

---

## System Architecture
1. User Interaction: Natural language queries are captured via the Streamlit interface.

2. Agent Orchestration: The system acts as the agent's "brain". It uses LLMs(GPT-4o-mini) to analyze the user's intent and autonomously decides which steps to take to solve the request.

3. Dynamic Tool Call: The agent selects the appropriate Custom Tool to interface with the TWSE OpenAPI.

4. Observation: The agent analyzes the returned data (Observation).

5. Synthesized Response: A final grounded analysis is generated and rendered for the user.

---

## Installation & Setup

### step1: Environment Setup
1. Clone the repository:
```bash
git clone https://github.com/WenChangB/STOCK_QA_AGENT.git
cd STOCK_QA_AGENT
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### step2: Configuration
Please follow these steps to configure your API Key:

1. Copy `.env.example` and rename it to `.env`
2. Open `.env` and enter your OPENAI_API_KEY and preferred MODEL_NAME (default is gpt-4o-mini).

### step3: Execution
```bash
streamlit run app.py
```

## File Structure
```
├── app.py              # Entry point (Streamlit UI)
├── agent.py            # Core Agentic Workflow logic
├── client.py           # TWSE API communication client
├── tools.py            # Custom tools for Agent invocation
├── config.py           # Environment variable management
├── .env.example        # Environment configuration template
├── .gitignore          # Excludes sensitive files and cache
└── requirements.txt    # Project dependencies
```
