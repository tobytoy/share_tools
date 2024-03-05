#!/bin/bash

# system
sudo apt update -y
sudo apt install -y neofetch
sudo apt upgrade -y

# python
# pip install -r requirements.txt
pip install jupyterlab streamlit gradio


# javascript
npm install -g localtunnel
npm install -g @vue/cli

# vue
cd ~
vue create project_vue

