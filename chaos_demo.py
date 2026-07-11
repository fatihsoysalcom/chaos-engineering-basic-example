import random
import time

def simulate_user_action(action_name):
    """Simulates a user performing an action. 
    Introduces a chance of failure to mimic real-world unpredictability."""
    print(f"User attempting action: {action_name}...")
    # Simulate network latency or other transient issues
    time.sleep(random.uniform(0.1, 0.5))

    # Introduce a random failure probability (e.g., 20% chance of failure)
    if random.random() < 0.2:
        print(f"!!! Action '{action_name}' FAILED due to unexpected error! !!!")
        return False
    else:
        print(f"Action '{action_name}' SUCCEEDED.")
        return True

def process_request(request_id):
    """Simulates processing a request, which involves multiple user actions."""
    print(f"\nProcessing request ID: {request_id}")
    
    # Simulate a sequence of operations that could fail independently
    success = True
    if not simulate_user_action("fetch_data"):
        success = False
    if success and not simulate_user_action("validate_data"):
        success = False
    if success and not simulate_user_action("save_data"):
        success = False

    if success:
        print(f"Request {request_id} processed successfully.")
    else:
        print(f"Request {request_id} failed during processing.")

if __name__ == "__main__":
    print("--- Starting Chaos Engineering Demo ---")
    print("This simulation demonstrates how unexpected failures can occur in complex systems.")
    print("Even simple actions have a chance of failure, mimicking real-world unpredictability.")

    # Simulate a few requests to observe failure patterns
    for i in range(5):
        process_request(i + 1)
        time.sleep(1) # Pause between requests

    print("\n--- Demo Finished ---")
