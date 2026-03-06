import ollama
import time

def run_summarizer_agent(text):

    prompt = f"Summarize this research:\n{text}"

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "agent": "Summarizer Agent",
        "topic": "summary",
        "output": response["message"]["content"],
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }