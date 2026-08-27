#!/usr/bin/env python3
"""
Unit tests for the Gemini Architectural client.
Requires pytest: pip install pytest
"""

import pytest
from unittest.mock import patch, MagicMock
import os
import sys

# Ensure workspace is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../workspace')))
from gemini_client import GeminiArchitect

@patch.dict(os.environ, {"GEMINI_API_KEY": "test_key"})
@patch('gemini_client.genai.Client')
def test_generate_plan(mock_client_class):
    # Mock the API response
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "Plan: 1. Create file. 2. Write code."
    mock_client.models.generate_content.return_value = mock_response
    mock_client_class.return_value = mock_client

    architect = GeminiArchitect()
    plan = architect.generate_plan("Make a snake game.")
    
    assert "Plan:" in plan
    mock_client.models.generate_content.assert_called_once()

def test_missing_api_key():
    with patch.dict(os.environ, clear=True):
        with pytest.raises(SystemExit):
            GeminiArchitect()
