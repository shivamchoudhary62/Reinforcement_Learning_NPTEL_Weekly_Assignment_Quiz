import sys
import os
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

import parse_helper
import questions

def format_question_dict(q):
    lines = ["    {"]
    q_str = json.dumps(q['question'], ensure_ascii=False)
    lines.append(f"        \"question\": {q_str},")
    lines.append("        \"options\": [")
    for opt in q['options']:
        opt_str = json.dumps(opt, ensure_ascii=False)
        lines.append(f"            {opt_str},")
    lines.append("        ],")
    if isinstance(q['correct'], list):
        lines.append(f"        \"correct\": {q['correct']},")
    else:
        lines.append(f"        \"correct\": {q['correct']},")
    exp_str = json.dumps(q['explanation'], ensure_ascii=False)
    lines.append(f"        \"explanation\": {exp_str},")
    lines.append("    },")
    return "\n".join(lines)

def build_week_code(var_name, q_list):
    lines = [f"{var_name} = ["]
    for q in q_list:
        lines.append(format_question_dict(q))
    lines.append("]\n")
    return "\n".join(lines)

# Prepare dictionary of all weeks
all_weeks_code = {}

# 2026
# W1_2026: keep current
all_weeks_code['W1_2026'] = questions.W1_2026

# W2_2026: keep current, fix Q10 options
w2_26 = [dict(q) for q in questions.W2_2026]
w2_26[9]['options'] = [
    "i and ii",
    "iii and iv",
    "iii and iv",
    "v and vi",
    "i and iii"
]
w2_26[9]['correct'] = 0
all_weeks_code['W2_2026'] = w2_26

# W3_2026: keep current
all_weeks_code['W3_2026'] = questions.W3_2026

# W4_2026: keep current
all_weeks_code['W4_2026'] = questions.W4_2026

# W5_2026: parsed
all_weeks_code['W5_2026'] = parse_helper.parse_week_file('extracted/2026_week05.txt')

# W6_2026: parsed
all_weeks_code['W6_2026'] = parse_helper.parse_week_file('extracted/2026_week06.txt')

# W7_2026: keep current
all_weeks_code['W7_2026'] = questions.W7_2026

# W8_2026: parsed
all_weeks_code['W8_2026'] = parse_helper.parse_week_file('extracted/2026_week08.txt')

# W9_2026: parsed
all_weeks_code['W9_2026'] = parse_helper.parse_week_file('extracted/2026_week09.txt')

# W10_2026: parsed
all_weeks_code['W10_2026'] = parse_helper.parse_week_file('extracted/2026_week10.txt')

# W11_2026: parsed
all_weeks_code['W11_2026'] = parse_helper.parse_week_file('extracted/2026_week11.txt')

# W12_2026: parsed
all_weeks_code['W12_2026'] = parse_helper.parse_week_file('extracted/2026_week12.txt')

# 2025
# W1_2025: keep current
all_weeks_code['W1_2025'] = questions.W1_2025

# W2_2025: keep current, fix symbols
w2_25 = [dict(q) for q in questions.W2_2025]
for idx in [4, 6, 7]:
    w2_25[idx]['question'] = w2_25[idx]['question'].replace('epsilon', 'ϵ').replace('delta', 'δ')
all_weeks_code['W2_2025'] = w2_25

# W3_2025: parsed
all_weeks_code['W3_2025'] = parse_helper.parse_week_file('extracted/2025_week03.txt')

# W4_2025: keep current
all_weeks_code['W4_2025'] = questions.W4_2025

# W5_2025: parsed
all_weeks_code['W5_2025'] = parse_helper.parse_week_file('extracted/2025_week05.txt')

# W6_2025: parsed
all_weeks_code['W6_2025'] = parse_helper.parse_week_file('extracted/2025_week06.txt')

# W7_2025: parsed
all_weeks_code['W7_2025'] = parse_helper.parse_week_file('extracted/2025_week07.txt')

# W8_2025: parsed
all_weeks_code['W8_2025'] = parse_helper.parse_week_file('extracted/2025_week08.txt')

# W9_2025: parsed
all_weeks_code['W9_2025'] = parse_helper.parse_week_file('extracted/2025_week09.txt')

# W10_2025: parsed
all_weeks_code['W10_2025'] = parse_helper.parse_week_file('extracted/2025_week10.txt')

# W11_2025: parsed
all_weeks_code['W11_2025'] = parse_helper.parse_week_file('extracted/2025_week11.txt')

# W12_2025: parsed
all_weeks_code['W12_2025'] = parse_helper.parse_week_file('extracted/2025_week12.txt')

# Build file content
output_lines = [
    '"""',
    'NPTEL Reinforcement Learning - Complete Question Bank (2025 & 2026)',
    'Contains 100% verbatim assignment questions, options, and official solutions/explanations.',
    '"""',
    '',
]

# Write week arrays
for wk in range(1, 13):
    output_lines.append(f"# {'─'*77}")
    output_lines.append(f"# WEEK {wk} (2026)")
    output_lines.append(f"# {'─'*77}")
    output_lines.append(build_week_code(f"W{wk}_2026", all_weeks_code[f"W{wk}_2026"]))
    output_lines.append(f"# {'─'*77}")
    output_lines.append(f"# WEEK {wk} (2025)")
    output_lines.append(f"# {'─'*77}")
    output_lines.append(build_week_code(f"W{wk}_2025", all_weeks_code[f"W{wk}_2025"]))

# Append metadata and QUIZ_DATA
output_lines.append('''
WEEK_META = {
    "Week 1":  {"title": "Introduction to RL & Multi-Armed Bandits",           "icon": "📊", "tag": "W01"},
    "Week 2":  {"title": "Advanced Bandit Algorithms (UCB, Thompson, PAC)",     "icon": "📈", "tag": "W02"},
    "Week 3":  {"title": "Policy Gradient & Contextual Bandits",                "icon": "🔍", "tag": "W03"},
    "Week 4":  {"title": "MDPs, Bellman Equations & Value Functions",           "icon": "⚙️", "tag": "W04"},
    "Week 5":  {"title": "Dynamic Programming & Monte Carlo Methods",           "icon": "🔄", "tag": "W05"},
    "Week 6":  {"title": "TD Learning, SARSA & Q-Learning",                    "icon": "⚡", "tag": "W06"},
    "Week 7":  {"title": "Eligibility Traces & n-Step Methods",                "icon": "📎", "tag": "W07"},
    "Week 8":  {"title": "Function Approximation & LSTD",                      "icon": "🧮", "tag": "W08"},
    "Week 9":  {"title": "DQN, Actor-Critic & Policy Gradient Methods",        "icon": "🤖", "tag": "W09"},
    "Week 10": {"title": "SMDPs, Options & Hierarchical RL",                   "icon": "🏗️", "tag": "W10"},
    "Week 11": {"title": "MAXQ & Hierarchical Decomposition",                  "icon": "🌲", "tag": "W11"},
    "Week 12": {"title": "Partial Observability & POMDPs",                     "icon": "👁️", "tag": "W12"},
}

QUIZ_DATA = {}
for i in range(1, 13):
    wk = f"Week {i}"
    q2026 = eval(f"W{i}_2026")
    q2025 = eval(f"W{i}_2025")
    QUIZ_DATA[wk] = {
        "title": WEEK_META[wk]["title"],
        "icon": WEEK_META[wk]["icon"],
        "tag": WEEK_META[wk]["tag"],
        "week_num": i,
        "2026": q2026,
        "2025": q2025,
        "mixed": q2026 + q2025,
    }
''')

with open('test_questions.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("Successfully written test_questions.py!")
