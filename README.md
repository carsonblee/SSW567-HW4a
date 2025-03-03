# HW4c: GitHub API w/ New Testing
[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/YBMEBAqhQKNrvTPDbdRbap/Uzcx6xoX9zwJYNYQd7TPgS/tree/HW04c_Mocking.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/YBMEBAqhQKNrvTPDbdRbap/Uzcx6xoX9zwJYNYQd7TPgS/tree/HW04c_Mocking)

# Assignment
The last assignment was to write code to interface with an external REST-based APIs, in this case, GitHub. Building off of that, we are now using mocking to run dynamic tests that aren't dependent on values that might change, like number of commits in a repo. 

# Thought Process
One thing I found very hard was wrapping my mind around how to use mocking and patches to achieve the testing goal of skipping over the call-and-response from the API. While I understand why it's so useful, it was hard to comprehend in the moment. Once that obstacle was overcome, I broke up testing into two parts of two. First being split between the functions of `get_repos` and `get_commit_count` and then with the assumption that the API call succeeded or failed.