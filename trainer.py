# trainer.py
import json

def train_agent():
    try:
        with open("experience_log.json", "r") as f:
            logs = [json.loads(line) for line in f]
        
        print(f"Trainer: Analyzing {len(logs)} past experiences...")
        
      
        success_count = sum(1 for log in logs if log['outcome'] == "SUCCESS")
        print(f"Trainer: Learning complete. Success rate: {(success_count/len(logs))*100:.1f}%")
        
    except FileNotFoundError:
        print("Trainer: No experience data found yet.")

if __name__ == "__main__":
    train_agent()