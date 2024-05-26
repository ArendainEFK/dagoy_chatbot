# 🌇 [Chat with Dagoy - Iloilo City Assistant](https://dagoychatbot-arendain.streamlit.app) 🌇
⬆️⬆️⬆️⬆️⬆️⬆️ Click to start chatting with Dagoy! ⬆️⬆️⬆️⬆️⬆️⬆️

## 👀 Overview:
This project creates a web application using Streamlit, integrated with the Google GenerativeAI API, to facilitate a chat-based interaction with an AI assistant named Dagoy. The assistant is designed to provide information and assistance related to Iloilo City, Philippines. Currently the model's knowledge base composes of 3,781 tokens. Said token are the interaction between the user and Gemini's respones which are fitted in order for the model to serve its purpose.

## ⚙️ Components:

1. **Streamlit:** Streamlit is a Python library used for building interactive web applications for data science and machine learning projects. In this project, Streamlit is utilized to create a user-friendly interface where users can interact with the AI assistant.

2. **Google GenerativeAI API:** The Google GenerativeAI API is accessed through the `google.generativeai` module. It provides access to state-of-the-art language models that can generate human-like text based on the input provided by users. In this project, the GenerativeAI API is used to power the AI assistant, Dagoy, enabling it to respond to user queries and provide information about Iloilo City.

3. **dotenv:** The `dotenv` library is used to load environment variables from a `.env` file. This is utilized to securely configure the API key required for accessing the Google GenerativeAI API.

## ❓ How It Works:

1. **Initialization:**
   - The necessary libraries (`streamlit`, `google.generativeai`, `dotenv`, `os`) are imported.
   - Streamlit page configuration is set, including the page title, icon, and layout.
   - The Google GenerativeAI API key is loaded from the environment variable using `dotenv`.

2. **Model Configuration:**
   - The parameters for model generation are configured, including temperature, top-p, top-k, maximum output tokens, and response MIME type.
   - Safety settings are defined to filter out harmful content such as harassment, hate speech, sexually explicit content, and dangerous content.
   - The model uses Google's Gemini 1.0 Pro API which is limited to 30,000 tokens. This model was specifically chosen as it performs well with small scale chatbot applications.

3. **Chat History:**
   - A chat history is initialized with an introductory message from the AI assistant, Dagoy. (NOTE Still Buggy)
   - The chat history is stored in `chat_history.py` within the repository. These are the prompts used to train the model as well within Google's Makersuite/AI Studio.

4. **User Interface:**
   - The Streamlit UI is created, consisting of a title, a brief description of Dagoy, and a chat input box where users can interact with the assistant.
   - When the user inputs a message, it is displayed in the chat interface, and the assistant's response is generated using the `get_response` function.

5. **Response Generation:**
   - The `get_response` function sends the user's input to the GenerativeAI model, which generates a response based on the input and chat history.
   - The response is appended to the chat history, and then displayed in the Streamlit interface.
   - Hence the `get_response` is what allows my model to have multi-level prompting.

## 🐍 Why Python and Streamlit:
- **Python:** Python is chosen for its simplicity, readability, and extensive ecosystem of libraries and frameworks. It provides powerful tools for web development, data science, and machine learning, making it well-suited for this project.
- **Streamlit:** Streamlit is selected for its ease of use and rapid prototyping capabilities. It allows developers to create interactive web applications with minimal effort, making it an ideal choice for building the UI for the AI assistant.

## 🐛 Known Bugs:
- **Chat History:** As of the moment even though my chatbot supports multilevel programing the chat history function which is resposible for showing all the user promts as well as responses still does not work. Hence everytime that the user prompts the session state resets even if the response still fetches data from past responses.


## 🎉 The Conclusion:
This project demonstrates how to leverage Python, Streamlit, and the Google GenerativeAI API to create a chat-based AI assistant for providing information and assistance about Iloilo City. With its intuitive interface and powerful backend, users can engage in natural language conversations with the assistant, enhancing their experience and knowledge about the city. This final task for our CCS 229 subject also shows how easy it is to create a custom chatbot with a custom knowledge base especially in today's generation.



