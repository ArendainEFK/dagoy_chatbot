import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from chat_history import chat_history

# Configure API key from environment variable
load_dotenv()

# Streamlit page configuration
st.set_page_config(
    page_title="Chat with Dagoy!",
    page_icon=":city_sunrise:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Configure Google Generative AI
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Model configuration
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

# Safety settings for the model
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

# Initialize the Generative Model
model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

# Function to translate user roles for display in Streamlit needed for better streamlit application
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session if not already in session state
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Function to get response from the model based on user input and chat history allows for multi-level prompting
def get_response(user_input):
  """Gets a response from the model based on user input and chat history"""
  chat_session = model.start_chat(history=chat_history.copy())
  response = chat_session.send_message(user_input)
  chat_history.append({"role": "user", "parts": [user_input]})
  chat_history.append({"role": "model", "parts": [response.text]})
  return response.text

# Display chat history (still not functioning properly only shows 1 promt and 1 response at a time)
for message in st.session_state.chat_session.history:
  with st.chat_message(translate_role_for_streamlit(message.role)):
    st.markdown(message.parts[0].text)

# Streamlit interface title and description
st.title("🌇 Ask Dagoy about Iloilo City!")
st.text("Dagoy is a Gemini Powered AI assistant that will \ncater any questions you have about Iloilo City. \nCreated By: Ed Francis Kyle G. Arendain")

# User input field
user_input = st.chat_input("Ask Dagoy anything...")

# Process user input and generate response
if user_input:
  st.chat_message("user", avatar="👨").markdown(user_input)

  #Pulls response from def_getresponse function to allow responses to be based on previous user inputs
  response = get_response(user_input)
    
  # Display the response
  with st.chat_message("assistant", avatar="👹"):
    st.markdown(f"{response}")
