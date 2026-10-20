import sys
import os
import re
import json
import questions

sys.stdout.reconfigure(encoding='utf-8')

def parse_pdf_text(text):
    raw_blocks = re.split(r'\n(?=[0-9]+\.\s+)', text)
    blocks = raw_blocks[1:]
    parsed = []
    for b in blocks:
        m_num = re.match(r'^([0-9]+)\.\s*', b)
        qnum = int(m_num.group(1)) if m_num else len(parsed) + 1
        
        m_sol = re.search(r'\n\s*Sol(?:ution|\.)\s*:?\s*([^\n]+)', b)
        sol_text = m_sol.group(1).strip() if m_sol else ''
        explanation = ''
        if m_sol:
            explanation = b[m_sol.end():].strip()
            content_before_sol = b[:m_sol.start()]
        else:
            content_before_sol = b
            
        m_first_a = re.search(r'\n\s*\(a\)\s+', content_before_sol)
        if m_first_a:
            q_text = content_before_sol[:m_first_a.start()].strip()
            q_text = re.sub(r'^[0-9]+\.\s*', '', q_text).strip()
            opts_part = content_before_sol[m_first_a.start():]
            opt_splits = re.split(r'\n\s*\(([a-h])\)\s*', opts_part)
            opts = []
            for i in range(1, len(opt_splits), 2):
                letter = opt_splits[i]
                otext = opt_splits[i+1].strip()
                opts.append((letter, otext))
        else:
            q_text = re.sub(r'^[0-9]+\.\s*', '', content_before_sol).strip()
            opts = []
            
        parsed.append({
            'num': qnum,
            'question': q_text,
            'options': opts,
            'sol': sol_text,
            'explanation': explanation,
            'raw': b
        })
    return parsed

report = []

for year in ['2026', '2025']:
    for wk in range(1, 13):
        fname = f'extracted/{year}_week{wk:02d}.txt'
        if not os.path.exists(fname): continue
        with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
            pdf_data = parse_pdf_text(f.read())
            
        code_qs = getattr(questions, f'W{wk}_{year}', [])
        
        wk_issues = []
        if len(pdf_data) != len(code_qs):
            wk_issues.append(f'Total Q count mismatch: PDF has {len(pdf_data)} vs Code has {len(code_qs)}')
            
        for i in range(min(len(pdf_data), len(code_qs))):
            pq = pdf_data[i]
            cq = code_qs[i]
            issues = []
            
            p_opts_len = len(pq['options'])
            c_opts_len = len(cq.get('options', []))
            if p_opts_len > 0 and p_opts_len != c_opts_len:
                opt_letters = [o[0] for o in pq['options']]
                issues.append(f"Option count mismatch: PDF has {p_opts_len} options {opt_letters} vs Code has {c_opts_len}")
                
            p_qlen = len(pq['question'])
            c_qlen = len(cq.get('question', ''))
            if p_qlen > 80 and c_qlen < p_qlen * 0.65:
                issues.append(f"Prompt significantly condensed: PDF ({p_qlen} chars) vs Code ({c_qlen} chars)")
                
            if '(i)' in pq['question'] and '(i)' not in cq.get('question', ''):
                issues.append("Prompt missing (i) statements from PDF")
                
            sol_letters = re.findall(r'\b([a-h])\b', pq['sol'].lower())
            expected_indices = [ord(c) - ord('a') for c in sol_letters]
            actual_correct = cq.get('correct')
            if isinstance(actual_correct, int):
                actual_list = [actual_correct]
            elif isinstance(actual_correct, list):
                actual_list = actual_correct
            else:
                actual_list = []
                
            if expected_indices and actual_list:
                if set(expected_indices) != set(actual_list):
                    issues.append(f"Correct answer mismatch: PDF says {pq['sol']} (indices {expected_indices}) vs Code correct={actual_correct}")
                    
            if issues:
                wk_issues.append((i+1, issues, pq, cq))
                
        if wk_issues:
            report.append((year, wk, wk_issues))

print(f"Total weeks with issues flagged: {len(report)}")
for yr, wk, wissues in report:
    print(f"\n=== {yr} Week {wk} ({len(wissues)} questions flagged) ===")
    for item in wissues:
        if isinstance(item, str):
            print("  *", item)
        else:
            qnum, issues, pq, cq = item
            print(f"  Q{qnum}:")
            for iss in issues:
                print(f"    - {iss}")
