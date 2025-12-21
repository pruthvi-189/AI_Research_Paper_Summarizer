from transformers import pipeline

# Load model once
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_text(text, max_len=150):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = ""

    for chunk in chunks[:3]:  # limit for speed
        result = summarizer(chunk, max_length=max_len, min_length=50, do_sample=False)
        summary += result[0]['summary_text'] + " "

    return summary
