#!/usr/bin/env python3
import os
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../workspace')))
from git_manager import is_git_repo

@patch('git_manager.subprocess.run')
def test_is_git_repo_true(mock_run):
    mock_process = MagicMock()
    mock_process.returncode = 0
    mock_run.return_value = mock_process
    
    assert is_git_repo("/tmp") is True
