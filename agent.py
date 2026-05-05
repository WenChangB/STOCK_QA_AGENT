from config import OPENAI_API_KEY, MODEL_NAME
from tools import tools
from prompts import SYSTEM_PROMPT
from langchain_openai import ChatOpenAI
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def create_stock_agent():
    llm = ChatOpenAI(
        model = MODEL_NAME,
        openai_api_key = OPENAI_API_KEY
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name = "chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name = "agent_scratchpad")
    ])

    agent = create_tool_calling_agent(llm, tools, prompt)
    
    return AgentExecutor(
        agent = agent,
        tools = tools,
        verbose = True,
        handle_parsing_errors = True
    )