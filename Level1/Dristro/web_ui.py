import streamlit as st
import requests

# Define the base URL for Ollama (default port)
OLLAMA_URL = "http://localhost:11434"  # Adjust this if Ollama runs on a different port

# Streamlit UI setup
st.title("Ollama Llama3.2 Chatbot")
st.write("Type in a prompt and get a response from the Llama3.2 model.")

# Input box for the user's question
user_input = st.text_input("Enter your message:")

# When the user submits input
if st.button("Submit") and user_input:
    # Send request to Ollama for inference
    try:
        response = requests.post(
            f"{OLLAMA_URL}/v1/completions",
            json={"model": "llama3.2:latest", "prompt": user_input},
            timeout=10
        )

        if response.ok:
            # Extract the first choice text from the response JSON
            output = response.json().get("choices", [{}])[0].get("text", "No response received.")
            st.write("Llama3.2's Response:", output)
        else:
            st.write("Error:", response.text)
    except requests.ConnectionError:
        st.write("Could not connect to Ollama. Please check if it’s running and on the correct port.")
