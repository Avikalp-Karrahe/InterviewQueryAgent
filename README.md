# 🤖 Interview Query Content-Builder Agent

**An autonomous agent that writes, tests, and publishes Interview Query take-home guides for you.**

> **TL;DR:** Provide API keys & Notion parent once, then run `trae run takehome.yaml`—the agent does the rest: research, writing, charting, grading, Notion-publishing, self-testing, and GitHub commit.

---

## 📋 Table of Contents
1. [Features](#features)  
2. [Installation & Setup](#installation--setup)  
3. [Configuration](#configuration)  
4. [Usage](#usage)  
5. [File Structure](#file-structure)  
6. [Contributing](#contributing)  
7. [License](#license)  

---

## Features
- 🤓 **AI-Driven Writing**: Rewrites interview guides per Outline & Styling rules.  
- 📊 **Chart Generation**: Creates Mermaid flowcharts & Python/Matplotlib funnel charts.  
- 📝 **Question Selection**: Picks & formats top questions from CSV banks.  
- 🏆 **Grading & Refinement**: Scrapes official spec, highlights gaps, auto-improves content.  
- 📖 **Publishing**: Pushes polished pages to Notion and opens public links.  
- 🔄 **Self-Test**: Verifies each page via HTTP checks.  
- 📂 **GitHub Commit**: Pushes artifacts and README to your repo.

---

## Installation & Setup
```bash
git clone https://github.com/Avikalp-Karrahe/InterviewQueryAgent.git
cd InterviewQueryAgent

python3 -m venv .venv && source .venv/bin/activate
pip install --upgrade openai notion-client pandas requests matplotlib bs4 mermaid-python
```

---

## Configuration
Create a file `.env` or export in your shell:
```bash
export OPENAI_API_KEY="sk-..."         # Your OpenAI secret
export NOTION_TOKEN="ntn_..."          # Your Notion integration token
export NOTION_PARENT="your_notion_page_id"
```

---

## Usage
Run the agent’s YAML workflow:
```bash
trae run takehome.yaml
```
After ~5–10 minutes you’ll see output: two public Notion URLs and a JSON blurb for submission. Artifacts and README are also committed to GitHub.

---

## File Structure
```
.
├── takehome.yaml                # Trae workflow config
├── takehome_implementation.py   # Core Python orchestration
├── test_key.py                  # OpenAI/Notion token checker
├── meta_funnel.png              # Generated funnel chart
├── .gitignore                   # Excludes raw data & venv
└── README.md                    # This agent overview
```

---

## Contributing
1. Fork this repo.  
2. Create a feature branch: `git checkout -b feature/my-improvement`.  
3. Commit your changes.  
4. Push and open a PR.

---

## License
Distributed under the MIT License. See [LICENSE](LICENSE) for details.
