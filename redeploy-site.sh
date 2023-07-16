#! /usr/bin/env bash

#No longer using, updated with adding to systemctl
#Kill existing tmux sessions #tmux kill-server

# Navigate to project folder
cd ProductionEngineer-portfolio

# Fetch latest changes from GitHub and reset to origin/main
git fetch && git reset origin/main --hard

# Activate Python virtual environment and install dependencies
source python3-virutalenv/bin/activate
pip install -r requirements.txt

#No longer using, updated with adding to systemctl
# Start Flask server in a new detached tmux session
#tmux new-session -d -s flask-session 'flask run --host=0.0.0.0'