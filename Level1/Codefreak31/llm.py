import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Set the API key for Google Generative AI
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    st.warning("Please set your Gemini API key in the .env file.")

# Function to fetch responses from the Gemini model
def fetch_gemini_flash_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # Initialize the model
        response = model.generate_content(prompt)  # Generate content
        return response.text  # Return the response text
    except Exception as e:
        return str(e)  # Return the error message

# Initialize session state for storing fetched queries
if 'responses' not in st.session_state:
    st.session_state.responses = []  # List to store responses

# Streamlit app layout
st.title("Chat with LLM")

# User input for general query or prompt
user_prompt = st.text_input("Enter your general question (e.g., 'What is the capital of France?'): ")

# Button to handle the query
if st.button("Submit Query"):
    if user_prompt:
        with st.spinner(f"Fetching response for your query: '{user_prompt}'..."):
            response_content = fetch_gemini_flash_response(user_prompt)
        
        # Store the fetched response in session state
        st.session_state.responses.append({"query": user_prompt, "response": response_content})


# Display the fetched queries and responses at the bottom
if st.session_state.responses:
    st.subheader("Fetched Queries and Responses:")
    for entry in st.session_state.responses:
        st.markdown(f"**Query:** {entry['query']}")
        st.markdown(f"**Response:** {entry['response']}\n")
