import streamlit as st
import google.generativeai as genai
import os

# Page setup
st.set_page_config(page_title="LabData Summarizer", page_icon="🧬", layout="wide")

st.title("🧬 LabData Summarizer")
st.write("Transform raw bioinformatics & lab outputs into publication-ready captions and reports.")

# Sidebar for API key input
st.sidebar.header("Settings")
user_api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

# Determine active API key
api_key = user_api_key if user_api_key.strip() else os.environ.get("GEMINI_API_KEY")

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
                # Configure API key
                genai.configure(api_key=api_key)
                
                # Initialize standard model with System Instructions
                model = genai.GenerativeModel(
                    model_name='gemini-1.5-flash',
                    system_instruction=SYSTEM_PROMPT
                )
                
                full_input = f"Data Type: {data_type}\n\nRaw Data:\n{raw_data}"
                
                # Generate content
                response = model.generate_content(full_input)
                
                st.markdown("---")
                if response.text:
                    st.markdown(response.text)
                else:
                    st.error("The API returned an empty response.")
                
            except Exception as e:
                st.error(f"❌ API Error: {str(e)}")
