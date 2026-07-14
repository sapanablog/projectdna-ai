<p align="center">
  <img src="screenshots/banner.png" alt="ProjectDNA-AI Banner" width="100%">
</p>

<h1 align="center">🧬 ProjectDNA-AI</h1>

<p align="center">
An extensible AI Coding Assistant built with <strong>Pydantic AI</strong>, <strong>OpenRouter</strong>, and <strong>Google Gemini</strong>.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Pydantic AI](https://img.shields.io/badge/Pydantic-AI-red)
![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM-success)
![Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?logo=google)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

<p align="center">
<img src="screenshots/demo.gif" alt="Project Demo" width="900">
</p>

---

# Overview

ProjectDNA-AI is a modular AI coding assistant that demonstrates the core principles of **Agentic AI** using **Pydantic AI**. The assistant combines conversational memory, adaptive reasoning, tool calling, execution hooks, and dynamically loaded skills within a clean and extensible architecture.

The project was developed after completing the **Agentic AI Masterclass** from the **appliedAI Institute for Europe**, delivered through the **THRIVE Machine Learning Specialization (Kiron Education)**. While following the concepts introduced in the masterclass, the implementation has been reorganized into a modular Python project to improve maintainability, readability, and future extensibility.

---

# Why ProjectDNA-AI?

Traditional chatbot examples generate text responses but cannot interact with their environment.

ProjectDNA-AI extends this concept by enabling the assistant to:

- maintain conversational context across multiple interactions
- interact with the local file system through tools
- adapt its reasoning effort depending on task complexity
- discover new capabilities through dynamically loaded Markdown skills
- organize functionality into reusable modules following a capability-based design

The result is a lightweight foundation for building more advanced agentic AI applications.

---

# Features

- Multi-turn conversation memory
- Adaptive reasoning (Low / Medium / High)
- File system tool calling
  - Read files
  - Write files
  - Search files
  - Delete files
- Real-time execution logging through hooks
- Dynamic skill discovery using Markdown
- Modular capability-based architecture
- OpenRouter integration with Google Gemini models
- Clean separation between tools, capabilities, and agent configuration

---

# Project Structure

```text
ProjectDNA-AI/
│
├── main.py                    # CLI entry point
├── agent.py                   # Agent configuration
│
├── capabilities/
│   ├── file_operations.py     # Tool registration + execution hooks
│   ├── reasoning.py           # Dynamic reasoning selection
│   └── skills.py              # Dynamic skill loading
│
├── tools/
│   └── file_tools.py          # File operation tools
│
├── skills/
│   └── code_review.md         # Example skill
│
├── screenshots/
│
├── requirements.txt
├── .env.example
└── README.md
```

---

# Architecture

```text
                         User
                           │
                           ▼
                    ProjectDNA-AI
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
      Reasoning      File Operations     Skills
             │             │             │
             ▼             ▼             ▼
     Model Settings   File Tools   Markdown Skills
                           │
                           ▼
                  Local File System
```

---

# Technologies

| Category | Technology |
|-----------|------------|
| Language | Python 3.11 |
| AI Framework | Pydantic AI |
| LLM Gateway | OpenRouter |
| Model | Google Gemini 2.5 Flash |
| API Client | OpenAI Python SDK |
| Configuration | python-dotenv |
| Metadata | python-frontmatter |

---

# Installation

Clone the repository

```bash
git clone https://github.com/sapanablog/ProjectDNA-AI.git

cd ProjectDNA-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
OPENROUTER_API_KEY=your_api_key
```

Run the assistant

```bash
python main.py
```

---

# Example Conversation

```text
You:
Hi, my name is Sapana.

Assistant:
Hello Sapana! How can I help you today?

You:
What is my name?

Assistant:
Your name is Sapana.
```

---

# File Operations Example

```text
You:
Create a file called notes.txt containing
"Hello ProjectDNA-AI".

Read the file.

Delete it afterwards.

→ Calling tool: write_file

→ Calling tool: read_file

→ Calling tool: delete_file

Assistant:
The requested file was successfully created,
read, and deleted.
```

---

# Adaptive Reasoning

The assistant dynamically adjusts the model's reasoning effort depending on the user's request.

| Task | Reasoning |
|------|-----------|
| Greetings | Low |
| General coding questions | Medium |
| Debugging | High |
| System design | High |
| Algorithm discussion | High |

---

# Dynamic Skills

Skills are automatically discovered from the `skills/` directory.

Current implementation:

- Code Review

Additional skills can be added simply by creating new Markdown files with frontmatter metadata—no changes to the Python application are required.

---

# Screenshots

### Application Startup

*(Add screenshot)*

---

### Conversation Memory

*(Add screenshot)*

---

### Tool Execution Logging

*(Add screenshot)*

---

### Dynamic Skill Loading

*(Add screenshot)*

---

### Adaptive Reasoning

*(Add screenshot)*

---

# Future Improvements

Possible future extensions include:

- Long-term memory with vector databases
- Retrieval-Augmented Generation (RAG)
- GitHub repository integration
- Web search capability
- Sandboxed Python execution
- Additional reusable skills
- Docker deployment
- Unit test generation
- Multi-agent collaboration

---

# What I Learned

Through this project I gained practical experience with:

- Designing modular AI applications
- Building reusable capabilities in Pydantic AI
- Maintaining conversation state
- Implementing tool calling
- Using execution hooks
- Dynamically adjusting model settings
- Loading runtime skills
- Structuring Python projects for maintainability
- Integrating OpenRouter with Google Gemini

---

# Author

**Sapana Gupta**

AI Developer | Machine Learning Engineer

**LinkedIn**

https://www.linkedin.com/in/sapana-g-074656176/

**GitHub**

https://github.com/sapanablog

---

# Acknowledgements

This project was completed as part of the **Agentic AI Masterclass** developed by the **appliedAI Institute for Europe** and delivered through the **THRIVE Machine Learning Specialization** by **Kiron Education**.

The repository builds upon the concepts introduced throughout the masterclass—including conversational agents, tool calling, execution hooks, adaptive reasoning, and dynamic skills—while reorganizing the implementation into a modular, portfolio-ready Python project.