# 🧠 NPTEL Reinforcement Learning - Weekly Assignment Quiz App

An interactive, responsive web quiz application for **NPTEL Reinforcement Learning** (taught by **Prof. B. Ravindran, IIT Madras**). Built with Streamlit, Vanilla CSS, and modern purple glassmorphism styling.

---

## 🌟 Features

- **📚 100% Verbatim Question Bank**:
  - **2026 Assignments**: 113 Questions (Weeks 1–12)
  - **2025 Assignments**: 106 Questions (Weeks 1–12)
  - **Total**: 219 fully verified questions with complete mathematical derivations, Greek notation ($\epsilon, \delta, \gamma, \theta, \alpha, \lambda, \tau, \pi$), and official explanations.
- **📅 Year Filter & Practice Modes**:
  - Dedicated tabs to practice **2026 assignments**, **2025 assignments**, or a **Mixed Quiz**.
  - **Practice Mode**: Instant answer checking with step-by-step explanations.
  - **Quiz Mode**: Full assessment mode with score summary and analytics.
- **🎨 Sleek Modern UI**:
  - Cohesive purple design palette (`#6C5CE7`).
  - Seamless **Dark & Light Mode** toggle.
  - Fully responsive across desktop, tablet, and mobile browsers.
- **🔢 Sequential Accuracy**:
  - Preserves exact 1..10 assignment question order without shuffling for weekly practice.

---

## 📂 Project Structure

```
├── app.py                  # Main Streamlit web application
├── questions.py            # Comprehensive question bank (2026 & 2025)
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── config.toml         # Theme and UI styling configuration
├── 2026/                   # Official 2026 assignment solution PDFs
├── 2025/                   # Official 2025 assignment solution PDFs
└── extracted/              # Cleaned text extractions for audit & verification
```

---

## 🚀 Running Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shivamchoudhary62/Reinforcement_Learning_NPTEL_Weekly_Assignment_Quiz.git
   cd Reinforcement_Learning_NPTEL_Weekly_Assignment_Quiz
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the web application**:
   ```bash
   streamlit run app.py
   ```
   Open `http://localhost:8501` in your browser.

---

## ☁️ Deployment on Streamlit Community Cloud (Free)

1. Push your code to your GitHub repository:
   ```bash
   git add .
   git commit -m "Initial commit with verified 2025-2026 question bank"
   git branch -M main
   git remote add origin https://github.com/shivamchoudhary62/Reinforcement_Learning_NPTEL_Weekly_Assignment_Quiz.git
   git push -u origin main
   ```
2. Go to **[share.streamlit.io](https://share.streamlit.io)** and log in with your GitHub account.
3. Click **"New app"**.
4. Select your repository: `shivamchoudhary62/Reinforcement_Learning_NPTEL_Weekly_Assignment_Quiz`.
5. Set **Main file path** to `app.py`.
6. Click **"Deploy!"**.
