# 🏡 AI Property Recommendation System

### 🚀 Overview
The **AI Property Recommendation System** is an intelligent property discovery platform that allows users to search for real estate projects using **natural language queries** instead of complex filters.

Users can type queries like:
> “3BHK flat in Pune under ₹1.2 Cr”  
> “Ready-to-move apartments in Mumbai”  
> “Projects near Hinjewadi under 80 lakh”

The system understands the intent behind the query, extracts important filters such as **city, BHK, budget, and project status**, searches through the dataset, and displays the **best-matched property recommendations**.

---

## 🎯 Objective
To build a smart recommendation system that leverages **Natural Language Processing (NLP)** and **structured data filtering** to assist users in finding the most relevant real estate options — all based on their query in plain English.

---

## 🧩 Features
✅ Understands user intent through NLP  
✅ Extracts filters like **City, BHK, Budget, Status, and Locality**  
✅ Searches and recommends top matching projects from CSV data  
✅ Generates a short summary describing the search results  
✅ Interactive **Streamlit-based user interface**  
✅ Clean, minimal, and responsive design with **background visuals**  

---

## 🧠 NLP Capabilities
- Rule-based and regex-driven intent parsing  
- Detects:
  - **City** (e.g., Pune, Mumbai)
  - **BHK type** (e.g., 2BHK, 3BHK)
  - **Budget** (e.g., under ₹1.2 Cr / under 50 Lakh)
  - **Construction status** (Ready to move / Under construction)
  - **Locality** (e.g., Baner, Wakad, Kothrud)

---

## 🧰 Tech Stack

| Layer | Tools Used |
|:------|:------------|
| **Frontend / UI** | Streamlit, HTML/CSS Styling |
| **Backend / Logic** | Python (Regex-based NLP) |
| **Data Handling** | Pandas |
| **Data Source** | Project CSV files (`project.csv`, `ProjectAddress.csv`) |
| **Version Control** | Git, GitHub |

---

## 🗂️ Folder Structure

```
AI_Property_Recommendation_System/
│
├── app.py                     # Main Streamlit application file
├── project.csv                # Property/project dataset
├── ProjectAddress.csv         # Address-level dataset
├── Backgrounds-Flat-Design-HD.jpg  # Background image
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/AI_Property_Recommendation_System.git
cd AI_Property_Recommendation_System
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # For Windows
source venv/bin/activate   # For macOS/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app
```bash
streamlit run app.py
```

---

## 🧮 Example Queries
You can type natural queries like:

| Example Query | What Happens |
|----------------|---------------|
| `3BHK in Pune under 80 lakh` | Filters for 3BHK flats in Pune below ₹80 lakh |
| `Ready to move projects in Mumbai` | Shows ready projects in Mumbai |
| `Under construction flats in Baner` | Shows under-construction properties in Baner |

---

## 🧾 Output Summary Example

> **Found 6 matching 3BHK projects in Pune.**  
> Most are located in Baner and Wakad.  
> 4 are ready-to-move and 2 are under construction.

---

## 📈 Future Enhancements
- Add **semantic search** using embeddings (Sentence Transformers)
- Integrate **LLM-based summarization**
- Deploy on **Streamlit Cloud / Hugging Face Spaces**
- Add **voice-based query input**

---

## 👨‍💻 Developer

**👤 Aditya Ware**  
*AI & Data Science Graduate*  
📍 Pune, India  
💼 Passionate about AI, NLP, and Data Analytics  
📧 [adityaware@example.com](mailto:adityaware@example.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/adityaware) • [GitHub](https://github.com/adityaware)

---

## 🏁 License
This project is open-source and available under the **MIT License**.

---

### ⭐ If you found this project useful, please give it a star on GitHub!
