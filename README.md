# 💻 AI Coding Assistant V2

A **context-aware coding assistant** that understands your project structure and suggests smart code completions, generates docstrings, and reviews pull request diffs.

## 🧠 How It Works

1. **Project Scanning** — indexes codebase (imports, class/function definitions, docstrings)
2. **Context Extraction** — when you type, assistant reads surrounding code + nearby files
3. **Completion** — LLM suggests next lines grounded in project context (not just generic snippets)
4. **Explanation** — hover to see what each line does
5. **Code Review** — paste a diff; assistant flags potential bugs, style issues, performance problems

## Tech Stack
- **OpenAI GPT-4** – completions & review
- **LangChain** – context management
- **Tree-sitter / AST** – code parsing
- **Streamlit / VSCode Extension** – IDE integration

## 🚀 Getting Started
```bash
git clone https://github.com/Varshini487/ai-coding-assistant-v2
cd ai-coding-assistant-v2
pip install -r requirements.txt
streamlit run app.py
```

## 💡 Use Cases
- Faster coding with smart completions
- Learning new libraries (explanations + examples)
- Code review automation (catch bugs before PR)
- Docstring generation (maintain documentation)
