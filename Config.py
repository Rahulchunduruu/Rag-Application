import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

class config:
    #If you prefer to run this in the terminal, make sure the first line is active and the second is commented out
    #GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not found in .env file. Please add your API key.")