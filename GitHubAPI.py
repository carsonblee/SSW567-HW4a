# --------------------------------------------------------------------------------
# HW04a: Github RESTful API
# # @author Carson Lee
# Date: 27 February 2025
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# --------------------------------------------------------------------------------
import requests
import json

def get_commit_count(github_id, repo_name):
    commit_url = f"https://api.github.com/repos/{github_id}/{repo_name}/commits"
    commitResponse = requests.get(commit_url)
    
    if commitResponse.status_code == 200:
        commits = commitResponse.json()
        return len(commits)
    else:
        print(f"Failed to fetch commits for repository '{repo_name}'. Status code: {commitResponse.status_code}")
        return 0

def get_repos(github_id):
    repo_url = f"https://api.github.com/users/{github_id}/repos"
    repoResponse = requests.get(repo_url)
    
    if repoResponse.status_code == 200:
        repos = repoResponse.json()
        if repos:
            for repo in repos:
                repoName = repo['name']
                commitCount = get_commit_count(github_id, repoName)
                print(f"Repo: {repoName} Number of commits: {commitCount}")
        else:
            print(f"No repositories found for GitHub user '{github_id}'.")
    else:
        print(f"Failed to fetch data for GitHub user '{github_id}'. Status code: {repoResponse.status_code}")

if __name__ == "__main__":
    github_id = input("Enter GitHub ID: ")
    get_repos(github_id)