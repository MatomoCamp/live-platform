#!/bin/bash
set -x
set -e

python="/srv/live/venv/bin/python"

runpython="sudo -u live $python"

git pull

$python utils.py

sudo systemctl reload live.service
