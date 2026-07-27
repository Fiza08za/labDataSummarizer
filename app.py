import streamlit as st
from google import genai
from google.genai import types
import os

st.set_page_config(
    page_title="LabData Summarizer",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 LabData Summarizer")
st.write(
    "Transform raw bioinformatics & lab outputs "
    "into publication-ready captions and reports."
)

# Sidebar setup
st.sidebar.header("Settings")

user_api_key = st.sidebar.text_input(
    "Enter Gemini API Key",
    type="password"
)

# Fetch API key
api_key = (
    user_api_key.strip()
    if user_api_key.strip()
    else os.environ.get("GEMINI_API_KEY")
)

# Select data type
data_type = st.selectbox(
    "Select your data type:",
    [
        "Sample-to-Sample Heatmap",
        "PCA Plot Results",
        "Volcano Plot / Differential Expression",
        "General Lab Data Summary"
    ]
)

# Input data
raw_data = st.text_area(
    "Paste your raw statistical output, top genes, or data description here:",
    height=200,
    placeholder=(
        "Example: W_1, W_2, and W_3 form a tight cluster "
        "with low distance values (0-15)..."
    )
)

# System prompt
SYSTEM_PROMPT = """
You are an expert bioinformatics assistant and scientific writer.

Your task is to take raw experimental analysis outputs and generate
structured, publication-grade scientific report text.

Important rules:
- Do not invent numerical values.
- Do not invent genes, pathways, statistical results, or biological conclusions.
- Use only information provided by the user.
- Clearly distinguish observations from interpretations.
- Use precise scientific language.

Always format your response using exactly these sections:

### 📝 Figure Caption

Write a formal scientific figure caption.

### 🔍 Key Observations

Provide 3 to 5 concise observations based on the supplied data.

### 📄 Draft Results Paragraph

Write a formal academic paragraph suitable for a thesis or scientific report.

### ⚠️ Limitations

Mention what cannot be concluded from the supplied information.
"""

# Generate result
if st.button("Generate Summary & Captions", type="primary"):

    if not api_key:
        st.error(
            "❌ No API Key found! Please paste your key "
            "in the sidebar or configure it in Streamlit Secrets."
        )

    elif not raw_data.strip():
        st.warning(
            "⚠️ Please paste some data or descriptions first."
        )

    else:

        with st.spinner("Analyzing laboratory data..."):

            try:

                client = genai.Client(api_key=api_key)

                full_input = f"""
Data Type:
{data_type}

Raw Data:
{raw_data}
"""

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=full_input,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT
                    )
                )

                st.markdown("---")

                if response.text:
                    st.markdown(response.text)
                else:
                    st.error(
                        "The AI model returned an empty response."
                    )

            except Exception as e:

                st.error(
                    f"❌ API request failed: {type(e).__name__}"
                )

                st.code(
                    str(e),
                    language="text"
                )
