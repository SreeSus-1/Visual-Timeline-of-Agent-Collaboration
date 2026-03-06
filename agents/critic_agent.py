import ollama
import time

def run_critic_agent(text):

    prompt = f"Critically evaluate this research and mention weaknesses:\n{text}"

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "agent": "Critic Agent",
        "topic": "evaluation",
        "output": response["message"]["content"],
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }