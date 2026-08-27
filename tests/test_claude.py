#!/usr/bin/env python3
"""
Unit tests for the Claude Code CLI wrapper.
"""

import pytest
from unittest.mock import patch, MagicMock
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../workspace')))
from claude_runner import ClaudeRunner

@patch('claude_runner.subprocess.Popen')
def test_claude_success(mock_popen):
    # Mock successful subprocess execution
    mock_process = MagicMock()
    mock_process.communicate.return_value = ("Success output", "")
    mock_process.returncode = 0
    mock_popen.return_value = mock_process

    runner = ClaudeRunner("/tmp/workspace")
    result = runner.run_plan("Test plan")
    
    assert result is True
    mock_popen.assert_called_once()

@patch('claude_runner.subprocess.Popen')
def test_claude_failure(mock_popen):
    # Mock failed subprocess execution
    mock_process = MagicMock()
    mock_process.communicate.return_value = ("", "Syntax Error")
    mock_process.returncode = 1
    mock_popen.return_value = mock_process

    runner = ClaudeRunner("/tmp/workspace")
    result = runner.run_plan("Bad plan")
    
    assert result is False
