# Playwright + Behave Example

This repository contains an automated test setup using [Playwright](https://playwright.dev/python/) and [Behave](https://behave.readthedocs.io/en/stable/) for browser-based functional testing using Gherkin syntax.

## 🚀 Features

- Uses **DuckDuckGo** to demonstrate search functionality.
- Structured with `feature` files and Python step definitions.
- Includes:
  - `Scenario Outline` with multiple examples
  - Logging and screenshots on error
  - Playwright **Tracing** support per scenario
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

Playwright Tracing is enabled **per scenario**. Each `.zip` trace file is saved to the `traces/` directory.

### Open a trace file:

```bash
playwright show-trace traces/Search_openai_and_verify_link.zip
```

You can also open all trace files in batch:

**Bash**:

```bash
for f in traces/*.zip; do playwright show-trace "$f"; done
```

**PowerShell**:

```powershell
Get-ChildItem -Path traces -Filter *.zip | ForEach-Object { playwright show-trace $_.FullName }
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
├── traces/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧼 Clean Commands

If you ever want to clean up screenshots, traces or cached data:

```bash
rm *.png
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

## 🤝 Contributing

PRs and issues are welcome!