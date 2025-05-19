
# Sales Agent with Google ADK

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![GitHub](https://img.shields.io/github/license/AmaedaQ/sales-agent)

A conversational sales agent that handles multiple lead interactions with automated follow-ups using Google's Agent Development Kit.

## 🚀 Features
- **Multi-conversation handling** - Manages multiple leads simultaneously
- **Automated follow-ups** - 24-hour reminder system
- **Data collection** - Structured information gathering
- **CSV storage** - Persistent lead data storage

## 📦 Installation
```bash
git clone https://github.com/AmaedaQ/sales-agent.git
cd sales-agent
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## ⚙️ Configuration
1. Create `config.ini`:
```ini
[DEFAULT]
CREDENTIALS_PATH = path/to/service-account.json
CSV_STORAGE = leads.csv
```

2. Set up Google Cloud credentials:
- Enable Dialogflow CX API
- Create service account with Dialogflow Agent Admin role

## 🖥️ Usage
```bash
# Start the agent
python main.py

# Simulate leads (5 leads)
python trigger_simulator.py --leads 5

# Test follow-ups
python followup_manager.py --test-mode
```

## 📂 Files
| File | Purpose |
| `agent.py` | Core agent logic |
| `followup_manager.py` | Follow-up system |
| `main.py` | Program entry point |
| `leads.csv` | Lead data storage |

## 📝 Data Storage
All lead data is stored in `leads.csv` with columns:
- `lead_id`, `name`, `age`, `country`, `interest`, `status`, `timestamp`

## 📜 License
MIT © 2025 [Amaeda]

