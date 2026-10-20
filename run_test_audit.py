import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')
import test_questions as questions
from audit_all_discrepancies import get_pdf_questions

total_flagged = 0
results = {}

for year in ['2026', '2025']:
    for wk in range(1, 13):
        fname = f'extracted/{year}_week{wk:02d}.txt'
        if not os.path.exists(fname):
            continue
        pdf_qs = get_pdf_questions(fname)
        code_qs = getattr(questions, f'W{wk}_{year}', [])
        
        wk_flags = []
        for i in range(min(len(pdf_qs), len(code_qs))):
            pq = pdf_qs[i]
            cq = code_qs[i]
            qnum = i + 1
            reasons = []
            
            p_len = len(pq['prompt'])
            c_len = len(cq.get('question', ''))
            
            for sym in ['ϵ', 'δ', 'γ', 'θ']:
                if sym in pq['prompt'] and sym not in cq.get('question', ''):
                    reasons.append(f"Prompt missing symbol '{sym}'")
                    break
                    
            if p_len > 80 and c_len < p_len * 0.7:
                reasons.append(f"Prompt shortened ({c_len} vs {p_len} chars)")
                
            if pq['options']:
                if len(pq['options']) != len(cq.get('options', [])):
                    reasons.append(f"Option count mismatch: {len(pq['options'])} vs {len(cq.get('options', []))}")
                else:
                    for oi, (po, co) in enumerate(zip(pq['options'], cq.get('options', []))):
                        po_clean = re.sub(r'\s+', ' ', po).strip()
                        co_clean = re.sub(r'\s+', ' ', co).strip()
                        if len(po_clean) > 30 and len(co_clean) < len(po_clean) * 0.6:
                            reasons.append(f"Option ({chr(ord('a')+oi)}) shortened ({len(co_clean)} vs {len(po_clean)} chars)")
                            break
                            
            if reasons:
                total_flagged += 1
                wk_flags.append((qnum, reasons))
        if wk_flags:
            results[f'{year}_W{wk}'] = wk_flags

print(f"Total questions flagged across all weeks: {total_flagged}")
for wk_key, flags in results.items():
    print(f"\n--- {wk_key} ({len(flags)} flagged) ---")
    for qn, r in flags:
        print(f"  Q{qn}: {'; '.join(r)}")
