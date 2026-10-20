import sys
import os
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

import parse_helper
import questions

def format_question_dict(q):
    lines = ["    {"]
    # escape quotes if needed, but json.dumps handles string formatting nicely
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

print("Helper ready")
