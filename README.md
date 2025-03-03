# HW4a: GitHub API
[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/YBMEBAqhQKNrvTPDbdRbap/Uzcx6xoX9zwJYNYQd7TPgS/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/YBMEBAqhQKNrvTPDbdRbap/Uzcx6xoX9zwJYNYQd7TPgS/tree/main)

# Assignment
The assignment was to write code to interface with an external REST-based APIs, in this case, GitHub. The goal for the assignment was to request a user's GitHub ID as the input and print their repositories and the corresponding number of commmits each repo had.

# Thought Process
My thought process started with the idea that this code should be broken up into two separate parts: fetching the repos and fetching the number of commits. Obviously, the more important step was to fetch the repos which was coded first as it lays the foundation for fetching the number of commits. Once that function was established and tested, able to fetch and print the repos of the user, I could move onto fetching the number of commits in each repo. Building into the loop that printed the repo names, I added a call to a new function that would also fetch the number of commits for that repo so the name and the number of commits could be printed at the same time on the same line.

By breaking the problem up into two distinct steps, I found it easier to conceptualize and code than doing it all at once. 
