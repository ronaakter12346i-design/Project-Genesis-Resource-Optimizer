# memory_buffer.py
import json

def save_experience(metrics, action, outcome):
    experience = {
        "metrics": metrics,
        "action": action,
        "outcome": outcome
    }
    
    with open("experience_log.json", "a") as f:
        f.write(json.dumps(experience) + "\n")