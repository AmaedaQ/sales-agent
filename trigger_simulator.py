import time
import random
import threading
import queue  # Importing queue for thread-safe lead storage
from agent import ask_questions  # Import the agent's ask_questions function

# Create a shared queue for leads to be processed by multiple threads
lead_queue = queue.Queue()

def simulate_lead_submission():
    """
    Simulates the submission of a lead with a random ID and name.
    This function mimics a delay before placing the lead into the queue for further processing.
    """
    # Generate a random lead ID and create a name for the lead
    lead_id = random.randint(1000, 9999)  # Random lead ID between 1000 and 9999
    lead_name = f"Lead_{lead_id}"  # Lead name using the generated ID
    
    # Log the new lead trigger
    print(f"New lead triggered: {lead_id}, {lead_name}")
    
    # Simulate a delay (e.g., network request or form submission time)
    time.sleep(2)
    
    # Place the new lead into the shared lead queue for processing
    lead_queue.put((lead_id, lead_name))  # Adds the lead as a tuple (ID, Name)

def trigger_multiple_leads(num_leads):
    """
    Trigger multiple leads by simulating lead submissions in parallel using threads.
    This function will create a number of threads that each simulate a lead submission.
    
    :param num_leads: Number of leads to trigger
    """
    # Create a list to hold all thread references
    threads = []
    
    # Start a new thread for each lead submission
    for _ in range(num_leads):
        thread = threading.Thread(target=simulate_lead_submission)  # Create a new thread for each lead
        threads.append(thread)
        thread.start()  # Start the thread to simulate lead submission
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()  # Ensure each thread has finished before proceeding
