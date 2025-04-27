# 📄 Market Research & Use Case Generation Multi-Agent System

## 🚀 Project Overview

This project builds a **Multi-Agent System** that performs:
- **Market Research**: Understands the company's industry and focus areas.
- **Use Case Generation**: Proposes AI, ML, and GenAI use cases tailored to the industry.
- **Resource Collection**: Provides datasets and references to help implement the solutions.

The solution is deployed using **Streamlit** for an interactive experience.

---

## 🏗️ Project Structure

```
instaresz-assignment/
├── agents/
│   ├── research_agent.py        # Researches company and industry information
│   ├── market_standards_agent.py # Analyzes market trends and generates use cases
│   └── resource_asset_agent.py   # Finds datasets/resources for use cases
├── outputs/
│   └── resource_assets.md        # Collected datasets and references
├── app.py                        # Streamlit app to run the system
├── main.py                       # Backend script to run the agents together
├── README.md                     # This file
└── requirements.txt              # Required Python packages
```

---

## 🧠 Multi-Agent System Flow

1. **Research Agent**:
   - Uses web search to understand the industry and key offerings of a company.
2. **Market Standards Agent**:
   - Extracts short, pinpointed use cases related to AI, ML, and GenAI.
3. **Resource Asset Agent**:
   - Fetches datasets/resources to support the generated use cases.

➡️ **All findings are compiled into clean outputs, with clickable references.**

---

## 🛠️ Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/instaresz-assignment.git
cd instaresz-assignment
```

### 2. Install required packages
```bash
pip install -r requirements.txt
```

If you face errors like "No module named streamlit" or "No module named googlesearch-python", install manually:

```bash
pip install streamlit googlesearch-python beautifulsoup4 requests
```

---

## 🚀 Running the Project

### 1. Streamlit App (Recommended)

```bash
streamlit run app.py
```

It will open a browser window at `http://localhost:8501`.

### 2. Direct Script (Backend only)

```bash
python main.py
```

Outputs will be saved under the `outputs/` folder.

---

## 🖥️ Architecture Flowchart

*(Attach your flowchart image or describe as text)*

```
User Input (Company/Industry)
    ↓
Research Agent --> Industry Info + Key Offerings
    ↓
Market Standards Agent --> AI/GenAI Use Cases
    ↓
Resource Asset Agent --> Datasets/References
    ↓
Final Output --> Use Cases + Datasets
```

*(You can create a diagram in Lucidchart, Excalidraw, or any tool and show it in your demo.)*

---

## 📚 Example Outputs

- **Company**: XYZ Retail Pvt Ltd
- **Industry**: Retail
- **Key Offerings**: E-commerce, Supply Chain, Customer Experience
- **Generated Use Cases**:
  - AI-based personalized recommendations
  - GenAI-powered customer chatbots
  - Predictive demand analytics using ML
- **Resources**:
  - [Retail Product Dataset - Kaggle](https://www.kaggle.com/)

---

## ✨ Bonus Features

- ✅ Short, clear, professional use cases (not paragraphs)
- ✅ Handles fallback scenarios if scraping fails
- ✅ Streamlit-based easy demo
- ✅ Resource asset file auto-generated

---

## 📋 Deliverables Checklist

| Deliverable        | Status |
|--------------------|--------|
| Source Code        | ✅ Done |
| Final Report (.md) | ✅ Done |
| Architecture Flow  | ✅ Included |
| Demo Video         | 🎥 To be recorded after Streamlit app is tested |

---

## ✍️ Author

- **Vikash Shakya**  

---

# 📢 Note:

> Make sure your demo video shows the architecture diagram and the working app clearly!
```

---

✅ This is now perfectly formatted for a `.md` file. Just create a new `README.md`, **paste this**, and you're good to go!

---
  
Would you also like a ready-made `requirements.txt` too so you don’t miss anything when you submit? 🚀  
Just say **"yes, send requirements"** if you want it! 📦
