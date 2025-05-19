
# Conversational Sales Agent with Threaded Processing

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![GitHub](https://img.shields.io/github/license/AmaedaQ/sales-agent)
![Threading](https://img.shields.io/badge/multithreading-supported-green)

A sales agent system that handles concurrent lead interactions with automated follow-ups, built with Python threading and rich terminal UI.

## 🚀 Key Features

- **Multi-threaded Processing**: Handles 5+ simultaneous lead conversations
- **Rich Terminal UI**: Beautiful console output with `rich` library
- **Automated Follow-ups**: 24-hour reminder system (configurable)
- **CSV Data Storage**: Persistent lead tracking with `leads.csv`
- **Thread-safe Operations**: Lock-protected shared resources

## 📦 Project Structure

```
sales-agent/
├── agent.py               # Core conversation logic (70% of system)
├── followup_manager.py    # Automated follow-up system
├── main.py                # Entry point with thread orchestration
├── trigger_simulator.py   # Lead generation simulator
├── leads.csv              # Persistent lead storage
├── requirements.txt       # Dependencies
└── README.md
```

## 🛠️ Installation

```bash
git clone https://github.com/AmaedaQ/sales-agent.git
cd sales-agent
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt
```

## 🖥️ Usage

### Basic Operation
```bash
python main.py
```
- Processes 5 simulated leads
- Runs follow-up checks in background
- Saves results to `leads.csv`

### Advanced Options
```bash
# Custom number of leads
python main.py --leads 10

# Test follow-up system only
python followup_manager.py --test-mode

# Generate leads without processing
python trigger_simulator.py --count 3
```

## 🔧 Core Components

| File | Responsibility | Key Technologies |
|------|----------------|------------------|
| `agent.py` | Conversation flow, data collection | `rich`, CSV handling |
| `followup_manager.py` | 24-hour follow-up system | `datetime`, threading |
| `main.py` | Thread orchestration | `threading`, queue |
| `trigger_simulator.py` | Lead generation | Randomization, queues |

## 📊 Data Model
```csv
lead_id,name,age,country,interest,status
1234,John Doe,35,USA,AI Tools,secured
5678,,,no_response
```

## 🧪 Testing the System

1. **Concurrency Test**:
```bash
python main.py --leads 20
```

2. **Follow-up Simulation**:
```bash
python followup_manager.py --test-delay 5  # 5-second test delay
```

3. **Data Integrity Check**:
```bash
python -c "import csv; print(len(list(csv.reader(open('leads.csv')))))"
```

## 🏗️ Design Decisions

1. **Threading over Async**:
   - Chose `threading` for true parallel processing
   - Better for CPU-bound conversation tasks

2. **Rich UI**:
   - Professional console interface
   - Color-coded message types

3. **CSV Storage**:
   - Simple, portable data format
   - Easy integration with analytics tools

4. **Follow-up System**:
   - Background thread with configurable delay
   - Tracks last interaction timestamp

## 📜 License
MIT License - See [LICENSE](LICENSE) for details.
