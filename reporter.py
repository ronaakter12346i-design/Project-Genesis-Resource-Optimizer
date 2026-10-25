# reporter.py
import json

def generate_report():
    try:
        with open("experience_log.json", "r") as f:
            logs = [json.loads(line) for line in f]
        
        total = len(logs)
        success = sum(1 for log in logs if log['outcome'] == "SUCCESS")
        blocked = sum(1 for log in logs if log['outcome'] == "BLOCKED")
        
        print("\n--- Project Genesis: Performance Report ---")
        print(f"Total Decisions Made: {total}")
        print(f"Successful Actions: {success}")
        print(f"Safety Blocks: {blocked}")
        
        if total > 0:
            rate = (success / total) * 100
            print(f"Agent Efficiency: {rate:.2f}%")
        
        if rate > 80:
            print("Status: Agent is highly optimized.")
        else:
            print("Status: Agent needs more training.")
        print("-------------------------------------------\n")
            
    except FileNotFoundError:
        print("Reporter: No logs found. Run the core first.")

if __name__ == "__main__":
    generate_report()