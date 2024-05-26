import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Configure API key from environment variable
load_dotenv()

st.set_page_config(
    page_title="Chat with Dagoy!",
    page_icon=":city_sunrise:",  # Favicon emoji
    layout="centered",  # Page layout option
)

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Model configuration
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

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

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

# Create chat history
chat_history = [
  {
    "role": "model",
    "parts": [
      "Hello! Welcome to Iloilo City! My name is Dagoy and I'll be your friendly assistant during your stay here. Feel free to ask me anything about Iloilo City, and I'll be happy to help.\n\nMay I know your name? (This is optional. You can skip this if you don't want to provide your name.)",
    ],
  },
]

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

def get_response(user_input):
  """Gets a response from the model based on user input and chat history"""
  chat_session = model.start_chat(history=chat_history.copy())
  response = chat_session.send_message(user_input)
  chat_history.append({"role": "user", "parts": [user_input]})
  chat_history.append({"role": "model", "parts": [response.text]})
  return response.text

for message in st.session_state.chat_session.history:
  with st.chat_message(translate_role_for_streamlit(message.role)):
    st.markdown(message.parts[0].text)

st.title("🌇 Ask Dagoy about Iloilo City!")
st.text("Dagoy is a Gemini Powered AI assistant that will \ncater any questions you have about Iloilo City. \nCreated By: Ed Francis Kyle G. Arendain")

#st.subheader("Your friendly AI assistant for all things Iloilo")

user_input = st.chat_input("Ask Dagoy anything...")

if user_input:
  st.chat_message("user", avatar="👨").markdown(user_input)
  
  response = get_response(user_input)
  #st.write(f"**Dagoy:** {response}")

  with st.chat_message("assistant", avatar="👹"):
    st.markdown(f"{response}")
