"""
@author: Carson Lee
"""
import unittest
from unittest.mock import patch, Mock
from GitHubAPI import get_repos, get_commit_count
from io import StringIO

class TestCommits(unittest.TestCase):
    
    # Testing as if fetching the commits and repos succeeded
    @patch('requests.get')
    def test_get_commit_count_success(self, mock_get):
        # Mocking the response for commit count
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = ['commit1', 'commit2', 'commit3']  # Simulating 3 commits
        mock_get.return_value = mock_response
        
        # Testing the function
        commit_count = get_commit_count("testuser", "testrepo")
        self.assertEqual(commit_count, 3)

    # Testing as if fetching the commits and repos failed
    @patch('requests.get')
    def test_get_commit_count_failure(self, mock_get):
        # Mocking the failure response for commit count
        mock_response = Mock()
        mock_response.status_code = 404  # Simulating an error response (not found)
        mock_get.return_value = mock_response
        
        # Testing the function when the commit count fails
        commit_count = get_commit_count("testuser", "testrepo")
        self.assertEqual(commit_count, 0)


class TestRepos(unittest.TestCase):

    # Testing as if fetching the repos was a success
    @patch('requests.get')
    def test_get_repos_success(self, mock_get):
        # Mocking the response for repositories
        mock_repo_response = Mock()
        mock_repo_response.status_code = 200
        mock_repo_response.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]  # Simulating 2 repos
        mock_get.return_value = mock_repo_response
        
        # Mocking the commit count response for both repos
        mock_commit_response = Mock()
        mock_commit_response.status_code = 200
        mock_commit_response.json.return_value = ['commit1', 'commit2']
        with patch('GitHubAPI.get_commit_count', return_value=2) as mock_commit_count:
            # Testing the function for repositories
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                get_repos("testuser")
                output = mock_stdout.getvalue().strip()
                self.assertIn("Repo: repo1 Number of commits: 2", output)
                self.assertIn("Repo: repo2 Number of commits: 2", output)

    # Testing as if fetching the repos failed
    @patch('requests.get')
    def test_get_repos_failure(self, mock_get):
        # Mocking the failure response for repositories
        mock_repo_response = Mock()
        mock_repo_response.status_code = 404  # Simulating an error response (not found)
        mock_get.return_value = mock_repo_response
        
        # Testing the function when the repositories fetch fails
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            get_repos("testuser")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "Failed to fetch data for GitHub user 'testuser'. Status code: 404")