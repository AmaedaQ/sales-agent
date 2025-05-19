import threading
import time
from agent import ask_questions, send_message, save_lead_data
from trigger_simulator import trigger_multiple_leads, lead_queue
from followup_manager import check_for_unresponsive_leads  # Import follow-up logic
from rich.console import Console
from rich.panel import Panel
import datetime

# Initialize the console for rich output
console = Console()

# Shared dictionary for lead interaction times and lock for thread-safe access
lead_interaction_times = {}
lead_interaction_lock = threading.Lock()

# Function to process leads from the queue
def lead_handler():
    """
    This function processes leads from the lead queue and interacts with them.
    It will fetch a lead, process it, and then update the console with status messages.
    The function keeps running until all leads are processed.
    """
    while not (lead_queue.empty() and all_leads_triggered.is_set()):  # Continue until all leads are processed
        if not lead_queue.empty():
            # Retrieve the next lead from the queue
            lead_id, lead_name = lead_queue.get()

            # Print a message indicating the lead is being processed
            console.print(Panel(f"[cyan]Processing Lead:[/] [bold]{lead_id} - {lead_name}[/]", title="Processing", border_style="blue"))

            # Process the lead by asking relevant questions (e.g., customer queries)
            ask_questions(lead_id, lead_name, lead_interaction_times, lead_interaction_lock)

            # Print a completion message once the lead is processed
            console.print(Panel(f"[green]Completed Lead:[/] [bold]{lead_id} - {lead_name}[/]", title="Lead Completed", border_style="green"))

            # Show remaining leads in the queue
            remaining = lead_queue.qsize()
            console.print(f"[yellow]Leads left in queue: {remaining}[/]\n")

            # Mark the lead task as done
            lead_queue.task_done()
        else:
            # If the queue is empty, wait and print a message
            console.print("[bold yellow]Waiting for new leads to process...[/]", style="dim")
            time.sleep(5)  # Sleep for 5 seconds before checking the queue again

# Main execution block
if __name__ == "__main__":
    # Display a welcome message in the console
    console.print(Panel("Welcome to the Lead Interaction System", title="Sales Agent", style="bold green"))

    # Create an event to track when all leads have been triggered
    all_leads_triggered = threading.Event()

    # Start the lead handler thread to process the leads
    handler_thread = threading.Thread(target=lead_handler)
    handler_thread.start()

    # Start the follow-up thread to check for unresponsive leads
    follow_up_thread = threading.Thread(target=check_for_unresponsive_leads, daemon=True, args=(lead_interaction_times, lead_interaction_lock))
    follow_up_thread.start()

    # Trigger multiple leads for processing
    num_leads = 5  # Number of leads to trigger
    console.print(f"[bold cyan]Triggering {num_leads} leads...[/]")  # Notify the user of lead triggering
    trigger_multiple_leads(num_leads)  # Simulate triggering the leads
    all_leads_triggered.set()  # Mark that no more leads will be triggered

    # Wait for the lead handler thread to finish processing all leads
    handler_thread.join()

    # Display a success message once all leads have been processed
    console.print(Panel("[bold green]✅ All leads handled successfully![/]", style="bold blue"))
