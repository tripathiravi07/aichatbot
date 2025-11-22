# 🤖 DevOps Q&A Chatbot 🚀

An interactive **Streamlit** app powered by **LangChain** and **Groq** that acts as a DevOps expert.  
Ask any DevOps-related question (CI/CD, Kubernetes, Terraform, cloud, monitoring, etc.) and get contextual, chat-style answers with conversation history.

---

## 🧩 Features

- 💬 **DevOps Expert Chatbot** – System prompt is tuned to answer DevOps-focused questions.
- 🧠 **Conversation Memory** – Uses `ChatMessageHistory` + `RunnableWithMessageHistory` to maintain chat history per session.
- ✂️ **Smart Message Trimming** – Older messages are trimmed using `trim_messages` to stay within token limits.
- 🔑 **Secure API Key Input** – Enter your **GROQ API key** safely via Streamlit sidebar.
- 🧹 **Clear History Button** – Clear stored chat history for the current session with one click.
- 🖥️ **Simple UI** – Built with Streamlit for quick local use and easy customization.

---

## 🏗️ Tech Stack

- Python (3.9+ recommended)
- Streamlit
- LangChain
  - `langchain-groq`
  - `langchain-core`
  - `langchain-community`
- Groq LLM (`openai/gpt-oss-20b`)
- python-dotenv

---

## 📂 Project Structure

```bash
.
├── app_self.py        # Streamlit application (main app code)
├── .env               # Optional: store GROQ_API_KEY here
├── requirements.txt   # Python dependencies
└── README.md          # This file
---
🛠️ Installation & Running Instructions

✅ Step 1 — Install All Dependencies
```
pip install -r requirements.txt
```
---
✅ Step 2 — Run the Streamlit App
```
streamlit run app_self.py
```
