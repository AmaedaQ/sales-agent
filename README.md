
#  Conversational Sales Agent with Threaded Processing

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/github/license/AmaedaQ/sales-agent)
![Threading](https://img.shields.io/badge/multithreading-supported-green)
![Architecture Diagram](architecture-diagram.png)

A Python-based multi-threaded sales agent that simulates multiple concurrent lead conversations, handles automated follow-ups, and stores persistent lead data in a CSV file. Built with the `rich` library for a clean, interactive terminal UI.

📽️ **Watch Demo:** [Tella Video Walkthrough](https://www.tella.tv/video/sales-agent-1-cpdm)

---

## 🚀 Features

- 🔄 Multi-threaded lead processing (5+ concurrent conversations)
- 💬 Beautiful terminal UI using the `rich` library
- ⏰ Automated follow-up system (e.g., 24-hour reminders)
- 📁 CSV-based lead storage
- 🧵 Thread-safe operations with locks for shared resources

---

## 📁 Project Structure

<pre>

sales-agent/
├── agent.py               # Core lead interaction logic
├── followup_manager.py    # Automated follow-up system
├── main.py                # Entry point and thread orchestration
├── trigger_simulator.py   # Lead simulation for testing
├── leads.csv              # Persistent storage of leads
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation

</pre>

---

## ⚙️ Installation

```bash
git clone https://github.com/AmaedaQ/sales-agent.git
cd sales-agent
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
````

---

## 🧪 Running the Application

### ▶️ Basic Run

```bash
python main.py
```

* Starts 5 concurrent lead conversations
* Enables background follow-up checks
* Saves interactions to `leads.csv`

### ⚙️ Advanced Options

```bash
# Simulate 10 leads
python main.py --leads 10

# Run follow-up test mode (faster delay)
python followup_manager.py --test-mode

# Only simulate leads without processing
python trigger_simulator.py --count 3
```

---

## 🔍 Key Modules Overview

| Module                 | Purpose                           | Key Concepts            |
| ---------------------- | --------------------------------- | ----------------------- |
| `agent.py`             | Conversational logic & data input | `rich`, CSV handling    |
| `followup_manager.py`  | Follow-up system and scheduler    | `threading`, `datetime` |
| `main.py`              | Thread orchestration and logging  | `threading`, `queue`    |
| `trigger_simulator.py` | Simulated lead generation         | CLI, randomness         |

---

## 📊 Sample CSV Format

```csv
lead_id,name,age,country,interest,status
1001,Alice,29,Canada,CRM Tools,secured
1002,,,,,no_response
```

---

## 🧪 Testing Checklist

1. **High-Concurrency Simulation**

```bash
python main.py --leads 20
```

2. **Follow-up Simulation (Fast Test Delay)**

```bash
python followup_manager.py --test-delay 5
```

3. **CSV Integrity Check**

```bash
python -c "import csv; print(len(list(csv.reader(open('leads.csv')))))"
```

---

## 💡 Design Decisions

* **Threading over Async**

  * Real multithreading preferred for CPU+I/O tasks
*  **Rich Terminal UI**

  * Improved UX with colors and formatting
*  **CSV as Data Store**

  * Portable and easy to integrate with external tools
*  **Background Follow-ups**

  * Daemon thread tracks elapsed time since last interaction

---

## 📜 License

Licensed under the [MIT License](LICENSE).

