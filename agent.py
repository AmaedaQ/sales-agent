import time
import csv
import os
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.prompt import Prompt
import threading
import datetime  # Import datetime for timestamps

# Initialize console for rich formatting in terminal output
console = Console()

# Create a lock object for thread-safe input handling
input_lock = threading.Lock()

# Function to send styled messages to the lead
def send_message(lead_id, message, delay=0.5, style="bold yellow", title="Agent"):
    """
    Sends a message to the lead in a rich formatted panel.
    
    Parameters:
        lead_id (int): Unique identifier for the lead.
        message (str): Message to be displayed.
        delay (float): Time delay before the next operation.
        style (str): Style for the message text.
        title (str): Title for the panel.
    """
    message = Text(message, style=style)
    # Display the message in a panel with the lead_id as the subtitle
    console.print(Panel(message, title=title, subtitle=f"Lead {lead_id}", style="bold magenta", border_style="blue", padding=(1, 2)))
    time.sleep(delay)

# Function to ask questions to the lead and process their responses
def ask_questions(lead_id, lead_name, lead_interaction_times, lead_interaction_lock):
    """
    Asks the lead for information and processes their responses.
    
    Parameters:
        lead_id (int): Unique identifier for the lead.
        lead_name (str): Name of the lead.
        lead_interaction_times (dict): Dictionary to track lead interaction times.
        lead_interaction_lock (threading.Lock): Lock to ensure thread safety during interaction.
    """
    # Welcome message
    welcome_message = f"Hey {lead_name}, thank you for filling out the form. I'd like to gather some information from you. Is that okay?"
    send_message(lead_id, welcome_message, style="bold purple", title="Welcome")

    # Ask for lead's consent
    consent = get_input(lead_id, "[bold yellow]Lead Response (Yes/No):[/bold yellow]", choices=["yes", "no"])

    if consent == 'yes':
        send_message(lead_id, "Great! Let's get started.", style="bold green", title="Proceeding")

        # Ask for the lead's details
        age = get_input(lead_id, "What's your age?", default="25")
        while not age.isdigit():
            send_message(lead_id, "Please enter a valid number for your age.", style="bold red", title="Error")
            age = get_input(lead_id, "What's your age?")

        country = get_input(lead_id, "Which country are you from?")
        interest = get_input(lead_id, "What product or service are you interested in?")

        # Save the collected lead data to a CSV file
        save_lead_data(lead_id, lead_name, age, country, interest)
        send_message(lead_id, "Thank you for providing the information. Your status is now secured!", style="bold green", title="Success")

    else:
        send_message(lead_id, "Alright, no problem. Have a great day!", style="bold red", title="Declined")
        save_lead_data(lead_id, lead_name, None, None, None, "no_response")

    # Record the interaction time with thread safety
    with lead_interaction_lock:
        lead_interaction_times[lead_id] = datetime.datetime.now()

# Function to handle user input with enhanced visual formatting
def get_input(lead_id, message, choices=None, default=None):
    """
    Handles user input with rich text styling.
    
    Parameters:
        lead_id (int): Unique identifier for the lead.
        message (str): Message prompting for input.
        choices (list): List of valid choices for the input.
        default (str): Default value if no input is provided.

    Returns:
        str: User's input response.
    """
    with input_lock:  # Ensure thread safety during input collection
        # If choices are provided, present a multiple-choice prompt
        if choices:
            prompt_message = Text(message, style="bold cyan")  # Style the message
            return Prompt.ask(prompt_message, choices=choices)
        else:
            prompt_message = Text(message, style="bold cyan")  # Style the message
            return Prompt.ask(prompt_message, default=default)  # Default input handling

# Function to save lead data into a CSV file
def save_lead_data(lead_id, lead_name, age=None, country=None, interest=None, status="secured"):
    """
    Saves the lead data into a CSV file.

    Parameters:
        lead_id (int): Unique identifier for the lead.
        lead_name (str): Name of the lead.
        age (str): Age of the lead.
        country (str): Country of the lead.
        interest (str): Product/service the lead is interested in.
        status (str): Current status of the lead (default: "secured").
    """
    file_exists = os.path.exists("leads.csv")
    with open("leads.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            # Write header if the file is new
            writer.writerow(["lead_id", "name", "age", "country", "interest", "status"])
        # Write the lead's data to the CSV
        writer.writerow([lead_id, lead_name, age, country, interest, status])

# Helper function to print a simple divider for console output formatting
def print_divider():
    console.print("-" * 60, style="dim")

# Function to print a styled header in the console
def print_header(message, style="bold green"):
    console.print(Panel(message, style=style, title="System Status", border_style="cyan", padding=(0, 1)))

# Main entry point for the script
if __name__ == "__main__":
    # Display the header message
    print_header("Welcome to the Lead Interaction System!", style="bold cyan")

    # Initialize lead interaction tracking (dictionary and lock for thread safety)
    lead_interaction_times = {}
    lead_interaction_lock = threading.Lock()

    # Simulate handling a lead (this could be extended further)
    lead_id = 1234  # Sample lead ID
    lead_name = "Sample Lead"  # Sample lead name

    # Ask questions and process the lead's responses
    ask_questions(lead_id, lead_name, lead_interaction_times, lead_interaction_lock)

    # Print a divider and a success message
    print_divider()
    console.print("[bold green]✅ Operation Completed Successfully![/]", style="bold magenta")
