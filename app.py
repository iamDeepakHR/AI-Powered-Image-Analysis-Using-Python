from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GENAI_API_KEY")  # Ensure GENAI_API_KEY is set in .env
if not api_key:
    st.error("API key not found. Please set the GENAI_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=api_key)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get Gemini response for image analysis
def get_gemini_response(input_text, image):
    try:
        # Convert PIL image to bytes
        img_bytes = image.convert("RGB")
        
        # Generate content using Gemini
        response = model.generate_content([input_text, img_bytes])
        
        if response and response.candidates:
            parts = response.candidates[0].content.parts
            return ' '.join(part.text for part in parts)
        else:
            return "No meaningful response generated."
    except Exception as e:
        return f"Error: {e}"

import streamlit as st
from PIL import Image

# Page configuration must come first
st.set_page_config(page_title="NexLens Image Analysis", layout="wide")

# Page header with centered title
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color:#4F8BF9;'>🔍 NexLens</h1>
        <p style='font-size:18px;'>Ask me anything!</p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f0f2f6;
            color: #000;
            text-align: center;
            padding: 12px 10px;
            font-size: 14px;
            z-index: 9999;
        }
        /* Push page content up above footer */
        .block-container {
            padding-bottom: 70px !important;
        }
    </style>
    <div class="footer">
        NexLens Image Analysis by <b>Deepak Gowda H R</b>, Mandya Technologies Ltd, Mandya, Karnataka, India • Copyright © 2025
    </div>
""", unsafe_allow_html=True)
# Input section
st.header("🧠 NexLens Computer Vision Application")

input_prompt = st.text_input("📝 Input Prompt:", key="input", placeholder="Describe what you want to know about the image.")
uploaded_file = st.file_uploader("📁 Upload an Image:", type=["jpg", "jpeg", "png"])

# Optional: Display uploaded image in small size
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=300)


    # Button to analyze the image
    if st.button("Analyze Image"):
        with st.spinner("Analyzing the image..."):
            response = get_gemini_response(input_prompt, image)
        
        # Display the response
        st.subheader("Analysis Result:")
        st.write(response)
