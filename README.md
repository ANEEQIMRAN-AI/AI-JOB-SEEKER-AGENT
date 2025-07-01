# 🤖 JOB SEARCHER AI — Automated CV-Based Job Hunting Agent

A fully automated AI agent built with **LangChain**, **LangGraph**, **Streamlit**, and **Twilio**, that takes your **CV (PDF)** as input, intelligently parses it, finds **matching job listings from LinkedIn**, and sends them directly to your **WhatsApp**.

> 🎯 “Upload your CV. Get jobs. Instantly. Anywhere.”

---

## 🚀 Features

- 📄 **CV Parsing** — Extracts your job title and skills automatically from a PDF resume.
- 🔍 **Live LinkedIn Scraping** — Searches LinkedIn in real-time for jobs that match your profile.
- 📬 **WhatsApp Notifications** — Sends matching jobs to your WhatsApp using Twilio.
- 🤖 **LangGraph Agent Workflow** — Fully modular graph-based pipeline with nodes for CV parsing, job search, and messaging.
- 🧠 **Skill Matching** — Identifies relevant technologies (Python, ML, AI, etc.) to tailor job queries.
- ⚡ **1-Click Streamlit UI** — Clean web interface to upload your CV and launch the agent.

---

## 🧠 Tech Stack

| Tool        | Purpose                                      |
|-------------|----------------------------------------------|
| 🦜 LangChain | Language modeling & pipeline orchestration   |
| 🧩 LangGraph | Multi-agent execution and state transitions  |
| 🐍 Python    | Core backend logic                           |
| 🕸 Selenium  | Real-time LinkedIn job scraping              |
| 🧾 PyMuPDF   | PDF parsing and text extraction              |
| 🌐 Streamlit | Interactive web UI for file upload           |
| 💬 Twilio    | WhatsApp API integration                     |
| 🔐 dotenv    | Secure API key and credentials management    |

---

## 📦 Installation

```bash
git clone https://github.com/your-username/JOB-SEARCHER-AI.git
cd JOB-SEARCHER-AI
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔐 Setup `.env`

Create a `.env` file in the root directory:

```env
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
USER_WHATSAPP_TO=whatsapp:+92xxxxxxxxxx
```

> ⚠️ Join Twilio Sandbox by sending the keyword to `+14155238886` via WhatsApp (see [docs](https://www.twilio.com/docs/whatsapp/sandbox)).

---

## 🚦 Usage

```bash
streamlit run main.py
```

Then:

1. Upload your **PDF CV**
2. Click **“Start Job Search”**
3. Check your **WhatsApp** for job listings 📱

---

## 📁 Folder Structure

```
JOB-SEARCHER/
│
├── main.py                # Streamlit app
├── graph.py               # LangGraph agent
├── cv_parser.py           # CV text extraction + skill matching
├── linkedin_scraper.py    # Job scraping via Selenium
├── notify_agent.py        # WhatsApp message sender via Twilio
├── .env                   # API keys & phone config
```

---

## ✅ Example Output (WhatsApp)

```
🧠 Jobs Matched to Your CV:

🔹 Machine Learning Engineer at Google
📍 Mountain View, CA
🔗 https://linkedin.com/jobs/view/...

🔹 Data Scientist at Meta
📍 Remote
🔗 https://linkedin.com/jobs/view/...
```

---

## ✨ Future Upgrades

- 📍 Location-based filtering
- 🧾 Export job results to PDF
- ⏱️ Scheduled daily/weekly job scans
- 📧 Email fallback for job results
- 🗣️ Chat-based interface

---

## 🙋‍♂️ Author

Repo by [ANEEQ IMRAN](https://github.com/ANEEQIMRAN-AI)

---



If you found this useful:

- 🌟 Star the repo
- 🍴 Fork it
- 🧵 Share with friends
