# 🍎 Principia: The Isaac Newton AI Agent

An interactive, persona-driven artificial intelligence agent designed to emulate the analytical rigor, historical context, and distinct temperament of Sir Isaac Newton. Built with Python and LangChain, this agent processes user queries through the lens of classical mechanics, calculus, and 17th-century natural philosophy, delivered via a responsive Gradio web interface.

## 🧠 Engineering Architecture
* **Core Logic (LLM Framework):** Powered by LangChain, utilizing custom prompt templates to enforce strict persona boundaries, ensuring the agent remains historically accurate and computationally rigorous.
* **Memory Management:** Implements conversational buffer memory to allow for multi-turn mathematical discourse and contextual follow-up questions.
* **Frontend Interface:** Deployed using Gradio for a lightweight, interactive, and easily shareable web-based chat UI.
* **State & Security:** Strict separation of configuration and code. LLM provider API keys are managed exclusively via environment variables to prevent cryptographic exposure.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **AI/Orchestration:** LangChain
* **Interface:** Gradio
* **Environment Management:** `python-dotenv`

## 🚀 Installation & Execution

Follow these strict deployment protocols to run the agent locally.

### 1. Clone the Repository
```bash
git clone https://github.com/Nayanxyz/Personality-Ai-Agent.git
cd Personality-Ai-Agent
```
### 2. Install Dependencies
```bash
pip install langchain gradio
python-dotenv openai
```
### 3. Create a .env file in the root and paste
```bash
GEMINI_API_KEY=your_secure_api_key
```
### 4. Initialize the Agent
```bash
puthon main.py
```
