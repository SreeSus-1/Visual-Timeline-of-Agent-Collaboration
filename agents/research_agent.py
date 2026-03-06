import ollama
import time

def run_research_agent(topic):

    prompt = f"Provide research insights about {topic}"

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "agent": "Research Agent",
        "topic": topic,
        "output": response["message"]["content"],
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }