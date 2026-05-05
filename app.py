import streamlit as st
from agent import create_stock_agent
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(page_title="AI Stock Agent", layout="centered")

if "agent_executor" not in st.session_state:
    st.session_state.agent_executor = create_stock_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("華碩股票價格？"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    chat_history_objs = []
    for m in st.session_state.messages:
        if m["role"] == "user":
            chat_history_objs.append(HumanMessage(content=m["content"]))
        else:
            chat_history_objs.append(AIMessage(content=m["content"]))

    with st.chat_message("assistant"):
        with st.spinner("正在分析數據..."):
            response = st.session_state.agent_executor.invoke({
                "input": prompt,
                "chat_history": chat_history_objs
            })
            
        answer = response["output"]
        st.markdown(answer)
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": answer})