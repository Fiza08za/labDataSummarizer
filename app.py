import streamlit as st
from google import genai
from google.genai import types
import os

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="LabData Summarizer",
    page_icon="🧬",
    layout="wide"
)

# --------------------------------------------------
# APPLICATION TITLE
# --------------------------------------------------

st.title("🧬 LabData Summarizer")

st.write(
    "Transform bioinformatics and laboratory analysis outputs "
    "into structured scientific summaries, figure captions, "
    "and results paragraphs."
)

# --------------------------------------------------
# PRIVATE API KEY
# --------------------------------------------------

# The API key is stored privately in Streamlit Cloud Secrets.
# Users do not need to enter an API key.

try:
    api_key = st.secrets["GEMINI_API_KEY"]

except Exception:

    api_key = os.environ.get("GEMINI_API_KEY")


# --------------------------------------------------
# ANALYSIS TYPE
# --------------------------------------------------

data_type = st.selectbox(
    "Select your data type:",
    [
        "Sample-to-Sample Heatmap",
        "PCA Plot Results",
        "Volcano Plot / Differential Expression",
        "General Lab Data Summary"
    ]
)


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

raw_data = st.text_area(
    "Paste your analysis results or describe your figure:",
    height=250,

    placeholder=(
        "Example:\n\n"
        "Differential expression analysis identified 120 significantly "
        "upregulated genes and 95 significantly downregulated genes in "
        "biofilm samples compared with planktonic samples. The significance "
        "threshold was adjusted p-value < 0.05 and absolute log2FC > 1."
    )
)


# --------------------------------------------------
# AI SYSTEM INSTRUCTIONS
# --------------------------------------------------

SYSTEM_PROMPT = """
You are an expert bioinformatics analyst and scientific writer.

Your task is to analyze user-provided bioinformatics and laboratory
analysis outputs and generate structured scientific text.

The user may provide information about:

- PCA analysis
- Sample-to-sample heatmaps
- Volcano plots
- Differential gene expression
- General laboratory data

IMPORTANT RULES:

1. Use only information explicitly provided by the user.

2. Do not invent:
   - genes
   - gene names
   - pathways
   - biological processes
   - numerical values
   - p-values
   - adjusted p-values
   - fold changes
   - experimental results

3. Do not claim statistical significance unless the user provides
   statistical evidence.

4. Clearly distinguish direct observations from biological interpretation.

5. If important information is missing, mention it in the Limitations section.

6. Use formal scientific language suitable for a thesis or research report.

7. Use plain-text scientific notation.

8. Write log2FC instead of LaTeX mathematical notation such as
   log_2(FC).

9. Write adjusted p-value instead of complicated mathematical formatting.

10. Do not use LaTeX notation.

Always format the response using exactly these sections:

### 📝 Figure Caption

Write a formal, publication-quality figure caption based only
on the supplied information.

### 🔍 Key Observations

Provide 3 to 5 concise bullet points describing the main observations.

### 📄 Draft Results Paragraph

Write a formal academic results paragraph suitable for a thesis
or scientific report.

### ⚠️ Limitations

Mention important conclusions that cannot be made because the
necessary information was not provided.
"""


# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------

if st.button(
    "Generate Summary & Captions",
    type="primary"
):

    # Check whether API key exists
    if not api_key:

        st.error(
            "The application is currently unavailable because the "
            "AI service has not been configured."
        )

        st.stop()


    # Check whether user provided data
    if not raw_data.strip():

        st.warning(
            "Please paste your analysis results or describe your figure "
            "before generating a summary."
        )

        st.stop()


    # AI generation
    with st.spinner(
        "Analyzing your laboratory data..."
    ):

        try:

            # Create Gemini client
            client = genai.Client(
                api_key=api_key
            )


            # Combine analysis type and user input
            full_input = f"""
Analysis Type:
{data_type}

User-Provided Analysis Information:
{raw_data}
"""


            # Generate response
            response = client.models.generate_content(

                model="gemini-3.6-flash",

                contents=full_input,

                config=types.GenerateContentConfig(

                    system_instruction=SYSTEM_PROMPT,

                    temperature=0.3
                )
            )


            # Display result
            if response.text:

                st.success(
                    "Scientific summary generated successfully."
                )

                st.markdown("---")

                st.markdown(
                    response.text
                )


            else:

                st.error(
                    "The AI model returned an empty response. "
                    "Please try again with more detailed analysis information."
                )


        except Exception as e:

            st.error(
                "The AI service could not process your request."
            )

            st.code(
                f"{type(e).__name__}: {str(e)}",
                language="text"
            )
