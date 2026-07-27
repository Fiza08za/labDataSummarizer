import streamlit as st
from google import genai
import os

# Page Configuration
st.set_page_config(page_title="LabData Summarizer", page_icon="🧬", layout="wide")

st.title("🧬 LabData Summarizer")
st.subheader("Transform raw bioinformatics & lab outputs into publication-ready captions and reports.")

# Sidebar for API key input
st.sidebar.header("Settings")
user_api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
api_key = user_api_key or os.environ.get("GEMINI_API_KEY")

# Input selection
data_type = st.selectbox(
    "Select your data type:",
    ["Sample-to-Sample Heatmap", "PCA Plot Results", "Volcano Plot / Differential Expression", "General Lab Data Summary"]
)

raw_data = st.text_area(
    "Paste your raw statistical output, top genes, or data description here:",
    height=200,
    placeholder="e.g., Top DEGs: GAPDH (log2FC=2.5, p=0.001), BRCA1 (log2FC=-3.1, p=0.0001)... or describe your plot clusters."
)

# System Prompt definition
SYSTEM_PROMPT = """
You are an expert bioinformatics assistant and scientific writer.
Your task is to take raw experimental analysis outputs (e.g., PCA data, DESeq2 results, volcano plots, sample heatmaps) and generate structured, publication-grade report text.

Always format your response using these exact markdown headers:
1. ### 📝 Figure Caption
Provide a formal, publication-ready figure legend suitable for a journal paper.

2. ### 🔍 Key Observations
List 3-4 bullet points summarizing the biological or technical takeaways.

3. ### 📄 Draft Results Paragraph
Write a cohesive, academic results paragraph for a thesis or report.
"""

if st.button("Generate Summary & Captions", type="primary"):
    if not api_key:
        st.error("Please provide a valid Gemini API Key in the sidebar.")
    elif not raw_data.strip():
        st.warning("Please paste some data or descriptions to analyze.")
    else:
        with st.spinner("Analyzing laboratory data..."):
            try:
                # Initialize Google GenAI client
                client = genai.Client(api_key=api_key)
                
                full_user_input = f"Data Type: {data_type}\n\nRaw Data/Description:\n{raw_data}"
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=full_user_input,
                    config={'system_instruction': SYSTEM_PROMPT}
                )
                
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Error generating summary: {str(e)}")