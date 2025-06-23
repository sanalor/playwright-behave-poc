# Playwright + Behave Example

This repository contains an automated test setup using [Playwright](https://playwright.dev/python/) and [Behave](https://behave.readthedocs.io/en/stable/) for browser-based functional testing using Gherkin syntax.

## 🚀 Features

- Uses **DuckDuckGo** to demonstrate search functionality.
- Structured with Gherkin `feature` files, Python step definitions, and **Page Object Model (POM)**.
- Includes:
  - `Scenario Outline` with multiple examples
  - Screenshots saved **only on scenario failure**
  - Playwright **Tracing** enabled **per scenario**, with timestamped `.zip` files
  - Centralized helper functions (`utils/helpers.py`) for reusable logic
  - Logging of trace and scenario status
  - Clean setup for GitHub

---

## 🧰 Requirements

- Python 3.8+
- Git Bash / Terminal
- Google Chrome or Chromium installed

---

## 📦 Installation

> Install dependencies globally (not using `venv`):

```bash
pip install -r requirements.txt
playwright install
```

---

## 🧪 Running Tests

```bash
behave
```

Optional: run specific tagged scenarios:

```bash
behave --tags=@search
```

---

## 🔍 Playwright Tracing

Playwright Tracing is enabled **per scenario**. Each `.zip` file is saved to the `traces/` directory with a timestamp.

### Open a trace file:

```bash
playwright show-trace traces/2025-06-23_19-10-12_Search_openai_and_verify_link.zip
```

### Open all traces (batch):

**Bash**:

```bash
for f in traces/*.zip; do playwright show-trace "$f"; done
```

**PowerShell**:

```powershell
Get-ChildItem -Path traces -Filter *.zip | ForEach-Object { playwright show-trace $_.FullName }
```

---

## 📸 Failure Screenshots

If a scenario fails, a screenshot is saved automatically to the `reports/failures/` directory.  
Filenames include a timestamp and scenario name, e.g.:

```
reports/failures/2025-06-23_19-12-45_Search_openai_and_verify_link.png
```

---

## 📝 Project Structure

```
project-root/
├── features/
│   ├── duckduckgo_search.feature
│   ├── steps/
│   │   └── duckduckgo_steps.py
│   └── environment.py
├── pages/
│   └── duckduckgo_page.py
├── utils/
│   └── helpers.py
├── traces/
├── reports/
│   └── failures/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧼 Clean Commands

Clean screenshots, traces, and cache:

```bash
rm -r reports/failures/
rm -r traces/
find . -type d -name '__pycache__' -exec rm -r {} +
```

---

## ✅ Recommended VS Code Extensions

- **Behave VSC** by `jLafitte` (for step linking)
- Python by Microsoft

---

## 🧪 Example Output

```bash
Feature: DuckDuckGo Search

  Scenario Outline: Search <term> and verify link
    Given I open the browser and go to DuckDuckGo
    When I search for "<term>"
    Then I should see "<expected>" in the results

    Examples:
      | term      | expected        |
      | mercadona | mercadona.es    |
      | openai    | openai.com      |
```

---

## 📈 Future Improvements

- Add **Allure Reporting** integration for rich visual reporting
- Capture **videos per scenario**
- Add support for **multiple browsers** (Firefox, WebKit)
- Integrate with **CI/CD pipelines** (GitHub Actions, Jenkins)
- Add **tag filtering** in `behave.ini`
- Support **parallel execution** using `pytest-playwright` or similar

---

## 🤝 Contributing

PRs and issues are welcome!