# Python Projects: 

# Task Tracker: 
https://roadmap.sh/projects/task-tracker

Task Tracker is a simple command-line interface (CLI) application that helps you track and manage tasks.
## Features
- Add, update, and delete tasks
- Mark tasks as "In Progress" or "Done"
- List all tasks
- Filter tasks by status: done, not done, in progress

## Requirements
- Add, update, and delete tasks
- List tasks by their status (all, done, in progress, not done)

## How to Run

1. **Clone the repository**:
   git clone https://github.com/DikeH-Ai/Python-projects.git
   
   cd Python-projects/

2. **Make the script executable**:
    chmod +x task-tracker.py

3. **Run the task tracker**:
    ./task-tracker --help

4. **Add a Task**:
    ./task-tracker add "Buy groceries"

5. **Update a Task**:
    ./task-tracker update 1 "Finish Python project"

6. **Delete a Task**:
    ./task-tracker delete 1

7. **List All Tasks**:
    ./task-tracker list --all

8. **List Completed Tasks**:
    ./task-tracker list --done


# Github Yser Activity CLI:
https://roadmap.sh/projects/github-user-activity

Github User Activity is a simple CLI tool for monitoring specific user activities.

## Feature
- Prouduce a user friendly output for each of these events:
    - Starred Repositories (WatchEvent)
    - Pushes (PushEvent)
    - Forks (ForkEvent)
    - Pull Requests (PullRequestEvent)
    - Issues (IssueEvent)
    - Issue Comments (IssueCommentEvent)

## Requirements
- Provide the GitHub username as an argument when running the CLI.
- Fetch the recent activity of the specified GitHub user using the GitHub API.
- Display the fetched activity in the terminal.

## How to Run

1. **Clone the repository**:
   git clone https://github.com/DikeH-Ai/Python-projects.git

- **Optional**:
    - make file executable
    chmod +x github-usr-activity.py

2. **Run file**
    - option 1:
        - pass CLI argument
        python github-usr-activity.py <username>
        
        - pass argument within file operation
        python github-usr-activity.py
