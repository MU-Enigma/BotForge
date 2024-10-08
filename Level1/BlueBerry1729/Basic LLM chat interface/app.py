from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv(".env")

fetcheed_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key = fetcheed_api_key)

model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat()

def LLM_Response(question):
    response = chat.send_message(question,stream=True)
    return response

st.title("Chat Interface for Google-Pro")

user_asks = st.text_input("Ask a question:")
btn = st.button("Ask")

if btn and user_asks:
    result = LLM_Response(user_asks)
    st.subheader("Response : ")
    for word in result:
        st.text(word.text)