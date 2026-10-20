import streamlit as st
import random
from datetime import datetime
from questions import QUIZ_DATA, WEEK_META

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NPTEL Reinforcement Learning Quiz",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE INITIALIZATION
# ─────────────────────────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "theme": "light",                  # Default to Light mode matching reference screenshots
        "current_page": "home",
        "selected_week": "Week 1",
        "selected_bank": "2026",           # "2026", "2025", or "mixed"
        "quiz_mode": "practice",           # "practice" (one by one) or "test" (all at once)
        "shuffled_questions": [],
        "current_question_idx": 0,
        "answers": {},
        "quiz_history": [],
        "mixed_years": ["2026", "2025"],
        "mixed_weeks": list(QUIZ_DATA.keys()),
        "mixed_mode": "practice",
        "mixed_count": 15,
        "results_data": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ─────────────────────────────────────────────────────────────────────────────
# CSS SYSTEM: PURPLE PALETTE & EXACT REFERENCE STYLING
# ─────────────────────────────────────────────────────────────────────────────
theme = st.session_state.theme

if theme == "light":
    css_vars = """
    :root {
        --app-bg: #F8F9FE;
        --sidebar-bg: #FFFFFF;
        --sidebar-border: #ECEAF8;
        --card-bg: #FFFFFF;
        --card-border: #ECEAF5;
        --card-shadow: 0 4px 16px rgba(108, 92, 231, 0.05);
        --text-main: #2D3748;
        --text-muted: #718096;
        --text-sub: #8F9BB3;
        --primary-purple: #6C5CE7;
        --primary-purple-hover: #5B48DF;
        --primary-gradient: linear-gradient(135deg, #705DE8 0%, #8774F8 50%, #9F8EFA 100%);
        --btn-gradient: linear-gradient(90deg, #6C5CE7 0%, #8A76FF 100%);
        --btn-hover-gradient: linear-gradient(90deg, #5B48DF 0%, #7662F0 100%);
        --notice-bg: #EEF2FF;
        --notice-border: #E0E7FF;
        --notice-text: #4338CA;
        --option-hover: #F8F7FF;
        --option-selected: #EDE9FE;
        --success-bg: #ECFDF5;
        --success-border: #A7F3D0;
        --success-text: #065F46;
        --error-bg: #FEF2F2;
        --error-border: #FECACA;
        --error-text: #991B1B;
    }
    """
else:
    css_vars = """
    :root {
        --app-bg: #0E101D;
        --sidebar-bg: #141728;
        --sidebar-border: rgba(108, 92, 231, 0.2);
        --card-bg: #1A1E33;
        --card-border: rgba(108, 92, 231, 0.25);
        --card-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        --text-main: #F1F3FF;
        --text-muted: #9CA3AF;
        --text-sub: #8B949E;
        --primary-purple: #8272F8;
        --primary-purple-hover: #6C5CE7;
        --primary-gradient: linear-gradient(135deg, #533FE4 0%, #6D59EC 50%, #8472F5 100%);
        --btn-gradient: linear-gradient(90deg, #6C5CE7 0%, #8A76FF 100%);
        --btn-hover-gradient: linear-gradient(90deg, #5B48DF 0%, #7662F0 100%);
        --notice-bg: rgba(108, 92, 231, 0.15);
        --notice-border: rgba(108, 92, 231, 0.3);
        --notice-text: #C4B5FD;
        --option-hover: #222742;
        --option-selected: rgba(108, 92, 231, 0.3);
        --success-bg: rgba(16, 185, 129, 0.15);
        --success-border: rgba(16, 185, 129, 0.35);
        --success-text: #34D399;
        --error-bg: rgba(239, 68, 68, 0.15);
        --error-border: rgba(239, 68, 68, 0.35);
        --error-text: #F87171;
    }
    """

