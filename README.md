# Playwright + Behave Example

This repository contains an automated test setup using [Playwright](https://playwright.dev/python/) and [Behave](https://behave.readthedocs.io/en/stable/) for browser-based functional testing using Gherkin syntax.

## 🚀 Features

- Uses **DuckDuckGo** to demonstrate search functionality.
- Structured with `feature` files and Python step definitions.
- Includes:
  - `Scenario Outline` with multiple examples
  - Logging and screenshots on error
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

## 📝 Project Structure

```
project-root/
├── features/
│   ├── duckduckgo_search.feature
│   └── steps/
│       └── duckduckgo_steps.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔍 How It Works

- `duckduckgo_search.feature` defines a Scenario Outline with multiple test cases.
- `duckduckgo_steps.py` contains the step implementations using Playwright sync API.
- Logs and screenshots are automatically saved if an error occurs.

---

## 🧼 Clean Commands

If you ever want to clean up screenshots or cached data:

```bash
rm *.png
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

## 🤝 Contributing

PRs and issues are welcome!
