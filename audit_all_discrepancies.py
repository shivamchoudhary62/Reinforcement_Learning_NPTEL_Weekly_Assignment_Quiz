import sys
import os
import re
import difflib
import questions

sys.stdout.reconfigure(encoding='utf-8')

def get_pdf_questions(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    raw_blocks = re.split(r'\n(?=[0-9]+\.\s+)', text)[1:]
    parsed = []
    for b in raw_blocks:
        m_sol = re.search(r'\n\s*Sol(?:ution|\.)\s*([^\n]+)', b)
        sol_line = m_sol.group(1).strip() if m_sol else ''
        explanation = b[m_sol.end():].strip() if m_sol else ''
        content_before_sol = b[:m_sol.start()] if m_sol else b
        
        m_first_a = re.search(r'\n\s*\(a\)\s+', content_before_sol)
        if m_first_a:
            prompt = content_before_sol[:m_first_a.start()].strip()
            prompt = re.sub(r'^[0-9]+\.\s*', '', prompt).strip()
            opts_part = content_before_sol[m_first_a.start():]
            opt_splits = re.split(r'\n\s*\(([a-h])\)\s*', opts_part)
            opts = []
            for i in range(1, len(opt_splits), 2):
                opts.append(opt_splits[i+1].strip())
        else:
            prompt = re.sub(r'^[0-9]+\.\s*', '', content_before_sol).strip()
            opts = []
            
        parsed.append({
            'prompt': prompt,
            'options': opts,
            'sol_line': sol_line,
            'explanation': explanation,
            'full_raw': b
        })
    return parsed

print("=================================================================")
print("=== COMPREHENSIVE AUDIT OF PARAPHRASED QUESTIONS & EXPLANATIONS ===")
print("=================================================================")

total_flagged = 0
results = {}

for year in ['2026', '2025']:
    for wk in range(1, 13):
        fname = f'extracted/{year}_week{wk:02d}.txt'
        if not os.path.exists(fname): continue
        pdf_qs = get_pdf_questions(fname)
        code_qs = getattr(questions, f'W{wk}_{year}', [])
        
        wk_flags = []
        for i in range(min(len(pdf_qs), len(code_qs))):
            pq = pdf_qs[i]
            cq = code_qs[i]
            qnum = i + 1
            
            reasons = []
            
            # Check prompt length ratio or missing key elements
            p_len = len(pq['prompt'])
            c_len = len(cq.get('question', ''))
            
            # Check for missing symbols / greek letters
            for sym in ['ϵ', 'δ', 'γ', 'α', 'π', 'θ', 'λ', 'Σ', 'τ']:
                if sym in pq['prompt'] and sym not in cq.get('question', '') and sym in ['ϵ', 'δ', 'γ', 'θ']:
                    reasons.append(f"Prompt missing symbol '{sym}' (used in PDF)")
                    break
                    
            if p_len > 80 and c_len < p_len * 0.7:
                reasons.append(f"Prompt significantly shortened ({c_len} chars vs {p_len} in PDF)")
                
            # Check options
            if pq['options']:
                if len(pq['options']) != len(cq.get('options', [])):
                    reasons.append(f"Option count mismatch: PDF has {len(pq['options'])} options vs Code has {len(cq.get('options', []))}")
                else:
                    # Check if options differ significantly
                    for oi, (po, co) in enumerate(zip(pq['options'], cq.get('options', []))):
                        # clean up newlines and spaces
                        po_clean = re.sub(r'\s+', ' ', po).strip()
                        co_clean = re.sub(r'\s+', ' ', co).strip()
                        if len(po_clean) > 30 and len(co_clean) < len(po_clean) * 0.6:
                            reasons.append(f"Option ({chr(ord('a')+oi)}) shortened ({len(co_clean)} vs {len(po_clean)} chars)")
                            break
                            
            # Check explanation
            # Check if PDF explanation is missing from code explanation
            pdf_exp = (pq['sol_line'] + ' ' + pq['explanation']).strip()
            code_exp = cq.get('explanation', '').strip()
            
            if reasons:
                total_flagged += 1
                wk_flags.append({
                    'qnum': qnum,
                    'reasons': reasons,
                    'pdf_prompt': pq['prompt'],
                    'code_prompt': cq.get('question', ''),
                    'pdf_opts': pq['options'],
                    'code_opts': cq.get('options', []),
                    'pdf_sol': pq['sol_line'],
                    'pdf_exp': pq['explanation'],
                    'code_exp': code_exp
                })
        if wk_flags:
            results[f"{year}_W{wk}"] = wk_flags

print(f"Total questions flagged across all weeks: {total_flagged}")
for wk_key, flags in results.items():
    print(f"\n--- {wk_key} ({len(flags)} flagged) ---")
    for f in flags:
        print(f"  Q{f['qnum']}: {'; '.join(f['reasons'])}")
