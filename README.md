# RasaChatbot

# FinanceBot – Rasa-Powered Virtual Banking Assistant

## 💡 Overview
This assistant simulates a virtual banking experience using Rasa. It supports checking balances, transferring money, reporting lost cards, talking to a human agent, and more.

## ⚙️ Features
- Balance Inquiry
- Transaction History
- Money Transfer via Form
- Card Loss Reporting via Form
- Address & PIN Updates
- Fallback Handling
- Human Escalation

## 📁 Project Structure
- `data/` – NLU and stories
- `actions.py` – Custom action logic
- `domain.yml` – Intents, actions, responses
- `rules.yml` – Rule-based logic

## 🧪 Sample Test Phrases
- "I want to transfer $50 to Mike"
- "I lost my debit card"
- "Can I change my pin?"
- "Show me my recent transactions"

## 🚀 Run Locally
```bash
rasa train
rasa run actions &
rasa shell
