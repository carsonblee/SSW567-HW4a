"""
@author: Carson Lee
"""
import unittest
import GitHubAPI

class TestCommits(unittest.TestCase):

    def test_get_commit_count_success(self):
        self.assertEqual(GitHubAPI.get_commit_count("richkempinski", "Mocks"), 10) # This works dependant on Github's API

    def test_get_commit_count_failed(self):
        self.assertEqual(GitHubAPI.get_commit_count("richkempinski", "WAWAWAWA"), 0)

class TestRepos(unittest.TestCase):

    def test_get_repos_success(self):
        self.assertEqual(GitHubAPI.get_repos("richkempinski"), "Repo: csp Number of commits: 2\nRepo: hellogitworld Number of commits: 30\nRepo: helloworld Number of commits: 6\nRepo: Mocks Number of commits: 10\nRepo: Project1 Number of commits: 2\nRepo: richkempinski.github.io Number of commits: 9\nRepo: threads-of-life Number of commits: 1\nRepo: try_nbdev Number of commits: 2\nRepo: try_nbdev2 Number of commits: 5") # This works dependant on Github's API

    def test_get_repos_failed(self):
        self.assertEqual(GitHubAPI.get_repos("asdfghjkl"), "No repositories found for GitHub user 'asdfghjkl'.")