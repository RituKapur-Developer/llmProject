# 🚀 Multi-Agent RAG API (FastAPI + LangGraph + Free LLMs)

A minimal, production-ready **Retrieval-Augmented Generation (RAG)** system using:

* FastAPI (API layer)
* LangGraph (multi-agent orchestration)
* SentenceTransformers (embeddings)
* Groq (LLM inference – fast & free tier)

---

## ✨ Features

* 🧠 Multi-agent workflow using LangGraph
* 🔍 RAG pipeline (retrieve + generate)
* ⚡ Fast inference via Groq
* 📦 Clean, minimal dependency setup (no TensorFlow conflicts)
* 🐳 Docker-ready

---

## 🏗️ Architecture

```
User Query
    ↓
FastAPI Endpoint (/query)
    ↓
LangGraph Agent Router
    ↓
Retriever (SentenceTransformers)
    ↓
LLM (Groq)
    ↓
Response
```

---

## 📂 Project Structure

```
app/
├── api.py        # FastAPI routes
├── agents.py     # LangGraph workflow
├── llm.py        # LLM routing (Groq)
├── rag.py        # Retrieval logic
├── config.py     # Environment + keys
```

---

## ⚙️ Setup (Local)

### 1. Clone repo

```bash
git clone https://github.com/RituKapur-Developer/llmProject.git
cd llmProject
```

---

### 2. Create environment (uv recommended)

```bash
pip install uv
uv venv
```

---

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

---

### 4. Add environment variables

Create `.env`:

```env
GROQ_API_KEY=your_key_here
HF_API_KEY=your_key_here
```

---

### 5. Run the API

```bash
uv run uvicorn app.api:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker Setup

### Build image

```bash
docker build -t rag-llm-app .
```

### Run container

```bash
docker run -p 8000:8000 --env-file .env rag-llm-app
```

---

## 🔑 Environment Variables

| Variable       | Description                  |
| -------------- | ---------------------------- |
| `GROQ_API_KEY` | Groq API key for LLM         |
| `HF_API_KEY`   | HuggingFace token (optional) |

---

## 🧪 Example Request

```bash
curl -X POST "http://127.0.0.1:8000/query" \
-H "Content-Type: application/json" \
-d '{"question": "What is RAG?"}'
```

---

## ⚠️ Notes

* This project uses **PyTorch only** (no TensorFlow)
* First run may download embedding models
* `.env` is ignored for security

---

## 📈 Future Improvements

* Add vector DB (FAISS / Chroma)
* Multi-LLM routing (Gemini, OpenAI, etc.)
* Streaming responses
* Evaluation pipeline

---

## 📜 License

MIT License

---

## 🙌 Acknowledgements

* LangGraph for agent orchestration
* SentenceTransformers for embeddings
* Groq for ultra-fast inference

---

## 👩‍💻 Author

**Ritu Khosla**

---

## ⭐ If you find this useful

Give it a star ⭐ — helps others discover it!
