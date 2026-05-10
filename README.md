![Tests](https://github.com/GameDevMF/QaAutomationAI/actions/workflows/tests.yml/badge.svg)

# QA Automation Framework (Python + Playwright + Pytest)

A modular QA automation framework built with Python, Pytest, Playwright, API testing, and GitHub Actions CI/CD.

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
- Automatic screenshots on failure
- HTML reporting
- Reusable Page Object Model

---

## 🏛️ Architecture

- API layer (ApiClient)
- UI layer (Page Object Model)
- Shared config (environment-based)
- Test data separation
- CI/CD pipeline with GitHub Actions

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
├── integration_tests/ # API & UI combined automation tests (Playwright)<br>
├── flows/ # Reusable flows<br>
├── core/ # Reusable components (API client, helpers)<br>
├── test_data/ # Data Driven test data<br>
├── pages/ # POM pages<br>
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
playwright install
```

### 2. Run tests
```bash
pytest -v
pytest -m ui
pytest -m api
pytest -m integration
```

### 3. Run with detailed output
```bash
pytest -v -s
```

---

## 🚫 Limitations

The project uses JSONPlaceholder, a mock API service that does not enforce real validation rules for POST requests.
