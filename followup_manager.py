import time
import datetime
from agent import send_message, save_lead_data  # Assuming these are imported correctly
from rich.console import Console
from rich.panel import Panel

# Initialize the console for rich text output
console = Console()

# Dictionary to store lead's last follow-up status and interaction times
follow_up_sent = {}

def check_for_unresponsive_leads(lead_interaction_times, lead_interaction_lock):
    """
    Continuously checks if leads have been unresponsive for a set period and sends follow-up messages.
    
    Parameters:
        lead_interaction_times (dict): Dictionary that tracks the last interaction time for each lead.
        lead_interaction_lock (threading.Lock): Lock for thread-safe access to shared data.
    """
    while True:
        current_time = datetime.datetime.now()  # Get the current time
        with lead_interaction_lock:  # Ensure thread-safe access to shared data
            for lead_id, last_interaction_time in lead_interaction_times.items():
                # Check if the lead hasn't been followed up already and has been inactive for 10 seconds (for testing)
                if lead_id not in follow_up_sent and (current_time - last_interaction_time).seconds >= 10:
                    # Send a follow-up message to the unresponsive lead
                    send_message(lead_id, "Just checking in to see if you're still interested. Let me know when you're ready to continue.", style="yellow", title="Follow-Up")

                    # Save lead data with "followed_up" status
                    save_lead_data(lead_id, None, None, None, None, "followed_up")

                    # Mark the lead as followed up and update the interaction time to the current time
                    follow_up_sent[lead_id] = current_time  # Mark follow-up as sent
                    lead_interaction_times[lead_id] = current_time  # Reset the lead's interaction time after the follow-up

                    # Provide visual feedback in the console that the follow-up was sent
                    console.print(Panel(f"Follow-up sent for Lead {lead_id}", title="Follow-Up Sent", style="bold yellow"))

        # Wait for 10 seconds before checking again for new unresponsive leads
        time.sleep(10)
