# 🚀 Automation Testing Repository

This repository contains my complete Automation Testing learning journey using **Selenium**, **Playwright**, and **API Testing** with **Python**.

The repository is organized into different modules covering browser automation, framework development, advanced Playwright concepts, and API automation.

---

# 📁 Repository Structure

```
AUTOMATION_TESTING
│
├── API Testing/
│
├── Playwright/
│   ├── Browser Automation/
│   ├── Configuration/
│   ├── Parameterized Testing/
│   └── POM/
│
├── Selenium/
│   ├── amazon.py
│   ├── flipkart.py
│   ├── practice.py
│   ├── test.py
│   └── test2.py
│
├── test-results/
│
├── logout_trace.zip
├── trace.zip
│
└── README.md
```

---

# 🛠 Tech Stack

- Python
- Selenium
- Playwright
- Pytest
- Pytest HTML
- Pytest-xdist
- Git & GitHub
- VS Code

---

# 📚 Selenium

Contains practice scripts for learning Selenium WebDriver with Python.

### Topics Covered

- Browser Launch
- Locators
- XPath
- CSS Selectors
- WebElement Methods
- Navigation Commands
- Waits
- Forms
- Browser Automation

---

# 🎭 Playwright

## Browser Automation

Topics Covered

- Browser Launch
- Browser Context
- New Page
- Locators
- Assertions
- Auto Waiting
- Screenshots
- Trace Viewer
- Videos

---

## Configuration

Topics Covered

- pytest.ini
- Config File
- Command Line Execution
- Timeouts
- Retries
- HTML Reports

---

## Parameterized Testing

Topics Covered

- pytest.mark.parametrize
- Multiple Test Data
- Login Validation
- HTML Reports
- Parallel Execution

---

## POM Framework

Implemented using **Page Object Model (POM)**.

### Features

- Page Object Model
- Fixtures
- Reusable Methods
- Assertions
- HTML Reports
- Parallel Execution
- Cross Browser Concepts
- Trace Viewer
- Playwright Inspector

### Test Scenarios

- Valid Login
- Invalid Username
- Invalid Password
- Blank Username
- Blank Password

---

# 🌐 API Testing (In Progress)

Learning API Automation using Playwright.

### Topics

- API Fundamentals
- Client Server Architecture
- HTTP Protocol
- HTTP Methods
- HTTP Requests
- HTTP Responses
- JSON
- REST APIs
- Authentication
- Playwright API Testing

---

# ▶ Running Tests

Run all tests

```bash
python -m pytest
```

Run a specific file

```bash
python -m pytest tests/test_login.py
```

Run with verbose output

```bash
python -m pytest -v
```

---

# ⚡ Parallel Execution

Run using 2 workers

```bash
python -m pytest -n 2
```

Run using all CPU cores

```bash
python -m pytest -n auto
```

---

# 📊 Generate HTML Report

```bash
python -m pytest --html=reports/report.html --self-contained-html
```

---

# 🐞 Debugging

### Playwright Inspector

```python
page.pause()
```

### Trace Viewer

Generate Trace

```python
context.tracing.start(
    screenshots=True,
    snapshots=True,
    sources=True
)

...

context.tracing.stop(
    path="trace.zip"
)
```

Open Trace

```bash
playwright show-trace trace.zip
```

---

# 🎯 Learning Roadmap

## ✅ Selenium

- Browser Automation
- Locators
- XPath
- CSS Selectors
- Waits
- Forms

---

## ✅ Playwright

### Core Playwright

- Auto Waiting
- Assertions
- Pages
- Navigation
- Dialogs
- Frames
- Events
- Isolation
- Videos

### Framework Development

- Fixtures
- POM
- Configuration
- Command Line
- Timeouts
- Retries
- HTML Reports
- Parameterized Testing

### Advanced Execution

- Projects
- Parallel Execution
- Global Setup & Teardown
- Emulation
- Debugging
- Trace Viewer

---

## 🚧 API Testing (Currently Learning)

- API Fundamentals
- HTTP Protocol
- HTTP Methods
- REST APIs
- Authentication
- API Automation with Playwright

---

# 📌 Future Enhancements

- JWT Authentication
- API Framework
- Network Interception
- Mock APIs
- Visual Testing
- Accessibility Testing
- GitHub Actions (CI/CD)
- Logging
- Data Driven Testing
- Screenshots on Failure

---

# 👨‍💻 Author

**Animesh Garg**

B.Tech Computer Science & Engineering (Cloud Computing)

SRM Institute of Science and Technology

---

# ⭐ Repository Goal

This repository documents my end-to-end Automation Testing journey, from Selenium fundamentals to advanced Playwright framework development and API automation, while following industry-standard best practices.