css_static = """
* {
    box-sizing: border-box;
}

body, .stApp {
    background-color: var(--app-bg) !important;
    color: var(--text-main) !important;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
}

.main .block-container {
    max-width: 1040px !important;
    padding: 1.5rem 1.5rem 4rem !important;
}

section[data-testid="stSidebar"] {
    background-color: var(--sidebar-bg) !important;
    border-right: 1px solid var(--sidebar-border) !important;
}

section[data-testid="stSidebar"] *:not(button):not(button *):not([data-testid="baseButton-secondary"] *):not([data-testid="baseButton-primary"] *) {
    color: var(--text-main);
}

/* Sidebar Action Buttons Matching Screenshots: Center aligned with pure white text */
section[data-testid="stSidebar"] .stButton > button,
section[data-testid="stSidebar"] button[data-testid="baseButton-secondary"],
section[data-testid="stSidebar"] button[data-testid="baseButton-primary"],
section[data-testid="stSidebar"] button {
    background: var(--btn-gradient) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.65rem 1rem !important;
    font-size: 0.92rem !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 14px rgba(108, 92, 231, 0.22) !important;
    transition: all 0.2s ease !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
    margin-bottom: 0.3rem !important;
    width: 100% !important;
}

section[data-testid="stSidebar"] .stButton > button *,
section[data-testid="stSidebar"] button * {
    color: #FFFFFF !important;
    text-align: center !important;
    justify-content: center !important;
    align-items: center !important;
}

section[data-testid="stSidebar"] .stButton > button p,
section[data-testid="stSidebar"] button p,
section[data-testid="stSidebar"] .stButton > button div,
section[data-testid="stSidebar"] button div,
section[data-testid="stSidebar"] .stButton > button span,
section[data-testid="stSidebar"] button span {
    color: #FFFFFF !important;
    text-align: center !important;
    justify-content: center !important;
    margin: 0 auto !important;
    width: 100% !important;
    display: flex !important;
}

section[data-testid="stSidebar"] .stButton > button:hover,
section[data-testid="stSidebar"] button:hover {
    background: var(--btn-hover-gradient) !important;
    box-shadow: 0 6px 18px rgba(108, 92, 231, 0.35) !important;
    transform: translateY(-1px) !important;
    color: #FFFFFF !important;
}

section[data-testid="stSidebar"] .stButton > button:hover *,
section[data-testid="stSidebar"] button:hover * {
    color: #FFFFFF !important;
}

/* Main Area Primary Buttons */
.stButton > button {
    background: var(--btn-gradient) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    padding: 0.65rem 1.4rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 3px 12px rgba(108, 92, 231, 0.2) !important;
}

.stButton > button:hover {
    background: var(--btn-hover-gradient) !important;
    box-shadow: 0 6px 18px rgba(108, 92, 231, 0.32) !important;
    transform: translateY(-1px) !important;
    color: #FFFFFF !important;
}

/* Radio Options Matching Reference App */
.stRadio > div {
    gap: 0.75rem !important;
}

.stRadio > div > label {
    background: transparent !important;
    border: none !important;
    padding: 0.45rem 0.6rem !important;
    color: var(--text-main) !important;
    font-size: 0.96rem !important;
    font-weight: 500 !important;
    line-height: 1.5 !important;
    cursor: pointer !important;
}

.stRadio > div > label p, .stRadio > div > label span {
    color: var(--text-main) !important;
    font-size: 0.96rem !important;
}

/* Top Hero Banner (Exact match to Screenshots 1 & 2) */
.hero-banner {
    background: var(--primary-gradient);
    border-radius: 18px;
    padding: 2.5rem 2rem 2.25rem;
    text-align: center;
    color: #FFFFFF;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 30px rgba(108, 92, 231, 0.25);
}

.hero-title {
    font-size: 2.15rem;
    font-weight: 800;
    color: #FFFFFF;
    margin-bottom: 0.5rem;
    line-height: 1.25;
}

.hero-sub {
    color: rgba(255, 255, 255, 0.92);
    font-size: 0.98rem;
    max-width: 720px;
    margin: 0 auto 1.25rem;
    line-height: 1.55;
}

.hero-pill-btn {
    display: inline-flex;
    align-items: center;
    background: rgba(255, 255, 255, 0.22);
    border: 1px solid rgba(255, 255, 255, 0.35);
    color: #FFFFFF !important;
    padding: 0.45rem 1.25rem;
    border-radius: 99px;
    font-size: 0.85rem;
    font-weight: 600;
    text-decoration: none !important;
    backdrop-filter: blur(8px);
    transition: background 0.2s ease;
}

.hero-pill-btn:hover {
    background: rgba(255, 255, 255, 0.32);
}

/* Stats Cards (4 on Home, 3 on Week) */
.stat-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 14px;
    padding: 1.35rem 1rem;
    text-align: center;
    box-shadow: var(--card-shadow);
}

.stat-number {
    font-size: 2.2rem;
    font-weight: 800;
    color: var(--primary-purple);
    line-height: 1;
}

.stat-label {
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--text-sub);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 0.45rem;
}

/* Notice Strip (Question Bank Indicator) */
.notice-strip {
    background: var(--notice-bg);
    border: 1px solid var(--notice-border);
    border-radius: 10px;
    padding: 0.75rem 1.25rem;
    color: var(--notice-text);
    font-size: 0.92rem;
    font-weight: 600;
    margin: 1.25rem 0 1rem;
}

/* Mode Choice Cards (Practice Mode & Test Mode) */
.mode-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 16px;
    padding: 1.75rem 1.5rem 1.25rem;
    box-shadow: var(--card-shadow);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 220px;
}

.mode-icon {
    font-size: 2rem;
    margin-bottom: 0.6rem;
}

.mode-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 0.4rem;
}

.mode-desc {
    font-size: 0.9rem;
    color: var(--text-muted);
    line-height: 1.5;
    margin-bottom: 1.25rem;
}

/* Question Container (Screenshot 3 & 4) */
.q-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    margin: 1.25rem 0 0.85rem;
    box-shadow: var(--card-shadow);
    display: flex;
    align-items: flex-start;
}

.q-badge {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: var(--primary-purple);
    color: #FFFFFF;
    font-weight: 700;
    font-size: 0.85rem;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 0.85rem;
    flex-shrink: 0;
    margin-top: 2px;
}

.q-text {
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--text-main);
    line-height: 1.55;
    white-space: pre-line;
}

/* Mixed Quiz Promo Card */
.mixed-promo-card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 14px;
    padding: 1.25rem 1.5rem;
    box-shadow: var(--card-shadow);
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

/* Progress bar */
.stProgress > div > div > div > div {
    background: var(--primary-purple) !important;
}

/* Feedback Alert Boxes */
.feedback-box-correct {
    background: var(--success-bg);
    border: 1px solid var(--success-border);
    border-radius: 10px;
    padding: 0.9rem 1.25rem;
    margin-top: 1rem;
    color: var(--success-text);
    font-weight: 600;
    font-size: 0.95rem;
}

.feedback-box-incorrect {
    background: var(--error-bg);
    border: 1px solid var(--error-border);
    border-radius: 10px;
    padding: 0.9rem 1.25rem;
    margin-top: 1rem;
    color: var(--error-text);
    font-size: 0.95rem;
}

.feedback-explanation {
    background: var(--notice-bg);
    border-left: 3px solid var(--primary-purple);
    border-radius: 8px;
    padding: 0.9rem 1.25rem;
    margin-top: 0.75rem;
    color: var(--text-main);
    font-size: 0.92rem;
    line-height: 1.55;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .main .block-container {
        padding: 1rem 0.75rem 3rem !important;
    }
    .hero-title {
        font-size: 1.6rem !important;
    }
    .q-card {
        padding: 1.15rem 1rem !important;
    }
}
"""

