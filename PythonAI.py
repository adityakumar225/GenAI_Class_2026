import streamlit as st
from google import genai

# Set the browser tab title and icon
st.set_page_config(page_title="Python AI Assistant", page_icon="🐍")

# Display the header and subheader using HTML
st.markdown("""
  <div style='text-align: center; padding: 20px; background: linear-gradient(135deg, #1a1a2e, #16213e); border-radius: 15px;'>
    <h1 style='color: #00d4ff; font-size: 48px; margin-bottom: 5px;'>🐍 Python AI Assistant</h1>
    <p style='color: #aaaaaa; font-size: 18px;'>Use for only Python related questions!</p>
  </div>
  <br>
""", unsafe_allow_html=True)

# Create the Gemini AI client using your API key
robo = genai.Client(api_key=st.secrets["API_KEY"])

# Start a new chat session with the Gemini model
mychat = robo.chats.create(model="gemini-flash-lite-latest")

# Empty placeholder where the response will appear
response_placeholder = st.empty()

# Text input box for the user to type their question
question = st.text_input("", placeholder="Enter your Python question here...")

# Create 3 columns to center the Send button
col1, col2, col3 = st.columns([4, 1, 4])
with col2:
    send = st.button("Send")

# When Send is clicked, send the question and display the response
if send:
    with st.spinner("Thinking..."):
        response = mychat.send_message(question)
    response_placeholder.success(response.text)
