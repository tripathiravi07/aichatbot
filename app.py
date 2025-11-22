##Loading GROQ API KEY
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

#Import Langchain and streamlit components
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.messages import trim_messages
from operator import itemgetter
from langchain_core.runnables import RunnablePassthrough




st.title("🤖 DevOps Q&A Chatbot 🚀")
groq_api_key=st.sidebar.text_input("🔑 Enter Your GROQ Api Key Here!",type="password")
user_input=st.text_input("I am a DevOps Expert Please Ask Your Questions?")


if user_input and groq_api_key:
    llm=ChatGroq(model="openai/gpt-oss-20b")
    prompt=ChatPromptTemplate.from_messages([
        ("system", "You are an DevOps Expert, Answer questions based upon provided context best of your ability"),
        MessagesPlaceholder(variable_name="messages")
    ])
    trimmer=trim_messages(
        max_tokens=200,
        strategy="last",
        token_counter=llm,
        include_system=True,
        allow_partial=False,
    )
    chain=(
        RunnablePassthrough.assign(messages=itemgetter("messages")|trimmer)
        | prompt
        | llm 
    )

    if "store" not in st.session_state:
        st.session_state.store={}

    def get_session_history(session_id:st)->BaseChatMessageHistory:
        if session_id not in st.session_state.store:
            st.session_state.store[session_id]=ChatMessageHistory()
        return st.session_state.store[session_id]
    SESSION="DefaultSession"
    with_message_history=RunnableWithMessageHistory(chain,get_session_history,input_messages_key="messages")

    config={"configurable":{"session_id": SESSION}}
    response=with_message_history.invoke({"messages": [HumanMessage(content=user_input)]},config=config)
    
    st.markdown("**Assistant Response:**⏎")
    st.write(response.content)

    st.markdown("**RawHistory:**")
    st.code(st.session_state.store)

    st.markdown("**Here Is Your Chat History**")
    history=st.session_state.store.get(SESSION)

    if history:
        try:
            for msg in history.messages:
                st.write(f"- {msg.type}: {getattr(msg,'content',str(msg))}")
        except Exception:
            st.write("Could not pretty-print history. Inspect raw store above.")
    clear = st.button("Clear History ❌")
    if clear:
        if SESSION in st.session_state.store:
            del st.session_state.store[SESSION]
        st.success("Chat History Cleared!")
else:
    st.write("Please enter groq api key and then ask your question")
