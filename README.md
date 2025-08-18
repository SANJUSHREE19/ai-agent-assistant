# 🤖 Autonomous AI Agent Assistant

A modular, tool-augmented AI agent powered by Hugging Face models. This assistant can reason using LLMs, search the web, perform calculations, schedule meetings, and send emails — all from natural language input.

---

## 🚀 Features

- 🧠 Uses free Hugging Face models (no OpenAI quota required)
- 🔍 Real-time web search with DuckDuckGo
- 🧮 Custom calculator tool
- 📅 Google Calendar integration
- 📧 Simulated email sending
- 🧠 Memory system with ChromaDB (vector search)
- 🎨 Streamlit frontend for simple UI
- ☁️ Deployable on AWS EC2
- 🔐 Secure `.env` setup (no secrets in repo)

---

## 📂 Project Structure

ai-agent-assistant/
├── app.py # Streamlit UI
├── main.py # AI agent logic
├── .env # API keys (not pushed)
├── tools/
│ ├── calculator_tool.py
│ ├── calendar_tool.py
│ ├── email_tool.py
│ └── voice_input.py
├── requirements.txt
└── README.md 

---

## 🔑 .env Configuration

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
SERPAPI_API_KEY=your_serpapi_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
🔒 Make sure .env and any client_secret_*.json files are listed in your .gitignore file.

🧠 Tech Stack
Layer	Tool/Library
LLM	Hugging Face Hub (falcon, flan)
Tools	LangChain Tool Interface
Web Search	DuckDuckGoSearchRun (LangChain)
Embeddings	sentence-transformers (MiniLM)
Memory	ChromaDB
Frontend UI	Streamlit
Deployment	GitHub + AWS EC2

🖥️ Running Locally
git clone https://github.com/SANJUSHREE19/ai-agent-assistant.git
cd ai-agent-assistant

python -m venv venv
venv\Scripts\activate        # On Windows
# source venv/bin/activate   # On macOS/Linux

pip install -r requirements.txt
streamlit run app.py
Visit your app at: http://localhost:8501

☁️ Deployment Options
✅ AWS EC2 (Streamlit + Python)

✅ Streamlit Community Cloud

✅ Optional Docker container for portability

📘 License
This project is for academic and personal learning purposes. Do not publish any API keys or secrets.

🙋‍♀️ Author
Sanjushree Golla
GitHub: @SANJUSHREE19

---

✅ Academic Report (DOCX or PDF)?

✅ Final-Year Presentation PPT?

✅ Help deploying to AWS EC2?

Let’s wrap it up strong! 💪
