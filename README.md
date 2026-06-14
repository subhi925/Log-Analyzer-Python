# Custom Log Analyzer & Reporter (v1.0 & v2.0)

A Python-based Command Line Interface (CLI) tool designed for Application Support and QA teams to analyze large system log files efficiently. Instead of manually digging through thousands of log lines during a production incident, this tool automates the process by generating instant summary reports or searching for specific user activities using Regular Expressions (Regex) and Timestamp filtering.

This repository showcases the evolution of the tool from a basic procedural script to a dynamic, decoupled, production-ready architecture.

---

## 📂 Project Structure & Evolution

The project includes two versions to demonstrate code refactoring and architectural growth:

### 1️⃣ Baseline Version: `analyzerLog.py` (Procedural & Interactive)
The foundational version of the tool. It introduces the core log-parsing logic using Regular Expressions (`re`) and standard file handling.
* **Key Features:** Interactive user menu, hardcoded target keywords (`ERROR` and `WARNING`), and real-time user activity tracking.
* **Takeaway:** Demonstrates strong basic programming principles, logic flow, and input validation.

### 2️⃣ Advanced Version: `analyzerLog2.PY` (Decoupled, Dynamic & Time-Aware)
The advanced, refactored version built for enterprise scalability. It completely separates the configuration data from the execution logic and introduces advanced timestamp parsing.
* **Key Features:** * Decoupled settings via `config.json` for dynamic log-level tracking.
  * Robust error handling with clean exception reflecting (`type(err).__name__`).
  * **Time-Based Filtering:** Parses and evaluates log timestamps using the `datetime` module to filter user actions after a specific hour.
* **Takeaway:** Demonstrates clean code architectures (DRY & SRP principles), scalability, and adaptability to real production environments.

---

## 🛠️ Features & Interactive Menu (v2.0)

When running the advanced version, the user is presented with three powerful operations:

* **Option 1: Global Summary Report** – Counts all occurrences of the log levels specified in `config.json` and exports a clean `my_report.txt` summary.
* **Option 2: User Log Search** – Scans the entire file using Regex to instantly display every log line associated with a specific username.
* **Option 3: Targeted Time-Window Analysis** – Extracts logs for a specific user **only after a user-defined timestamp (`HH:MM:SS`)**. It counts the log levels within that window and generates a dedicated custom report file (e.g., `subhi_h_report.txt`).

---

## ⚙️ Configuration Setup (`config.json`)

For **v2.0**, the application behavior can be customized instantly by modifying the external configuration file without touching a single line of Python code:

```json
{
    "file_path": "app.log",
    "log_levels": ["INFO", "WARNING", "ERROR"]
}
🏃‍♂️ How to Run (Step-by-Step)
Follow these steps to set up the environment and run either version of the tool:

Step 1: Clone the Repository
Bash
git clone <your-repository-url>
cd <repository-folder>
Step 2: Generate Mock Production Logs
Run the built-in log generator script to simulate a realistic production log file (app.log) containing over 250+ lines of mock data:

Bash
python generate_logs.py
Step 3: Run the Analyzer
To run the Baseline Version (v1.0):

Bash
python analyzerLog.py
To run the Advanced Dynamic Version (v2.0):

Bash
python analyzerLog2.PY
🛠️ Tech Stack
Language: Python 3

Data Format: JSON (for configuration management in v2.0)

Core Libraries: re (Regular Expressions), json, datetime