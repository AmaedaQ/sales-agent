
# Conversational Sales Agent (Simulating Google ADK)

This Python project implements a conversational sales agent that handles multiple leads concurrently, collects information, and manages follow-ups. It was developed for the AI Candidates Evaluation Task.

**Note on Google ADK:** This project simulates Google ADK functionalities using standard Python (`asyncio`) as the specific ADK was not provided/readily available. The aim is to demonstrate core agent orchestration, context management, and concurrent processing.

## Core Features

* **Concurrent Lead Handling:** Manages multiple conversations simultaneously using `asyncio`.
* **Information Collection:** Engages leads to collect consent, age, country, and product interest.
* **Data Persistence:** Stores lead data in a CSV file (`leads.csv` or `simulation_leads.csv`).
* **Automated Follow-ups:** Sends follow-up messages to unresponsive leads after a simulated delay.
* **State Management:** Tracks the state of each conversation independently.

## Project Structure

```

sales\_agent\_project/
├── agent.py             \# Agent's conversational logic
├── state\_manager.py     \# Manages state & CSV persistence
├── main.py              \# Main application entry point & demo
├── simulation.py        \# Targeted test case simulations
├── leads.csv            \# Output from main.py
├── requirements.txt     \# Dependencies
└── README.md            \# This file

````

## Setup

1.  **Clone the repository (or download files).**
2.  **Navigate to the project directory:**
    ```bash
    cd sales_agent_project
    ```
3.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv .venv
    # Windows: .\.venv\Scripts\activate
    # macOS/Linux: source .venv/bin/activate
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Run the Main Demonstration

This runs a built-in simulation showcasing multiple leads and follow-ups. Output is saved to `leads.csv`.

```bash
python main.py
````

### 2\. Run Specific Test Scenarios

This executes predefined test cases (e.g., consent decline, successful flow, concurrency). Output is saved to `simulation_leads.csv`.

```bash
python simulation.py
```

## Key Design Choices

  * **ADK Simulation:** Core ADK concepts (event handling, state, agent logic) are modeled with Python's `asyncio` and custom classes.
  * **Concurrency:** `asyncio` for non-blocking I/O and concurrent conversation management.
  * **State:** In-memory dictionary (`active_conversations` in `StateManager`) with `asyncio.Lock` for safe concurrent access.
  * **Data Storage:** Lead details are logged to CSV files using `pandas`.

This project demonstrates the ability to design and implement a complex, stateful, and concurrent AI agent system.