st.markdown("<style>" + css_vars + "\n" + css_static + "</style>", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def get_questions_for_week(week_key, bank_choice):
    wd = QUIZ_DATA.get(week_key, {})
    if bank_choice == "2026":
        return wd.get("2026", [])
    elif bank_choice == "2025":
        return wd.get("2025", [])
    elif bank_choice == "mixed":
        return wd.get("mixed", [])
    return []

def start_quiz(week_key, bank_choice, mode):
    raw_qs = get_questions_for_week(week_key, bank_choice)
    qs = [dict(q) for q in raw_qs]
    # Keep exact sequential order of the assignment PDF for weekly quizzes
    st.session_state.shuffled_questions = qs
    st.session_state.selected_week = week_key
    st.session_state.selected_bank = bank_choice
    st.session_state.quiz_mode = mode
    st.session_state.current_question_idx = 0
    st.session_state.answers = {}
    st.session_state.current_page = "quiz"

def start_custom_mixed(years, selected_weeks, count, mode):
    collected = []
    for wk in selected_weeks:
        wd = QUIZ_DATA.get(wk, {})
        if "2026" in years:
            for q in wd.get("2026", []):
                qc = dict(q)
                qc["src_week"] = wk
                qc["src_year"] = "2026"
                collected.append(qc)
        if "2025" in years:
            for q in wd.get("2025", []):
                qc = dict(q)
                qc["src_week"] = wk
                qc["src_year"] = "2025"
                collected.append(qc)
    random.shuffle(collected)
    n = min(count, len(collected))
    st.session_state.shuffled_questions = collected[:n]
    st.session_state.selected_week = "Mixed Quiz"
    st.session_state.selected_bank = "mixed"
    st.session_state.quiz_mode = mode
    st.session_state.current_question_idx = 0
    st.session_state.answers = {}
    st.session_state.current_page = "quiz"

def record_quiz_attempt(week_name, bank_name, mode_name, score, total, pct):
    st.session_state.quiz_history.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "week": week_name,
        "bank": bank_name,
        "mode": mode_name,
        "score": score,
        "total": total,
        "pct": pct,
    })

# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR (MATCHING SCREENSHOT 1 & 2)
# ─────────────────────────────────────────────────────────────────────────────
def render_sidebar():
    with st.sidebar:
        # Header with Logo Icon matching screenshot
        st.markdown(
            '<div style="text-align:center;padding:1rem 0 0.75rem;">'
            '<div style="display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;background:linear-gradient(135deg,#FF7675,#FD79A8);border-radius:12px;margin-bottom:0.6rem;box-shadow:0 4px 12px rgba(253,121,168,0.3);font-size:1.6rem;">'
            '📈'
            '</div>'
            '<div style="font-weight:800;font-size:1.05rem;line-height:1.3;color:var(--text-main);">'
            'Reinforcement Learning'
            '</div>'
            '<div style="font-size:0.78rem;color:var(--text-muted);margin-top:0.25rem;">'
            'NPTEL Quiz Dashboard'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        # Theme Switcher (subtle pill)
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            if st.button("☀️ Light", key="btn_theme_light", use_container_width=True):
                st.session_state.theme = "light"
                st.rerun()
        with t_col2:
            if st.button("🌙 Dark", key="btn_theme_dark", use_container_width=True):
                st.session_state.theme = "dark"
                st.rerun()

        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)

        # Primary Navigation Buttons (Screenshot 1 & 2)
        if st.button("🏠  Home", key="nav_home", use_container_width=True):
            st.session_state.current_page = "home"
            st.rerun()

        if st.button("📊  Dashboard", key="nav_dash", use_container_width=True):
            st.session_state.current_page = "dashboard"
            st.rerun()

        if st.button("🔀  Mixed Quiz", key="nav_mixed", use_container_width=True):
            st.session_state.current_page = "mixed"
            st.rerun()

        # Weekly Quizzes Section Header
        st.markdown(
            '<div style="font-size:0.75rem;font-weight:700;color:var(--text-sub);text-transform:uppercase;letter-spacing:0.08em;margin:1.4rem 0 0.6rem 0.2rem;">'
            'WEEKLY QUIZZES'
            '</div>',
            unsafe_allow_html=True
        )

        # 12 Week Buttons with exact icons from reference app
        for wk, wd in QUIZ_DATA.items():
            icon = wd["icon"]
            btn_label = f"{icon}  {wk}"
            if st.button(btn_label, key=f"side_btn_{wk}", use_container_width=True):
                st.session_state.selected_week = wk
                st.session_state.current_page = "week_detail"
                st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: HOME (MATCHING SCREENSHOT 1)
