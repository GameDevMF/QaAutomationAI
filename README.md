# QA Automation & AI Testing Playground (Python)

This repository is a personal QA automation learning project focused on building real-world testing skills using Python, pytest, API testing, UI automation, and CI/CD basics.

It is designed to simulate how modern QA Engineers structure automation frameworks in real companies.

---

## 🚀 Tech Stack

- Python 3.x
- pytest (test framework)
- requests (API testing)
- Playwright (UI automation - planned/expanding)
- GitHub Actions (CI/CD - upcoming)

---

## 📁 Project Structure
qa-automation-ai/
│
├── api_tests/ # API test cases using pytest
├── ui_tests/ # UI automation tests (Playwright)
├── core/ # Reusable components (API client, helpers)
├── ai_experiments/ # AI-assisted testing experiments
├── requirements.txt # Dependencies
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