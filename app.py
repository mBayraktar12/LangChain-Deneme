from langchain.llms import OpenAI
import streamlit as st
import os

from dotenv import load_dotenv

load_dotenv()

def get_openai_response(question):
    llm = OpenAI(openai_api_key = os.getenv("OPENAI_API_KEY"), temperature=0.5)
    response = llm(question)
    return response

### streamlit

st.set_page_config(page_title="Q&A Experiment")
st.header("Langchain App")

input = st.text_input("Input: ", key="input")

submit=st.button("Ask a question here!")

response = get_openai_response(input)

if submit:
    st.subheader("The response is")
    st.write(response)
