from transformers import pipeline

explainer = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def explain_text(text):
    prompt = f"Explain the following technical content in simple words:\n{text}"
    result = explainer(prompt, max_length=200)
    return result[0]['generated_text']
