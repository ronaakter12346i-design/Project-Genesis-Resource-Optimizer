# safety_shield.py

def verify_action(action, metrics):
  
    if metrics['mem'] > 85 and action == "THROTTLE_PROCESS":
        return "BLOCK", "Memory is too high, cannot throttle further."
    
    return "EXECUTE", "Action is safe."