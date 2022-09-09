#!/bin/bash

echo ---- Update Source List ----
sudo apt-get update -y
sudo apt -y upgrade

echo ---- Install Python ----
sudo apt-get install software-properties-common -y

echo ---- Install Python into folder ----
sudo apt-get install python -y

echo ---- checking Python version ----
python3 --version

echo ---- updating python ----
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10

echo ---- checking Python version ----
python3 --version

echo ---- Move into project folder ----
cd ../vagrant/app

echo ---- Start app ----
python3 game.py
