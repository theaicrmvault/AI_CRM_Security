"""
tests/test_app.py
Unit tests for app.py — no live API calls needed.
Run: python -m pytest tests/ -v
"""

import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Allow importing app.py from parent folder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def make_mock_response(text):
    """Build a fake Groq API response object."""
    choice = MagicMock()
    choice.message.content = text
    response = MagicMock()
    response.choices = [choice]
    return response


class TestAskFunction(unittest.TestCase):

    @patch.dict(os.environ, {"GROQ_API_KEY": "fake-key", "MODEL": "llama3-8b-8192"})
    @patch("groq.Groq")
    def test_ask_returns_answer(self, MockGroq):
        """ask() should return the assistant text and update history."""
        mock_client = MagicMock()
        MockGroq.return_value = mock_client
        mock_client.chat.completions.create.return_value = make_mock_response("  Paris  ")

        import importlib
        import app
        importlib.reload(app)
        app.client = mock_client

        history = []
        result = app.ask("Capital of France?", history)

        self.assertEqual(result, "Paris")
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0]["role"], "user")
        self.assertEqual(history[1]["role"], "assistant")

    @patch.dict(os.environ, {"GROQ_API_KEY": "fake-key"})
    @patch("groq.Groq")
    def test_history_grows_across_turns(self, MockGroq):
        """History should grow with each ask() call."""
        mock_client = MagicMock()
        MockGroq.return_value = mock_client
        mock_client.chat.completions.create.side_effect = [
            make_mock_response("Paris"),
            make_mock_response("It has the Eiffel Tower."),
        ]

        import importlib
        import app
        importlib.reload(app)
        app.client = mock_client

        history = []
        app.ask("Capital of France?", history)
        app.ask("Tell me more.", history)

        # 2 questions + 2 answers = 4 entries
        self.assertEqual(len(history), 4)


if __name__ == "__main__":
    unittest.main()