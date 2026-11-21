import pytest
from pydantic_ai.models.test import TestModel
import local


def test_tools_directly(tmp_path, monkeypatch):
    # Redirect NOTES_FILE inside local.py to a temporary test folder
    temp_notes = tmp_path / "notes.txt"
    monkeypatch.setattr(local, "NOTES_FILE", temp_notes)

    assert local.read_notes() == "No notes saved yet."
    assert "Saved note" in local.save_note("Buy milk")
    assert local.read_notes().strip() == "Buy milk"
    assert local.calculate("12 * (3 + 4)") == "84"
    assert local.calculate("__import__('os').system('ls')") == "Invalid math expression."


def test_agent_calls_all_tools_safely(tmp_path, monkeypatch):
    temp_notes = tmp_path / "notes.txt"
    monkeypatch.setattr(local, "NOTES_FILE", temp_notes)

    # local = your module (local.py); local.agent = the Agent object inside local.py
    with local.agent.override(model=TestModel()):
        result = local.agent.run_sync("Test all tools")
        assert isinstance(result.output, str)
        assert len(result.all_messages()) > 1
