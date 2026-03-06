import json
from agents.research_agent import run_research_agent
from agents.summarizer_agent import run_summarizer_agent
from agents.critic_agent import run_critic_agent

LOG_FILE = "logs/agent_logs.json"


def save_log(entry):

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)


def run_agents(topic):

    research = run_research_agent(topic)
    save_log(research)

    summary = run_summarizer_agent(research["output"])
    save_log(summary)

    critic = run_critic_agent(research["output"])
    save_log(critic)