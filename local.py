from datetime import datetime
from pathlib import Path

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider

NOTES_FILE = Path("notes.txt")

model = OpenAIChatModel(
    "qwen3.5:2b",
    provider=OllamaProvider(base_url="http://localhost:11434/v1"),
)




def get_current_time() -> str:
    """Return the current local date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate(expression: str) -> str:
    """Evaluate a simple math expression."""
    allowed = set("0123456789+-*/(). ")
    if not expression or not set(expression).issubset(allowed):
        return "Invalid math expression."
    return str(eval(expression, {"__builtins__": {}}))


def save_note(text: str) -> str:
    """Append a note to notes.txt."""
    with NOTES_FILE.open("a", encoding="utf-8") as f:
        f.write(text.rstrip() + "\n")
    return f"Saved note to {NOTES_FILE}"


def read_notes() -> str:
    """Read saved notes from notes.txt."""
    if not NOTES_FILE.exists():
        return "No notes saved yet."
    return NOTES_FILE.read_text(encoding="utf-8")


agent = Agent(
    model,
    tools=[get_current_time, calculate, save_note, read_notes],
    system_prompt=(
        "You are a helpful local assistant. Use your tools when asked to check "
        "the time, calculate math, or save/read notes."
    ),
)


def main() -> None:
    message_history = []
    print("Local agent ready. Type 'quit' or 'exit' to stop.")
    while True:
        user_input = input("\nYou: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            break
        result = agent.run_sync(user_input, message_history=message_history)
        message_history = result.all_messages()
        print(f"\nAgent: {result.output}")


if __name__ == "__main__":
    main()
