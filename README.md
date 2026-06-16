# 🎓 Predictive Analysis of Gaming Habits on Academic Performance

## 🍗 Team: Chicken Tenders
* **Course:** BICS 2303 — Intelligent Systems (Section 05)  
* **Instructor:** Dr. Marini Binti Othman  
* **Institution:** International Islamic University Malaysia (IIUM)  

---

## 📌 Project Overview
This repository contains the complete implementation framework for our Intelligent Systems group project. The system utilizes an advanced **Random Forest Regressor** to predict a student's final continuous academic grade based on various intersecting daily lifestyle habits, gaming patterns, and cognitive index metrics. 

By evaluating an empirical baseline **Single Decision Tree** against our proposed **Random Forest Ensemble**, the project highlights the mathematical strength of ensemble learning models in reducing variance and mitigating overfitting on tabular datasets.

### 📊 Performance Summary
* **Proposed Random Forest $R^2$ Score:** `91.21%` (Explains over 91% of grade variance)
* **Proposed Random Forest RMSE:** `6.6385` grade points
* **Baseline Single Decision Tree $R^2$ Score:** `87.06%`

---

## 📂 Repository Structure
```text
📁 analysis_gaming_habit_to_academic/
├── 📄 app.py                     # Interactive Streamlit Web Application Interface
├── 📄 student_rf_model.sav       # Serialized 18-Feature Random Forest Trained Model
├── 📄 Gaming_Academic_Performance.csv  # Sourced Complete Student Tracking Dataset
├── 📄 requirements.txt           # Python Project Package Dependencies File
└── 📄 README.md                  # System Documentation and Execution Guide

```

# 🚀 Local Installation & Execution Guide

Follow this comprehensive, step-by-step walkthrough to configure your local machine dependencies and spin up the interactive performance application live:

### 📦 Prerequisite Environment Verification
Before initializing setup, ensure you have **Python 3.10 or higher** installed on your operating system. Verify your installation by opening your terminal (macOS/Linux) or Command Prompt (Windows) and running:
```bash
python --version
```
---

### 🛠️ Step-by-Step Deployment Instructions

### Step 1: Open Your System Terminal Environment

* **On Windows Platforms:** Press the `Windows Key`, type **cmd** (*Command Prompt*), and hit Enter.
* **On macOS / Linux Platforms:** Press `Command + Space`, type **Terminal**, and hit Enter.

### Step 2: Clone or Download the Workspace Files

Clone this version-controlled repository down to your local directory machine, then use the change directory command to enter the root project folder:

```bash
git clone [https://github.com/your-github-username/analysis_gaming_habit_to_academic.git](https://github.com/your-github-username/analysis_gaming_habit_to_academic.git)
cd analysis_gaming_habit_to_academic

```

*(Alternative: If you downloaded the project bundle as a `.zip` archive, extract the files to your desired folder location, open your terminal, and use `cd path/to/extracted/folder` to point to that directory).*

### Step 3: Install Package Infrastructure Dependencies

Install the required data frameworks and web server engines (`streamlit`, `pandas`, `numpy`, and `scikit-learn`) concurrently by pointing your package manager to the tracking file:

```bash
pip install -r requirements.txt

```

*💡 **System Note:** This automated installation sequence takes roughly 1–2 minutes to fetch, compile, and safely register the software environment layers behind the scenes.*

### Step 4: Launch the Streamlit Application Server Live

With your folder parameters matching the layout constraints, spin up the responsive web script engine by executing:

```bash
streamlit run app.py

```

---

### 🎈 Launch Notification & Verification

As soon as the engine initializes, the terminal will open local port allocations. **Your default web browser will automatically open a live webpage tab pointing directly to:**

```text
http://localhost:8501

```

From this local interface dashboard portal, your teammates and assessor can seamlessly browse the **Dashboard & Analysis** evaluation matrices or interactively test custom lifestyle metrics live via the **Predict Student Grade** portal!


