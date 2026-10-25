# genesis_core.py (Final Master Script with Trend Analysis)
import time
import random
import json
import safety_shield
import memory_buffer
from datetime import datetime

def get_system_metrics():
    return {"cpu": random.randint(10, 95), "mem": random.randint(20, 90)}

def analyze_trend():
    try:
        with open("experience_log.json", "r") as f:
            logs = [json.loads(line) for line in f]
        
        # Trend: CPU 70% er upor thakle kon action successful chilo
        recent_logs = logs[-20:] # Shesh 20ti experience analyze korbe
        throttle_success = sum(1 for log in recent_logs if log['action'] == "THROTTLE_PROCESS" and log['outcome'] == "SUCCESS")
        optimize_success = sum(1 for log in recent_logs if log['action'] == "OPTIMIZE_CACHE" and log['outcome'] == "SUCCESS")
        
        return "THROTTLE_PROCESS" if throttle_success >= optimize_success else "OPTIMIZE_CACHE"
    except:
        return "OPTIMIZE_CACHE"

def get_intelligent_decision(metrics):
    # Exploration (20%) vs Exploitation (80% trend-based)
    if random.random() < 0.2:
        return random.choice(["THROTTLE_PROCESS", "OPTIMIZE_CACHE"])
    
    return analyze_trend()

def run_genesis_core():
    print("Project Genesis: Predictive Autonomous Mode Active...")
    try:
        while True:
            metrics = get_system_metrics()
            action = get_intelligent_decision(metrics)
            
            decision, reason = safety_shield.verify_action(action, metrics)
            
            # Timestamp add kora jate trend bujha jay
            log_entry = {"time": str(datetime.now().strftime("%H:%M")), "metrics": metrics, "action": action, "outcome": "SUCCESS" if decision == "EXECUTE" else "BLOCKED"}
            
            if decision == "EXECUTE":
                print(f"[{log_entry['time']}] CPU {metrics['cpu']}% | Decision: {action}")
                memory_buffer.save_experience(metrics, action, "SUCCESS")
            else:
                print(f"[{log_entry['time']}] !! BLOCKED !! ({reason})")
                memory_buffer.save_experience(metrics, action, "BLOCKED")
            
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nProject Genesis: Stopping safely.")

if __name__ == "__main__":
    run_genesis_core()