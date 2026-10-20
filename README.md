# 🧠 NPTEL Reinforcement Learning - Weekly Assignment Quiz App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://reinforcementlearningnptelweeklyassignmentquiz.streamlit.app/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Course](https://img.shields.io/badge/NPTEL-IIT%20Madras-orange.svg)](https://nptel.ac.in/courses/106106143)

An interactive, responsive web quiz application for **NPTEL Reinforcement Learning** (taught by **Prof. B. Ravindran, IIT Madras**). Built with Streamlit, custom CSS, and a sleek purple glassmorphism design.

👉 **Live Application**: **[reinforcementlearningnptelweeklyassignmentquiz.streamlit.app](https://reinforcementlearningnptelweeklyassignmentquiz.streamlit.app/)**

---

## 🌟 Key Features

- **📚 100% Verbatim Question Bank (219 Total Questions)**:
  - **2026 Assignments**: **113 Questions** (Weeks 1–12)
  - **2025 Assignments**: **106 Questions** (Weeks 1–12)
  - Every question prompt, mathematical formulation, Greek notation ($\epsilon, \delta, \gamma, \theta, \alpha, \lambda, \tau, \pi$), option list, and official solution explanation matches the official NPTEL PDFs with 100% fidelity.
- **📅 Dedicated Year Separation**:
  - Filter by **2026 assignments**, **2025 assignments**, or attempt a **Mixed Quiz**.
- **🎯 Flexible Practice Modes**:
  - **Practice Mode**: Step-by-step instant feedback with the official detailed explanations upon selecting an answer.
  - **Quiz Mode**: Complete timed assessment mode with score breakdowns and detailed result reviews.
- **🎨 Modern Glassmorphism UI**:
  - Custom purple color palette (`#6C5CE7`) matching modern design aesthetics.
  - Seamless **Dark & Light Mode** toggle in the sidebar.
  - Fully responsive across desktop, tablet, and mobile screens.
- **🔢 Strict Sequential Question Order**:
  - Preserves exact 1..10 question order for weekly assignments without random shuffling.

---

## 📊 Course Syllabus & Question Bank Breakdown

| Week | Topic / Title | 2026 Qs | 2025 Qs | Total |
| :---: | :--- | :---: | :---: | :---: |
| **01** | Introduction to RL & Multi-Armed Bandits | 10 | 10 | 20 |
| **02** | Advanced Bandit Algorithms (UCB, Thompson Sampling, PAC) | 10 | 10 | 20 |
| **03** | Policy Gradient & Contextual Bandits | 10 | 10 | 20 |
| **04** | MDPs, Bellman Equations & Value Functions | 10 | 10 | 20 |
| **05** | Dynamic Programming & Monte Carlo Methods | 8 | 10 | 18 |
| **06** | TD Learning, SARSA & Q-Learning | 10 | 10 | 20 |
| **07** | Eligibility Traces & n-Step Methods | 10 | 10 | 20 |
| **08** | Function Approximation & LSTD | 10 | 8 | 18 |
| **09** | DQN, Actor-Critic & Policy Gradient Methods | 10 | 8 | 18 |
| **10** | SMDPs, Options & Hierarchical RL | 10 | 8 | 18 |
| **11** | MAXQ & Hierarchical Decomposition | 10 | 6 | 16 |
| **12** | Partial Observability & POMDPs | 5 | 6 | 11 |
| **Total** | **All 12 Weeks** | **113** | **106** | **219** |

---

## 📂 Repository Structure

```
├── app.py                  # Main Streamlit web application
├── questions.py            # Complete 219 question bank (2026 & 2025)
├── requirements.txt        # Python dependencies (streamlit>=1.40.0)
├── README.md               # Documentation & live demo link
├── .gitignore              # Clean ignore rules
├── .streamlit/
│   └── config.toml         # Custom theme configuration
├── 2026/                   # Official 2026 assignment solution PDFs
├── 2025/                   # Official 2025 assignment solution PDFs
└── extracted/              # Cleaned text transcriptions for verification
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

## 🌐 Live Deployment

The app is deployed on **Streamlit Community Cloud**:
🔗 **[https://reinforcementlearningnptelweeklyassignmentquiz.streamlit.app/](https://reinforcementlearningnptelweeklyassignmentquiz.streamlit.app/)**
