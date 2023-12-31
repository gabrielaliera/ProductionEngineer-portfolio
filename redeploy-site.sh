#! /usr/bin/env bash

# Navigate to project folder
cd ProductionEngineer-portfolio

# Fetch latest changes from GitHub and reset to origin/main
git fetch && git reset origin/main --hard

# Spin containers down to prevent out of memory issues on our VPS instances
docker compose -f docker-compose.prod.yml down

#Rebuild image incase of changes
docker compose -f docker-compose.prod.yml up --build
#Spin up containers
docker compose -f docker-compose.prod.yml up -d
