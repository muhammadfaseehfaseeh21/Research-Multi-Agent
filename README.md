# 🔬 Research Multi-Agent Team

An AI-powered research team built with CrewAI, Groq and Streamlit.

## 🤖 Agents

### 🔎 Researcher
Finds relevant information and evidence.

### ✅ Fact Checker
Verifies important claims using web research.

### 📊 Research Analyst
Analyzes verified information and identifies insights.

### 📝 Report Writer
Creates the final structured research report.

## 🛠️ Technology

- CrewAI
- Groq
- openai/gpt-oss-120b
- Streamlit
- Groq Browser Search

## 🔄 Workflow

User Topic

↓

Researcher

↓

Fact Checker

↓

Research Analyst

↓

Report Writer

↓

Final Research Report

## 🔐 API Key

The application requires:

GROQ_API_KEY

For Streamlit deployment, add the key through Streamlit Secrets.

Do not upload API keys to GitHub.

## 📁 Project Structure

research-multi-agent/

├── app.py
├── crew.py
├── tools.py
├── researcher.py
├── fact_checker.py
├── analyst.py
├── report_writer.py
├── requirements.txt
├── README.md
└── .gitignore

## 🚀 Deployment

The application can be deployed through Streamlit Community Cloud using a GitHub repository.

## 📌 Model

openai/gpt-oss-120b