# ─────────────────────────────────────────────────────────────────────────────
def render_home():
    total_weeks = len(QUIZ_DATA)
    total_questions = sum(len(w["2026"]) + len(w["2025"]) for w in QUIZ_DATA.values())

    # Calculate attempted and avg best score
    history = st.session_state.quiz_history
    attempted_count = len(history)
    if attempted_count > 0:
        scores = [h["pct"] for h in history]
        avg_score_text = f"{int(sum(scores)/len(scores))}%"
    else:
        avg_score_text = "—"

    # Top Hero Banner (Matching Screenshot 1)
    st.markdown(
        '<div class="hero-banner">'
        '<div class="hero-title">📈 Reinforcement Learning</div>'
        '<div class="hero-sub">'
        'NPTEL Quiz Dashboard — Master Reinforcement Learning concepts through interactive quizzes, from Multi-Armed Bandits to POMDPs'
        '</div>'
        '<a href="https://nptel.ac.in/courses/106106143" target="_blank" class="hero-pill-btn">'
        '🌐 Visit Official NPTEL Course Page'
        '</a>'
        '</div>',
        unsafe_allow_html=True
    )

    # 4 Stats Cards (Matching Screenshot 1)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(
            f'<div class="stat-card"><div class="stat-number">{total_weeks}</div><div class="stat-label">TOTAL WEEKS</div></div>',
            unsafe_allow_html=True
        )
    with c2:
        st.markdown(
            f'<div class="stat-card"><div class="stat-number">{total_questions}</div><div class="stat-label">QUESTIONS</div></div>',
            unsafe_allow_html=True
        )
    with c3:
        st.markdown(
            f'<div class="stat-card"><div class="stat-number">{attempted_count}</div><div class="stat-label">ATTEMPTED</div></div>',
            unsafe_allow_html=True
        )
    with c4:
        st.markdown(
            f'<div class="stat-card"><div class="stat-number">{avg_score_text}</div><div class="stat-label">AVG BEST SCORE</div></div>',
            unsafe_allow_html=True
        )

    st.markdown("<div style='height:1.5rem;'></div>", unsafe_allow_html=True)

    # Question Bank Selector (Matching Screenshot 1: Select Question Bank)
    st.markdown(
        '<div style="font-size:0.92rem;font-weight:600;color:var(--text-main);margin-bottom:0.4rem;">'
        '📁 Select Question Bank <span style="font-size:0.8rem;color:var(--text-sub);cursor:help;" title="Choose which assignment year to practice across all weeks">ⓘ</span>'
        '</div>',
        unsafe_allow_html=True
    )

    bank_opts = ["2026 Assignment", "2025 Assignment", "Mixed (Both Years)"]
    current_bank_idx = 0 if st.session_state.selected_bank == "2026" else (1 if st.session_state.selected_bank == "2025" else 2)
    selected_bank_choice = st.radio(
        "Question Bank",
        options=bank_opts,
        index=current_bank_idx,
        horizontal=True,
        label_visibility="collapsed",
        key="home_bank_select"
    )

    if "2026" in selected_bank_choice:
        st.session_state.selected_bank = "2026"
    elif "2025" in selected_bank_choice:
        st.session_state.selected_bank = "2025"
    else:
        st.session_state.selected_bank = "mixed"

    st.markdown("<div style='height:1.25rem;'></div>", unsafe_allow_html=True)

    # Mixed Quiz Row (Matching Screenshot 1)
    st.markdown(
        '<div style="font-size:1.35rem;font-weight:700;color:var(--text-main);margin-bottom:0.75rem;">'
        '🔀 Mixed Quiz — Test Across All Weeks'
        '</div>',
        unsafe_allow_html=True
    )

    mc1, mc2 = st.columns([3, 1])
    with mc1:
        st.markdown(
            '<div class="mixed-promo-card">'
            '<div style="display:flex;align-items:center;gap:1.15rem;">'
            '<div style="width:50px;height:50px;border-radius:12px;background:var(--notice-bg);display:flex;align-items:center;justify-content:center;font-size:1.6rem;color:var(--primary-purple);flex-shrink:0;">'
            '🔀'
            '</div>'
            '<div>'
            '<div style="font-size:1.05rem;font-weight:700;color:var(--text-main);">Mixed Quiz</div>'
            f'<div style="font-size:0.86rem;color:var(--text-muted);margin-top:0.2rem;">Shuffled assignment questions from all 12 weeks · {total_questions} questions available</div>'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    with mc2:
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        if st.button("Configure →", key="btn_cfg_mixed", use_container_width=True):
            st.session_state.current_page = "mixed"
            st.rerun()

    st.markdown("<div style='height:1.25rem;'></div>", unsafe_allow_html=True)

    # Weekly Overview List
    st.markdown("### Weekly Quizzes")
    active_bank = st.session_state.selected_bank

    for wk, wd in QUIZ_DATA.items():
        icon = wd["icon"]
        title = wd["title"]
        q_count = len(get_questions_for_week(wk, active_bank))
        bank_label = "2026 Assignment" if active_bank == "2026" else ("2025 Assignment" if active_bank == "2025" else "Mixed")

        st.markdown(
            '<div class="mixed-promo-card" style="margin-bottom:0.65rem;padding:1.1rem 1.4rem;">'
            '<div style="display:flex;align-items:center;gap:1rem;">'
            f'<div style="font-size:1.6rem;">{icon}</div>'
            '<div>'
            f'<div style="font-weight:700;font-size:1rem;color:var(--text-main);">{wk}: {title}</div>'
            f'<div style="font-size:0.82rem;color:var(--text-muted);margin-top:0.2rem;">{q_count} questions ({bank_label})</div>'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        bcol1, bcol2, bcol3 = st.columns([1, 1, 1])
        with bcol1:
            if st.button(f"Open {wk} Overview", key=f"open_ov_{wk}", use_container_width=True):
                st.session_state.selected_week = wk
                st.session_state.current_page = "week_detail"
                st.rerun()
        with bcol2:
            if st.button(f"Practice {wk}", key=f"quick_prac_{wk}", use_container_width=True):
                start_quiz(wk, active_bank, "practice")
                st.rerun()
        with bcol3:
            if st.button(f"Test {wk}", key=f"quick_test_{wk}", use_container_width=True):
                start_quiz(wk, active_bank, "test")
                st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: WEEK DETAIL (MATCHING SCREENSHOT 2)
# ─────────────────────────────────────────────────────────────────────────────
def render_week_detail():
    wk = st.session_state.selected_week
    wd = QUIZ_DATA[wk]
    icon = wd["icon"]
    title = wd["title"]
    active_bank = st.session_state.selected_bank

    q_count = len(get_questions_for_week(wk, active_bank))

    # History stats for this specific week
    week_attempts = [h for h in st.session_state.quiz_history if h["week"] == wk]
    attempts_num = len(week_attempts)
    best_score_str = f"{max(h['pct'] for h in week_attempts)}%" if attempts_num > 0 else "—"

    # Top Hero Banner (Matching Screenshot 2)
    st.markdown(
        '<div class="hero-banner" style="padding:2.25rem 2rem 1.85rem;">'
        f'<div class="hero-title">{icon} {wk}</div>'
        f'<div class="hero-sub" style="margin-bottom:0.25rem;">{title}</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # 3 Stats Cards (Matching Screenshot 2)
    bank_name_upper = "2026 ASSIGNMENT" if active_bank == "2026" else ("2025 ASSIGNMENT" if active_bank == "2025" else "MIXED ASSIGNMENTS")
    w1, w2, w3 = st.columns(3)
    with w1:
        st.markdown(
            f'<div class="stat-card"><div class="stat-number">{q_count}</div><div class="stat-label">{bank_name_upper}</div></div>',
            unsafe_allow_html=True
        )
    with w2:
        st.markdown(
            f'<div class="stat-card"><div class="stat-number">{attempts_num}</div><div class="stat-label">ATTEMPTS</div></div>',
            unsafe_allow_html=True
        )
    with w3:
        st.markdown(
            f'<div class="stat-card"><div class="stat-number">{best_score_str}</div><div class="stat-label">BEST SCORE</div></div>',
            unsafe_allow_html=True
        )

    # Active Question Bank Notice Strip (Matching Screenshot 2)
    active_bank_text = "2026 Assignment" if active_bank == "2026" else ("2025 Assignment" if active_bank == "2025" else "Mixed (2025 + 2026)")
    st.markdown(
        f'<div class="notice-strip">📌 Question Bank: <strong>{active_bank_text}</strong> ({q_count} questions)</div>',
        unsafe_allow_html=True
    )

    # Switch Bank Button
    switch_target = "2025" if active_bank == "2026" else ("2026" if active_bank == "2025" else "2026")
    switch_label = f"🔄 Switch to {switch_target} Assignment" if active_bank != "mixed" else "🔄 Switch to 2026 Assignment"
    
    sw_col1, sw_col2 = st.columns([1, 2])
    with sw_col1:
        if st.button(switch_label, key="btn_switch_bank", use_container_width=True):
            st.session_state.selected_bank = switch_target
            st.rerun()

    st.markdown("<div style='height:1.25rem;'></div>", unsafe_allow_html=True)

    # Choose Quiz Mode (Matching Screenshot 2)
    st.markdown(
        '<div style="font-size:1.45rem;font-weight:700;color:var(--text-main);margin-bottom:1rem;">'
        'Choose Quiz Mode'
        '</div>',
        unsafe_allow_html=True
    )

    m1, m2 = st.columns(2)
    with m1:
        st.markdown(
            '<div class="mode-card">'
            '<div>'
            '<div class="mode-icon">📖</div>'
            '<div class="mode-title">Practice Mode</div>'
            '<div class="mode-desc">Answer questions one by one. See instant feedback with correct answers and explanations after each question.</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
        if st.button("Start Practice", key="btn_start_practice", use_container_width=True):
            start_quiz(wk, active_bank, "practice")
            st.rerun()

    with m2:
        st.markdown(
            '<div class="mode-card">'
            '<div>'
            '<div class="mode-icon">🏆</div>'
            '<div class="mode-title">Test Mode</div>'
            '<div class="mode-desc">Answer all questions with shuffled order. See your score and detailed review only after submitting all answers.</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
        if st.button("Start Test", key="btn_start_test", use_container_width=True):
            start_quiz(wk, active_bank, "test")
            st.rerun()

    st.markdown("<div style='height:1.25rem;'></div>", unsafe_allow_html=True)

    # Preview Question Topics Expander (Matching Screenshot 2)
    with st.expander(f"Preview Question Topics ({q_count} questions)", expanded=False):
        qs_list = get_questions_for_week(wk, active_bank)
        for i, q in enumerate(qs_list):
            q_snippet = q["question"].split("\n")[0][:110]
            st.markdown(f"• **Q{i+1}:** {q_snippet}...")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: QUIZ RUNNER (MATCHING SCREENSHOT 3 & 4)
# ─────────────────────────────────────────────────────────────────────────────
def render_quiz():
    qs = st.session_state.shuffled_questions
    total = len(qs)
    if total == 0:
        st.warning("No questions found for the active selection.")
        if st.button("Back"):
            st.session_state.current_page = "home"
            st.rerun()
        return

    mode = st.session_state.quiz_mode
    wk = st.session_state.selected_week
    bank = st.session_state.selected_bank

    if mode == "practice":
        render_practice_mode(qs, total, wk, bank)
    else:
        render_test_mode(qs, total, wk, bank)

# --- PRACTICE MODE (MATCHING SCREENSHOT 3) ---
def render_practice_mode(qs, total, wk, bank):
    idx = st.session_state.current_question_idx
    q = qs[idx]

    # Header Matching Screenshot 3
    st.markdown(
        '<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.25rem;">'
        f'<div style="font-size:0.75rem;font-weight:700;color:var(--text-sub);text-transform:uppercase;letter-spacing:0.08em;">{wk.upper()} · PRACTICE MODE</div>'
        f'<div style="background:var(--notice-bg);color:var(--notice-text);padding:0.25rem 0.75rem;border-radius:99px;font-size:0.78rem;font-weight:600;">Question {idx + 1} of {total}</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # Week Title
    title_text = QUIZ_DATA.get(wk, {}).get("title", wk) if wk != "Mixed Quiz" else "Mixed Assignment Questions"
    st.markdown(
        f'<div style="font-size:1.35rem;font-weight:700;color:var(--text-main);margin-bottom:0.6rem;">{title_text}</div>',
        unsafe_allow_html=True
    )

    # Purple Thin Progress Bar Matching Screenshot 3
    st.progress((idx + 1) / total)

    # Question Card with Purple Number Circle Matching Screenshot 3
    st.markdown(
        '<div class="q-card">'
        f'<div class="q-badge">{idx + 1}</div>'
        f'<div class="q-text">{q["question"]}</div>'
        '</div>',
        unsafe_allow_html=True
    )

    ans_record = st.session_state.answers.get(idx, {})
    prev_idx = ans_record.get("selected_idx", None)

    # Options Matching Screenshot 3
    selected_choice = st.radio(
        f"Select an option for Question {idx + 1}:",
        options=q["options"],
        index=prev_idx,
        key=f"prac_opt_{idx}",
        label_visibility="collapsed"
    )

    checked = ans_record.get("checked", False)

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)

    # Bottom Buttons Matching Screenshot 3: Check Answer ✓ and Next →
    b1, b2 = st.columns(2)
    with b1:
        if not checked:
            if st.button("Check Answer ✓", key="btn_prac_check", use_container_width=True):
                if selected_choice is not None:
                    sel_i = q["options"].index(selected_choice)
                    is_corr = (sel_i in q["correct"]) if isinstance(q["correct"], list) else (sel_i == q["correct"])
                    st.session_state.answers[idx] = {
                        "selected": selected_choice,
                        "selected_idx": sel_i,
                        "correct": is_corr,
                        "checked": True,
                    }
                    st.rerun()
                else:
                    st.warning("Please choose an option first.")
        else:
            if idx > 0:
                if st.button("← Previous", key="btn_prac_prev", use_container_width=True):
                    st.session_state.current_question_idx = idx - 1
                    st.rerun()

    with b2:
        if idx < total - 1:
            if st.button("Next →", key="btn_prac_next", use_container_width=True):
                st.session_state.current_question_idx = idx + 1
                st.rerun()
        else:
            if st.button("Finish Practice →", key="btn_prac_finish", use_container_width=True):
                finish_quiz(qs, total, wk, bank, "Practice Mode")

    # Immediate Feedback Box
    if checked:
        is_corr = ans_record.get("correct", False)
        correct_txt = ", ".join([q["options"][c] for c in q["correct"]]) if isinstance(q["correct"], list) else q["options"][q["correct"]]
        if is_corr:
            st.markdown('<div class="feedback-box-correct">✓ Correct!</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                f'<div class="feedback-box-incorrect">✕ Incorrect. Correct Answer: <strong>{correct_txt}</strong></div>',
                unsafe_allow_html=True
            )

        st.markdown(
            f'<div class="feedback-explanation"><strong>Explanation:</strong><br>{q["explanation"]}</div>',
            unsafe_allow_html=True
        )

# --- TEST MODE (MATCHING SCREENSHOT 4) ---
def render_test_mode(qs, total, wk, bank):
    title_text = QUIZ_DATA.get(wk, {}).get("title", wk) if wk != "Mixed Quiz" else "Mixed Assignment Questions"
    answered_count = sum(1 for i in range(total) if st.session_state.answers.get(i, {}).get("selected") is not None)

    # Title & Subtitle Matching Screenshot 4
    st.markdown(
        f'<div style="font-size:1.45rem;font-weight:700;color:var(--text-main);margin-bottom:0.15rem;">{title_text}</div>'
        f'<div style="font-size:0.86rem;color:var(--text-muted);margin-bottom:0.75rem;">{answered_count}/{total} answered</div>',
        unsafe_allow_html=True
    )

    # Thin Progress Bar
    st.progress(answered_count / total)
    st.markdown("<div style='height:0.75rem;'></div>", unsafe_allow_html=True)

    # Sequential Questions Matching Screenshot 4
    for i, q in enumerate(qs):
        st.markdown(
            '<div class="q-card">'
            f'<div class="q-badge">{i + 1}</div>'
            f'<div class="q-text">{q["question"]}</div>'
            '</div>',
            unsafe_allow_html=True
        )

        prev_idx = st.session_state.answers.get(i, {}).get("selected_idx", None)
        selected_choice = st.radio(
            f"Question {i+1} Options",
            options=q["options"],
            index=prev_idx,
            key=f"test_opt_{i}",
            label_visibility="collapsed"
        )

        if selected_choice is not None:
            si = q["options"].index(selected_choice)
            is_c = (si in q["correct"]) if isinstance(q["correct"], list) else (si == q["correct"])
            st.session_state.answers[i] = {
                "selected": selected_choice,
                "selected_idx": si,
                "correct": is_c,
                "checked": False,
            }

        st.markdown("<div style='height:0.75rem;'></div>", unsafe_allow_html=True)

    # Submit Button Matching Screenshot 4
    st.markdown("<hr style='border:none;border-top:1px solid var(--card-border);margin:1.5rem 0;'>", unsafe_allow_html=True)
    sb_col1, sb_col2, sb_col3 = st.columns([1, 2, 1])
    with sb_col2:
        if st.button("Submit Test", key="btn_test_submit", use_container_width=True):
            unanswered = [i + 1 for i in range(total) if st.session_state.answers.get(i, {}).get("selected") is None]
            if unanswered and len(unanswered) > 0:
                st.warning(f"Notice: You have {len(unanswered)} unanswered question(s).")
            finish_quiz(qs, total, wk, bank, "Test Mode")

def finish_quiz(qs, total, wk, bank, mode_name):
    correct_count = sum(1 for i in range(total) if st.session_state.answers.get(i, {}).get("correct", False))
    pct = int((correct_count / total) * 100) if total > 0 else 0
    record_quiz_attempt(wk, bank, mode_name, correct_count, total, pct)

    st.session_state.results_data = {
        "week": wk,
        "bank": bank,
        "mode": mode_name,
        "questions": qs,
        "total": total,
        "correct": correct_count,
        "pct": pct,
    }
    st.session_state.current_page = "results"
    st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: RESULTS
# ─────────────────────────────────────────────────────────────────────────────
def render_results():
    res = st.session_state.results_data
    if not res:
        st.session_state.current_page = "home"
        st.rerun()
        return

    pct = res["pct"]
    correct = res["correct"]
    total = res["total"]
    wk = res["week"]
    bank = res["bank"]
    mode = res["mode"]
    qs = res["questions"]

    st.markdown(
        '<div class="hero-banner" style="padding:2.5rem 2rem;">'
        f'<div style="font-size:0.85rem;font-weight:700;color:rgba(255,255,255,0.85);text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.4rem;">{wk} · {mode} ({bank.upper()})</div>'
        f'<div style="font-size:3.5rem;font-weight:800;color:#FFFFFF;line-height:1.1;">{pct}%</div>'
        f'<div style="font-size:1.2rem;font-weight:700;margin:0.5rem 0 0.2rem;">{correct} of {total} Correct</div>'
        '</div>',
        unsafe_allow_html=True
    )

    r1, r2, r3 = st.columns(3)
    with r1:
        if st.button("🏠 Home", key="res_home", use_container_width=True):
            st.session_state.current_page = "home"
            st.rerun()
    with r2:
        if st.button("🔄 Retake Quiz", key="res_retake", use_container_width=True):
            start_quiz(wk, bank, "practice" if "Practice" in mode else "test")
            st.rerun()
    with r3:
        if wk != "Mixed Quiz":
            if st.button(f"📖 Back to {wk}", key="res_week", use_container_width=True):
                st.session_state.current_page = "week_detail"
                st.rerun()
        else:
            if st.button("🔀 Mixed Builder", key="res_mixed", use_container_width=True):
                st.session_state.current_page = "mixed"
                st.rerun()

    st.markdown("<hr style='border:none;border-top:1px solid var(--card-border);margin:1.5rem 0;'>", unsafe_allow_html=True)
    st.markdown("### Answer Review")

    for i, q in enumerate(qs):
        ans_info = st.session_state.answers.get(i, {})
        is_correct = ans_info.get("correct", False)
        selected_text = ans_info.get("selected", "Unanswered")
        correct_text = ", ".join([q["options"][c] for c in q["correct"]]) if isinstance(q["correct"], list) else q["options"][q["correct"]]

        box_cls = "feedback-box-correct" if is_correct else "feedback-box-incorrect"
        status_sym = "✓ Correct" if is_correct else "✕ Incorrect"

        corr_line = f'<div style="font-size:0.88rem;margin-top:0.35rem;color:var(--text-main);">Correct Answer: <strong style="color:var(--primary-purple);">{correct_text}</strong></div>' if not is_correct else ""

        st.markdown(
            f'<div class="{box_cls}">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;font-weight:700;">'
            f'<span>Question {i + 1}</span>'
            f'<span>{status_sym}</span>'
            f'</div>'
            f'<div style="font-size:0.95rem;margin:0.5rem 0;color:var(--text-main);font-weight:500;">{q["question"]}</div>'
            f'<div style="font-size:0.88rem;color:var(--text-muted);">Your Answer: <strong>{selected_text}</strong></div>'
            f'{corr_line}'
            f'</div>'
            f'<div class="feedback-explanation"><strong>Explanation:</strong> {q["explanation"]}</div>',
            unsafe_allow_html=True
        )

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: MIXED QUIZ BUILDER
# ─────────────────────────────────────────────────────────────────────────────
def render_mixed_builder():
    st.markdown(
        '<div style="margin-bottom:1.5rem;">'
        '<div style="font-size:1.85rem;font-weight:800;color:var(--text-main);">🔀 Mixed Quiz Builder</div>'
        '<div style="color:var(--text-muted);font-size:0.92rem;margin-top:0.25rem;">'
        'Test across multiple weeks with questions from 2026, 2025, or combined.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("#### 1. Select Question Banks to Include")
    yc1, yc2 = st.columns(2)
    with yc1:
        inc_26 = st.checkbox("2026 Assignments", value=("2026" in st.session_state.mixed_years), key="chk_m_26")
    with yc2:
        inc_25 = st.checkbox("2025 Assignments", value=("2025" in st.session_state.mixed_years), key="chk_m_25")

    active_years = []
    if inc_26: active_years.append("2026")
    if inc_25: active_years.append("2025")
    st.session_state.mixed_years = active_years

    if not active_years:
        st.warning("Please select at least one year.")
        return

    st.markdown("#### 2. Select Weeks")
    w1, w2 = st.columns(2)
    with w1:
        if st.button("Select All Weeks", key="mix_btn_all", use_container_width=True):
            st.session_state.mixed_weeks = list(QUIZ_DATA.keys())
            st.rerun()
    with w2:
        if st.button("Deselect All", key="mix_btn_none", use_container_width=True):
            st.session_state.mixed_weeks = []
            st.rerun()

    cols = st.columns(3)
    selected_weeks = []
    for i, (wk, wd) in enumerate(QUIZ_DATA.items()):
        cnt = sum(len(wd[y]) for y in active_years)
        is_chk = (wk in st.session_state.mixed_weeks)
        with cols[i % 3]:
            if st.checkbox(f"{wd['icon']} {wk} ({cnt}Q)", value=is_chk, key=f"m_wk_{wk}"):
                selected_weeks.append(wk)

    st.session_state.mixed_weeks = selected_weeks

    pool_size = 0
    for wk in selected_weeks:
        wd = QUIZ_DATA.get(wk, {})
        for y in active_years:
            pool_size += len(wd.get(y, []))

    st.markdown(f"#### 3. Quiz Size ({pool_size} questions available)")
    if pool_size == 0:
        st.warning("No questions available. Please select at least one week.")
        return

    slider_val = min(st.session_state.mixed_count, pool_size)
    slider_val = max(5, slider_val)
    count = st.slider("Number of Questions:", min_value=min(5, pool_size), max_value=pool_size, value=slider_val, step=5)
    st.session_state.mixed_count = count

    mode_choice = st.radio("Mode:", ["Practice Mode (one by one)", "Test Mode (full test)"], index=0, horizontal=True)
    chosen_mode = "practice" if "Practice" in mode_choice else "test"

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("Start Mixed Quiz →", key="btn_launch_mixed", use_container_width=True):
            start_custom_mixed(active_years, selected_weeks, count, chosen_mode)
            st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
def render_dashboard():
    st.markdown(
        '<div style="margin-bottom:1.5rem;">'
        '<div style="font-size:1.85rem;font-weight:800;color:var(--text-main);">📊 Performance Dashboard</div>'
        '<div style="color:var(--text-muted);font-size:0.92rem;margin-top:0.25rem;">'
        'Review your quiz attempts, accuracy, and test history.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    history = st.session_state.quiz_history
    if not history:
        st.markdown(
            '<div class="stat-card" style="padding:3rem 1.5rem;text-align:center;">'
            '<div style="font-size:2rem;margin-bottom:0.5rem;">📊</div>'
            '<div style="font-size:1.1rem;font-weight:700;color:var(--text-main);">No Attempts Recorded Yet</div>'
            '<div style="font-size:0.88rem;color:var(--text-muted);margin-top:0.35rem;">Complete a weekly quiz or mixed test to track your performance.</div>'
            '</div>',
            unsafe_allow_html=True
        )
        return

    total_attempts = len(history)
    scores = [h["pct"] for h in history]
    avg_score = int(sum(scores) / len(scores))
    best_score = max(scores)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f'<div class="stat-card"><div class="stat-number">{total_attempts}</div><div class="stat-label">TOTAL ATTEMPTS</div></div>',
            unsafe_allow_html=True
        )
    with c2:
        st.markdown(
            f'<div class="stat-card"><div class="stat-number">{avg_score}%</div><div class="stat-label">AVERAGE SCORE</div></div>',
            unsafe_allow_html=True
        )
    with c3:
        st.markdown(
            f'<div class="stat-card"><div class="stat-number">{best_score}%</div><div class="stat-label">BEST SCORE</div></div>',
            unsafe_allow_html=True
        )

    st.markdown("### Attempt Log")
    for h in reversed(history):
        st.markdown(
            '<div class="mixed-promo-card" style="padding:1rem 1.25rem;margin-bottom:0.65rem;">'
            '<div>'
            f'<div style="font-weight:700;font-size:1rem;color:var(--text-main);">{h["week"]} ({h["bank"].upper()}) · {h["mode"]}</div>'
            f'<div style="font-size:0.78rem;color:var(--text-muted);margin-top:0.2rem;">{h["timestamp"]} · {h["score"]}/{h["total"]} correct</div>'
            '</div>'
            f'<div style="font-size:1.6rem;font-weight:800;color:var(--primary-purple);">{h["pct"]}%</div>'
            '</div>',
            unsafe_allow_html=True
        )

    if st.button("Clear Quiz History", key="btn_clear_hist"):
        st.session_state.quiz_history = []
        st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# ROUTER
# ─────────────────────────────────────────────────────────────────────────────
def main():
    render_sidebar()
    page = st.session_state.current_page
    if page == "home":
        render_home()
    elif page == "week_detail":
        render_week_detail()
    elif page == "quiz":
        render_quiz()
    elif page == "results":
        render_results()
    elif page == "mixed":
        render_mixed_builder()
    elif page == "dashboard":
        render_dashboard()
    else:
        render_home()

if __name__ == "__main__":
    main()
