# Local AI Agent Lab (Ollama + Pydantic AI)

A lightweight local command-line AI agent built with **Pydantic AI** and **Ollama** using custom Python tools—no cloud API keys required.

## Inspiration & Customization

This lab is inspired by Tech With Tim's tutorial [*Build a Local AI Agent in 10 Minutes using Python*](https://www.youtube.com/watch?v=ByWCsa8DbF8), adapted into a local Python lab with custom tools and automated tests.

## Features

- Runs locally against an Ollama server (`http://localhost:11434/v1`) using `OpenAIChatModel` and `OllamaProvider`.
- Includes local Python tools for checking the current date and time (`get_current_time`), evaluating basic arithmetic expressions (`calculate`), and saving or reading notes (`save_note`, `read_notes`).
- Maintains multi-turn conversation history in a command-line loop until you type `quit` or `exit`.
- Includes unit tests (`test_locall.py`) using `pytest` and Pydantic AI's `TestModel`.

## Setup

1. **Install Ollama** on your machine and verify the CLI is available:

   ```bash
   ollama
   ```

2. **Pull a local model** (such as `qwen3.5:2b`) and confirm it is listed locally:

   ```bash
   ollama pull qwen3.5:2b
   ollama list
   ```

3. **Create a virtual environment** inside your project folder:

   ```bash
   python3 -m venv .venv
   ```

4. **Activate the virtual environment** in your terminal:

   ```bash
   source .venv/bin/activate
   ```

5. **Upgrade `pip` and install dependencies** (`pydantic-ai` and `pytest`):

   ```bash
   python3 -m pip install --upgrade pip
   python3 -m pip install pydantic-ai pytest
   ```

## Usage

Make sure Ollama is running in the background and your `.venv` is active, then run the agent:

```bash
python3 local.py
```

Type `quit` or `exit` to stop the session.

## Running Tests

Run the test suite with `pytest`:

```bash
pytest -v
```

