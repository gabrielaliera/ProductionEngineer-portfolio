#! /usr/bin/env bash

# Kill existing tmux sessions
tmux kill-server

# Navigate to project folder
cd ProductionEngineer-portfolio

# Fetch latest changes from GitHub and reset to origin/main
git fetch && git reset origin/main --hard

# Activate Python virtual environment and install dependencies
source python3-virutalenv/bin/activate
pip install -r requirements.txt

# Start Flask server in a new detached tmux session
# tmux new-session -d -s flask-session 'cd ProductionEngineer-portfolio && source python3-virutalenv/bin/activate && flask run --host=0.0.0.0'
tmux new-session -d -s flask-session 'flask run --host=0.0.0.0'