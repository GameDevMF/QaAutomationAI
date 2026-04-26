![Tests](https://github.com/GameDevMF/QaAutomationAI/actions/workflows/tests.yml/badge.svg)

# QA Automation & AI Testing Playground (Python)

This repository is a personal QA automation learning project focused on building real-world testing skills using Python, pytest, API testing, UI automation with Playwright, and CI/CD integration via GitHub Actions.

It is designed to simulate how modern QA Engineers structure automation frameworks in real companies.

---

## 📋 Features

- API testing (GET, POST, negative cases)
- UI automation (Playwright)
- Reusable test framework structure
- Data-driven testing
- Logging and error handling
- Environment-based configuration
- CI/CD pipeline (GitHub Actions)

---

## 🚀 Tech Stack

- Python 3.x
- pytest (test framework)
- requests (API testing)
- Playwright (UI automation - planned/expanding)
- GitHub Actions (CI/CD - upcoming)

---

## 📁 Project Structure
qa-automation-ai/<br>
├── api_tests/ # API test cases using pytest<br>
├── ui_tests/ # UI automation tests (Playwright)<br>
├── core/ # Reusable components (API client, helpers)<br>
├── ai_experiments/ # AI-assisted testing experiments<br>
├── requirements.txt # Dependencies<br>
└── README.md

---

## 🧪 What This Project Covers

### API Testing
- GET requests validation
- POST requests with payloads
- Status code validation
- JSON response assertions
- Negative testing (invalid endpoints)

### Test Framework
- pytest-based structure
- Reusable test logic
- Clean assertions with meaningful error messages

### UI Testing (in progress)
- Playwright-based browser automation
- End-to-end test scenarios

### CI/CD (planned)
- GitHub Actions pipeline
- Automated test execution on push

---

## 🔧 Configuration

Environment variables:

- HEADLESS → controls browser mode (false shows browser)
- SLOW_MO → controls execution speed (use it to see browser)
- BASE_URL → API base URL

The variables can be configured using an environment variable:

For Windows Powershell
```bash
$env:HEADLESS="true"
$env:SLOW_MO="500"
$env:BASE_URL="https://jsonplaceholder.typicode.com/"
```

For Windows CMD
```bash
set HEADLESS=false
set SLOW_MO=0
set BASE_URL=https://jsonplaceholder.typicode.com/
```

For Linux
```bash
export HEADLESS=true
export SLOW_MO=500
export BASE_URL=https://your-api-url.com
```

---

## ▶️ How to Run Tests

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run tests
```bash
pytest -v
```

### 3. Run with detailed output
```bash
pytest -v -s
```