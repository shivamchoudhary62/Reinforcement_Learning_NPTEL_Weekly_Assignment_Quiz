import sys
import os
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

def clean_text(t):
    if not t:
        return ''
    # Replace PDF math / LaTeX font artifacts
    t = t.replace('(cid:15)', 'ϵ')
    t = t.replace('(cid:16)', '(').replace('(cid:17)', ')')
    t = t.replace('(cid:0)', '(').replace('(cid:1)', ')')
    t = t.replace('\x0c', '') # form feed
    # Remove trailing page numbers e.g. \n1\n or \n2\n or \n4\n
    t = re.sub(r'\n\s*[0-9]+\s*$', '', t)
    return t.strip()

def parse_week_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    
    # Split by questions: 1. 2. 3. ...
    raw_blocks = re.split(r'\n(?=[0-9]+\.\s+)', text)[1:]
    qs = []
    
    for idx, b in enumerate(raw_blocks):
        # Find solution line: Sol. (x) or Solution. (x) or Sol: (x) or Solution: (x)
        m_sol = re.search(r'\n\s*Sol(?:ution|\.)\s*:?\s*([^\n]+)', b)
        sol_line = m_sol.group(1).strip() if m_sol else ''
        explanation = clean_text(b[m_sol.end():].strip()) if m_sol else ''
        content_before_sol = b[:m_sol.start()] if m_sol else b
        
        # Check for options starting with (a)
        m_first_a = re.search(r'\n\s*\(a\)\s+', content_before_sol)
        if m_first_a:
            prompt = clean_text(content_before_sol[:m_first_a.start()].strip())
            prompt = re.sub(r'^[0-9]+\.\s*', '', prompt).strip()
            opts_part = content_before_sol[m_first_a.start():]
            opt_splits = re.split(r'\n\s*\(([a-h])\)\s*', opts_part)
            opts = []
            for i in range(1, len(opt_splits), 2):
                opts.append(clean_text(opt_splits[i+1]))
        else:
            prompt = clean_text(re.sub(r'^[0-9]+\.\s*', '', content_before_sol))
            opts = []
            
        # Parse correct answer(s) from sol_line
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
            'raw': b
        })
    return qs

if __name__ == '__main__':
    for year in ['2026', '2025']:
        for wk in range(1, 13):
            fname = f'extracted/{year}_week{wk:02d}.txt'
            if os.path.exists(fname):
                qs = parse_week_file(fname)
                print(f'{year} W{wk:02d}: {len(qs)} Qs, opts counts={[len(q["options"]) for q in qs]}')
