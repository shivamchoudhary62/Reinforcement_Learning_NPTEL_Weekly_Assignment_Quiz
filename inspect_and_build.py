import sys
import os
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

def clean_math(t):
    if not t:
        return ''
    t = t.replace('(cid:15)', 'ϵ')
    t = t.replace('(cid:16)', '(').replace('(cid:17)', ')')
    t = t.replace('(cid:0)', '(').replace('(cid:1)', ')')
    t = t.replace('\x0c', '')
    # replace common OCR / extraction artifacts
    t = t.replace('–', '–')
    # strip trailing page numbers
    t = re.sub(r'\n\s*[0-9]+\s*$', '', t)
    return t.strip()

def parse_week(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    raw_blocks = re.split(r'\n(?=[0-9]+\.\s+)', text)[1:]
    qs = []
    for idx, b in enumerate(raw_blocks):
        m_sol = re.search(r'\n\s*Sol(?:ution|\.)\s*:?\s*([^\n]+)', b)
        sol_line = m_sol.group(1).strip() if m_sol else ''
        explanation = clean_math(b[m_sol.end():].strip()) if m_sol else ''
        content_before_sol = b[:m_sol.start()] if m_sol else b
        
        m_first_a = re.search(r'\n\s*\(a\)\s+', content_before_sol)
        if m_first_a:
            prompt = clean_math(content_before_sol[:m_first_a.start()].strip())
            prompt = re.sub(r'^[0-9]+\.\s*', '', prompt).strip()
            opts_part = content_before_sol[m_first_a.start():]
            opt_splits = re.split(r'\n\s*\(([a-h])\)\s*', opts_part)
            opts = []
            for i in range(1, len(opt_splits), 2):
                opts.append(clean_math(opt_splits[i+1]))
        else:
            prompt = clean_math(re.sub(r'^[0-9]+\.\s*', '', content_before_sol))
            opts = []
            
        sol_letters = re.findall(r'\b([a-h])\b', sol_line.lower())
        indices = [ord(c) - ord('a') for c in sol_letters]
        if len(indices) == 1:
            correct = indices[0]
        else:
            correct = indices
            
        qs.append({
            'qnum': idx + 1,
            'question': prompt,
            'options': opts,
            'correct': correct,
            'sol_line': sol_line,
            'explanation': explanation,
        })
    return qs

def test():
    for target in [
        ('2026', 10), ('2026', 11), ('2026', 12),
        ('2025', 3), ('2025', 5), ('2025', 6), ('2025', 7),
        ('2025', 8), ('2025', 9), ('2025', 10), ('2025', 11), ('2025', 12)
    ]:
        yr, wk = target
        path = f'extracted/{yr}_week{wk:02d}.txt'
        qs = parse_week(path)
        print(f'{yr} W{wk:02d}: {len(qs)} Qs parsed')
        for q in qs:
            print(f"  Q{q['qnum']}: sol={q['sol_line']}, correct={q['correct']}, opts={len(q['options'])}, prompt_len={len(q['question'])}")

if __name__ == '__main__':
    test()

