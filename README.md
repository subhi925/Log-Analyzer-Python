# Custom CLI Log Analyzer & Reporter

A Python-based Command Line Interface (CLI) tool designed for Application Support and QA teams to analyze large system log files efficiently. Instead of manually digging through thousands of log lines during a production incident, this tool automates the process by generating instant summary reports or searching for specific user activities using Regular Expressions (Regex).

## 🚀 Features

* **Interactive CLI Menu:** User-friendly menu with automated input validation.
* **Smart Summary Report:** Scans the log file, counts `ERROR` and `WARNING` levels, and generates a clean, structured `my_report.txt` file (only if issues are found).
* **Targeted User Search:** Uses dynamic Regular Expressions to extract and display all log lines associated with a specific username in real-time.
* **Robust Error Handling:** Built-in exception handling to prevent system crashes during file I/O operations.
* **Built-in Test Suite:** Includes a dynamic log generator script (`generate_logs.py`) to simulate realistic production data (250+ lines).

## 🛠️ Tech Stack

* **Language:** Python 3
* **Core Libraries:** `re` (Regular Expressions), `random`, `datetime`

## 🏃‍♂️ How to Run

1. Clone the repository to your local machine.
2. Run the log generator to create a mock database log file:
   ```bash
   python generate_logs.py
