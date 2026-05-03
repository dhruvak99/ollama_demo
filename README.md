# Ollama Workshop Guide

---

## Setup Anaconda (First)

Download Anaconda:  https://www.anaconda.com  

Create Environment  
`conda create -n ollama python=3.11 -y`

Activate Environment  
`conda activate ollama`  

---

## Setup Ollama

Download Ollama:  https://ollama.com  

Verify Installation  
`ollama --version`  

Ollama Models:  https://ollama.com/library

Run a Model  
`ollama run qwen3:4b`  

## NOTE: You should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models.

---

## Run Python Scripts

Install Dependency  
`pip install requests`  

Run Script  
`python ollama_local_chat_api.py`  

---

## Setup OpenWebUI

Project:  https://github.com/open-webui/open-webui  

Install  
`pip install open-webui`  

Run  
`open-webui serve`  

Open in Browser  http://localhost:8080  

---

## Configure OpenWebUI

Open Settings  
Set Ollama Base URL:  http://localhost:11434  

Select your model (e.g., qwen3:4b)  
Start chatting  

---

## RAM vs Model Size

Approximate RAM required for quantized models:

1B parameters ≈ 0.6 – 0.8 GB RAM  

Examples  

3B → 2 – 3 GB  
4B → 3 – 4 GB  
7B → 5 – 8 GB  
13B → 10 – 16 GB  
34B → 25 – 40 GB  
70B → 50 – 80 GB  

---

## Project Ideas

1. Resume–Job Match Analyzer  
2. AI Study Assistant  
3. Code Review & Debugging Tool  
4. Intelligent Log Analyzer  
5. Smart Email Composer  
6. Interview Preparation Assistant  
7. Personal Knowledge Chatbot  
8. Command Line Helper AI  
9. Startup Idea Generator  
10. AI Teaching Assistant  
11. Lecture & Meeting Summarizer  
12. Bug Report Generator  
13. Private Local ChatGPT System  
14. Data Insight Generator  
15. Code Documentation Generator  

---

## Done

You can now:

- Run models locally using Ollama  
- Use Python scripts to interact with them  
- Use a UI via OpenWebUI  

---
