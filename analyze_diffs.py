import sys
import os
import re
import json
import questions

sys.stdout.reconfigure(encoding='utf-8')

def analyze_week(year, week):
    fname = f'extracted/{year}_week{week:02d}.txt'
    if not os.path.exists(fname):
        return
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        
    code_qs = getattr(questions, f'W{week}_{year}', [])
    blocks = re.split(r'\n(?=[0-9]+\.\s+)', text)[1:]
    
    print(f'=== {year} WEEK {week}: PDF={len(blocks)}, CODE={len(code_qs)} ===')
    for idx in range(min(len(blocks), len(code_qs))):
        blk = blocks[idx]
        cq = code_qs[idx]
        qnum = idx + 1
        diffs = []
        
        m_sol = re.search(r'\n\s*Sol\.\s*([^\n]+)', blk)
        content_before_sol = blk[:m_sol.start()] if m_sol else blk
        m_first_a = re.search(r'\n\s*\(a\)\s+', content_before_sol)
        pdf_prompt = content_before_sol[:m_first_a.start()].strip() if m_first_a else content_before_sol.strip()
        pdf_prompt = re.sub(r'^[0-9]+\.\s*', '', pdf_prompt).strip()
        
        code_prompt = cq.get('question', '').strip()
        
        if len(pdf_prompt) > len(code_prompt) + 50:
            diffs.append(f'Prompt truncated (PDF: {len(pdf_prompt)} chars vs Code: {len(code_prompt)} chars)')
            
        if '(i)' in pdf_prompt and '(i)' not in code_prompt:
            diffs.append('Prompt missing (i) statements')
            
        code_opts = cq.get('options', [])
        if m_first_a:
            opts_part = content_before_sol[m_first_a.start():]
            # Match (a) ... up to next option or end
            opt_matches = list(re.finditer(r'\n\s*\(([a-h])\)\s*', opts_part))
            pdf_opts_count = len(opt_matches)
            if pdf_opts_count != len(code_opts):
                diffs.append(f'Option count mismatch (PDF: {pdf_opts_count} vs Code: {len(code_opts)})')
                
        if m_sol:
            sol_text = m_sol.group(1).strip()
            sol_letters = re.findall(r'\b([a-h])\b', sol_text.lower())
            expected_indices = [ord(c) - ord('a') for c in sol_letters]
            actual_correct = cq.get('correct')
            actual_list = [actual_correct] if isinstance(actual_correct, int) else (actual_correct or [])
            if expected_indices and actual_list:
                if set(expected_indices) != set(actual_list):
                    diffs.append(f"Answer key difference: PDF={sol_text} (idx {expected_indices}) vs Code={actual_correct}")
                    
        if diffs:
            print(f'  Q{qnum}: ' + ' | '.join(diffs))

print("--- 2026 AUDIT ---")
for w in range(1, 13):
    analyze_week('2026', w)

print("\n--- 2025 AUDIT ---")
for w in range(1, 13):
    analyze_week('2025', w)
