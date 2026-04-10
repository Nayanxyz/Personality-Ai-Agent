# 🍎 Principia: The Isaac Newton AI Agent

An interactive, persona-driven artificial intelligence agent designed to emulate the analytical rigor, historical context, and distinct temperament of Sir Isaac Newton. Built with Python and LangChain, this agent processes user queries through the lens of classical mechanics, calculus, and 17th-century natural philosophy, delivered via a responsive Gradio web interface.

## 🧠 Engineering Architecture
* **Core Logic (LLM Framework):** Powered by LangChain, utilizing custom prompt templates to enforce strict persona boundaries, ensuring the agent remains historically accurate and computationally rigorous.
* **Memory Management:** Implements conversational buffer memory to allow for multi-turn mathematical discourse and contextual follow-up questions.
* **Frontend Interface:** Deployed using Gradio for a lightweight, interactive, and easily shareable web-based chat UI.
* **State & Security:** Strict separation of configuration and code. LLM provider API keys are managed exclusively via environment variables to prevent cryptographic exposure.

