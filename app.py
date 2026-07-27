import streamlit as st
from google import genai
from google.genai import types
import os

st.set_page_config(page_title="LabData Summarizer", page_icon="🧬", layout="wide")

st.title("🧬 LabData Summarizer")
st.write("Transform raw bioinformatics & lab outputs into publication-ready captions and reports.")

# Sidebar setup
st.sidebar.header("Settings")
user_api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# Fetch API key
api_key = user_api_key.strip() if user_api_key.strip() else os.environ.get("GEMINI_API_KEY")

data_type = st.selectbox(
    "Select your data type:",
    ["Sample-to-Sample Heatmap", "PCA Plot Results", "Volcano Plot / Differential Expression", "General Lab Data Summary"]
)

raw_data = st.text_area(
    "Paste your raw statistical output, top genes, or data description here:",
    height=200,
    placeholder="e.g., W_1, W_2, W_3 form a tight cluster with low distance values (0-15)..."
)

SYSTEM_PROMPT = """
You are an expert bioinformatics assistant and scientific writer.
Your task is to take raw experimental analysis outputs and generate structured, publication-grade report text.

Always format your response using these exact markdown headers:
1. ### 📝 Figure Caption
2. ### 🔍 Key Observations
3. ### 📄 Draft Results Paragraph
"""

if st.button("Generate Summary & Captions", type="primary"):
    if not api_key:
        st.error("❌ No API Key found! Please paste your key in the sidebar on the left.")
    elif not raw_data.strip():
        st.warning("⚠️ Please paste some data or descriptions first.")
    else:
        with st.spinner("Analyzing laboratory data..."):
            try:
                # Initialize GenAI Client
                client = genai.Client(api_key=api_key)
                
                # Automatically find available model supporting text generation
                available_models = [
                    m.name for m in client.models.list() 
                    if hasattr(m, 'supported_actions') and "generateContent" in m.supported_actions
                ]
                
                # Pick best available model on the account
                chosen_model = None
                for preferred in ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]:
                    for m in available_models:
                        if preferred in m:
                            chosen_model = m
                            break
                    if chosen_model:
                        break
                        
                if not chosen_model and available_models:
                    chosen_model = available_models[0]
                elif not chosen_model:
                    chosen_model = "gemini-2.0-flash"
                
                full_input = f"Data Type: {data_type}\n\nRaw Data:\n{raw_data}"
                
                # Call generateContent
                response = client.models.generate_content(
                    model=chosen_model,
                    contents=full_input,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT
                    )
                )
                
                st.markdown("---")
                if response.text:
                    st.markdown(response.text)
                else:
                    st.error("The API returned an empty response.")
                
            except Exception as e:
                st.error(f"❌ API Error: {str(e)}")
