**LabData Summarizer**

An AI-powered bioinformatics assistant that transforms raw laboratory and computational analysis outputs into structured scientific summaries, figure captions, key observations, and academic results paragraphs.

**Live App:**  
https://labdatasummarizer-5osongvipecbremecngf69.streamlit.app/

**Project Overview**

**The Problem**
Bioinformatics students and researchers frequently generate analytical outputs such as PCA plots, sample-to-sample heatmaps, volcano plots, and differential expression results. However, converting these computational outputs into clear scientific explanations, publication-style figure captions, and formal results paragraphs can be time-consuming.

This problem is particularly relevant to students and early-career researchers who may have successfully completed their computational analysis but still need to interpret and communicate their results in a scientifically structured format.

**The Solution**
LabData Summarizer is an AI-powered web application designed to help bioinformatics students, laboratory researchers, and life-science researchers interpret and communicate their analysis outputs.

Users select the type of analysis they have performed and paste their raw results or a description of their figure. The application then uses an AI model to generate:
A scientific figure caption
Key observations from the provided data
A draft academic results paragraph
Limitations regarding conclusions that cannot be made from the available information

The application is designed to assist with scientific communication while ensuring that the AI does not invent unsupported numerical or biological results.

**Target Users**

LabData Summarizer is designed for:

Bioinformatics students
Life-science students
Molecular biology researchers
Laboratory researchers
Computational biology researchers
Researchers preparing thesis or report sections

**Features**
1. Analysis Type Selection
Users can select from four analysis categories:

Sample-to-Sample Heatmap
PCA Plot Results
Volcano Plot / Differential Expression
General Lab Data Summary

2. Scientific Figure Caption Generation
The application converts the supplied analysis information into a formal figure caption suitable for a scientific report or thesis.

3. Key Observation Extraction
The AI identifies the major observations from the provided data and presents them in a concise, structured format.

4. Academic Results Paragraph Generation
The application generates a formal draft results paragraph using the information supplied by the user.

5. Limitations Identification
The AI identifies information that is missing and explains which biological or statistical conclusions cannot be made from the provided data.

6. Scientific Hallucination Control
The AI instructions explicitly prohibit the invention of:
Gene names
Numerical values
Statistical results
p-values
Adjusted p-values
Fold changes
Biological pathways
Experimental conclusions
The application is instructed to use only the information supplied by the user.

7. Multiple Bioinformatics Analysis Types
The application supports common bioinformatics result types, including:
PCA interpretation
Heatmap interpretation
Differential expression analysis summaries
Volcano plot summaries
General RNA-seq analysis summaries

**AI Feature**
The central AI feature of LabData Summarizer is an automated scientific interpretation and writing assistant.
The user provides:

Analysis Type
+
Raw Analysis Data or Figure Description

The application sends this information to the AI model, which returns:

Figure Caption
+
Key Observations
+
Draft Results Paragraph
+
Limitations
AI System Instructions

The application uses the following system instructions:

You are an expert bioinformatics analyst and scientific writer.

Your task is to analyze user-provided bioinformatics and laboratory analysis outputs and generate structured scientific text.

The user may provide information about:
- PCA analysis
- Sample-to-sample heatmaps
- Volcano plots
- Differential gene expression
- General laboratory data
    
Always format the response using exactly these sections:

### Figure Caption
Write a formal, publication-quality figure caption based only on the supplied information.

### Key Observations
Provide 3 to 5 concise bullet points describing the main observations.

### Draft Results Paragraph
Write a formal academic results paragraph suitable for a thesis or scientific report.

### Limitations
Mention important conclusions that cannot be made because the necessary information was not provided.
This instruction set is designed to make the AI function as a structured scientific writing assistant rather than a general-purpose chatbot.

**Technologies and Tools**

**Frontend and Application Framework**
Python
Streamlit
Streamlit was used to create the interactive web application interface.

**AI Integration**
Google Gemini API
Google GenAI Python SDK
Gemini Flash model
The AI model processes the user's bioinformatics analysis information and generates structured scientific text.

**Version Control**
GitHub
The source code is maintained in a public GitHub repository.

**Deployment**
Streamlit Community Cloud
The application is deployed online and can be accessed through a public web URL.

**Programming Libraries**
The project uses:
streamlit
google-genai

**Application Workflow**
User selects analysis type
          ↓
User enters analysis results
          ↓
Application validates the input
          ↓
Data is sent to the AI model
          ↓
AI analyzes the supplied information
          ↓
Scientific output is generated
          ↓
Figure caption + observations
+ results paragraph + limitations
are displayed to the user

**Screenshots**
1. Application Interface
This screenshot shows the main application interface, including the application title, analysis type selection menu, input area, and generation button.

2. Analysis Input
This screenshot shows the user entering bioinformatics analysis results into the application.

3. AI-Generated Scientific Summary
This screenshot shows the AI-generated figure caption, key observations, draft results paragraph, and limitations.

**How to Run the Project Locally**
The easiest way to use LabData Summarizer is through its publicly deployed web application.

Open the live application URL:
[PASTE YOUR LIVE STREAMLIT APP URL HERE]

Select the type of analysis from the dropdown menu:
Sample-to-Sample Heatmap
PCA Plot Results
Volcano Plot / Differential Expression
General Lab Data Summary

Paste the relevant bioinformatics analysis results or figure description into the input box.

Click Generate Summary & Captions.

The application sends the input to the integrated AI model and displays:
A scientific figure caption
Key observations
A draft results paragraph
Limitations of the interpretation

No local installation or API key entry is required for users of the deployed application.


**Deployment**
The application is deployed using Streamlit Community Cloud.

The deployment process consists of:
Uploading the application source code to GitHub.
Connecting the GitHub repository to Streamlit Community Cloud.
Configuring the Gemini API key using secure deployment secrets.
Deploying the Streamlit application.
Making the application available through a public URL.

The API key is stored as a deployment secret and is not exposed to application users.

**Security**
The Gemini API key is not stored directly in the source code.
Instead, the application retrieves it from a secure environment variable or Streamlit secret:

api_key = st.secrets["GEMINI_API_KEY"]

This prevents the API key from being exposed in the public GitHub repository.

**Limitations**
LabData Summarizer is an AI-assisted scientific writing tool and does not replace biological or statistical expertise. The quality of the generated output depends on the quality and completeness of the information provided by the user.

The application cannot reliably determine:
Biological mechanisms not represented in the input
Pathways that were not provided
Statistical significance without statistical evidence
Gene-level interpretations without gene-level data
Experimental validity without appropriate experimental information

AI-generated text should therefore be reviewed by the user before being used in a thesis, scientific report, or publication.

**Future Improvements**
Potential future improvements include:
Direct CSV upload for differential expression results
Automatic parsing of DESeq2 output files
Direct visualization upload
Automatic extraction of gene names and fold changes
Integration with functional enrichment results
Export of generated reports as PDF or DOCX files
User authentication and saved analysis history
Support for additional bioinformatics analysis types

**Project Summary**
LabData Summarizer demonstrates the development of a complete AI-powered application from concept to deployment.
The project combines:

Python
+
Streamlit
+
Google Gemini AI
+
Scientific Prompt Engineering
+
GitHub
+
Cloud Deployment

The result is a functional application that addresses a real problem encountered by bioinformatics students and researchers, transforming computational analysis outputs into structured scientific communication. 
