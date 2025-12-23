import streamlit as st
from src.pdf_loader import extract_text_from_pdf
from src.summarizer import summarize_text
from src.explainer import explain_text

st.set_page_config(page_title="AI Research Paper Summarizer", layout="wide")

st.title(" AI Research Paper Summarizer & Explainer")
st.write("Upload a research paper PDF to get structured summaries and simple explanations.")

uploaded_file = st.file_uploader("Upload Research Paper (PDF)", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        paper_text = extract_text_from_pdf(uploaded_file)

    st.success("Text extracted successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Abstract Summary")
        if st.button("Generate Abstract Summary"):
            abstract_summary = summarize_text(paper_text)
            st.write(abstract_summary)

    with col2:
        st.subheader("Methodology Summary")
        if st.button("Generate Methodology Summary"):
            method_summary = summarize_text(paper_text)
            st.write(method_summary)

    st.subheader("Results Summary")
    if st.button("Generate Results Summary"):
        results_summary = summarize_text(paper_text)
        st.write(results_summary)

    st.subheader("Future Scope")
    if st.button("Generate Future Scope"):
        future_scope = summarize_text(paper_text)
        st.write(future_scope)

    st.subheader("Explain Complex Content")
    user_text = st.text_area("Paste a technical paragraph here")
    if st.button("Explain in Simple Words"):
        explanation = explain_text(user_text)
        st.write(explanation)


# To run the app, use the command: streamlit run app.py