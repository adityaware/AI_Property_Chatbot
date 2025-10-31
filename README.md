# 🏡 AI Property Chatbot

### 🚀 Company: NoBrokerage.com  
### 👨‍💻 Developer: **Aditya Ware**  
### 💼 Role: AI Engineer Intern Task  

---

## 📖 Overview

**AI Property Chatbot** is an intelligent assistant that helps users discover real estate projects using **natural language queries** like:

> “3BHK flats in Pune under ₹1 crore”  
> “Ready-to-move apartments in Baner”  

This chatbot eliminates the need for manual filters — users can simply *ask* what they want, and the system automatically:
- Understands the query using NLP and Regex  
- Searches through project data from CSV files  
- Generates factual summaries and top property results  

---

## 🧠 Features

| Feature | Description |
|----------|--------------|
| **Natural Query Understanding** | Detects city, BHK type, price, and property status using Regex |
| **Data-Driven Search** | Retrieves results from structured CSV files |
| **Summarization Logic** | Generates factual responses from data only |
| **Chat-Based Interface** | Streamlit UI similar to ChatGPT |
| **Error Handling** | Friendly fallback when no results are found |

---

## 🏗️ Tech Stack

| Layer | Tools / Libraries |
|--------|-------------------|
| **Frontend** | Streamlit |
| **Backend** | Python |
| **Data Handling** | Pandas |
| **NLP Parsing** | Regex |
| **Storage** | CSV files |
| **Deployment (Optional)** | Streamlit Cloud |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/AI_Property_Chatbot.git
cd AI_Property_Chatbot
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Add Data Files
Create a `data` folder and add:
```
data/
 ├── project.csv
 └── ProjectAddress.csv
```

### 4️⃣ Run the App
```bash
streamlit run app.py
```

---

## 💬 Example Queries

Try typing:
- `3BHK flats in Pune under 50 lakh`
- `Ready-to-move apartments in Mumbai`
- `Under construction projects in Hinjewadi`
- `Standalone buildings in Pune`
- `Projects in Baner near IT Park`

---

## 🧩 Core Files

| File | Description |
|------|--------------|
| `app.py` | Main Streamlit app |
| `project.csv` | Project data |
| `ProjectAddress.csv` | Address and locality data |
| `requirements.txt` | Dependencies |
| `README.md` | Documentation file |

---

## 🧠 Evaluation Criteria (Company Task)

| Criteria | Weight |
|-----------|---------|
| Query Understanding | 30% |
| Result Accuracy | 25% |
| Summary Quality | 20% |
| Code Quality | 15% |
| UI/UX | 10% |

---

## 🎯 Future Scope
- Add semantic search (using embeddings)
- Integrate with a live database (e.g., PostgreSQL)
- Add map visualization for nearby areas
- Deploy publicly on Streamlit Cloud

---

## 👨‍💻 Developed By

**Aditya Ware**  
🎓 B.Tech in Artificial Intelligence and Data Science  
📧 your-email@example.com  
🔗 [https://github.com/your-username](https://github.com/your-username)

---
