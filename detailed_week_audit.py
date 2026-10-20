import re
import os
import sys
import questions

sys.stdout.reconfigure(encoding='utf-8')

def audit():
    for year in ['2026', '2025']:
        print(f"\n=======================================================")
        print(f"=== AUDITING YEAR {year} ===")
        print(f"=======================================================")
        for wk in range(1, 13):
            fname = f"extracted/{year}_week{wk:02d}.txt"
            if not os.path.exists(fname): continue
            with open(fname, "r", encoding="utf-8", errors="ignore") as f:
                raw_text = f.read()
            
            var_name = f"W{wk}_{year}"
            code_qs = getattr(questions, var_name, [])
            
            q_splits = re.split(r'\n(?=[0-9]+\.\s+)', raw_text)
            pdf_blocks = q_splits[1:]
            
            for idx in range(min(len(pdf_blocks), len(code_qs))):
                blk = pdf_blocks[idx]
                cq = code_qs[idx]
                
                # Check for (a), (b), (c), (d), (e)
                # Find options block
                # Options usually follow: \n(a) ...
                opt_matches = list(re.finditer(r'(?:^|\n)\s*\(([a-e])\)\s*', blk))
                
                # If there are roman numerals before options, e.g. (i), (ii), (iii)...
                has_roman = bool(re.search(r'\((?:i|ii|iii|iv|v|vi)\)', blk))
                
                # Check length difference
                c_len = len(cq['question'])
                p_len = len(blk)
                
                # Check if code options count != pdf options count
                # Let's count genuine (a), (b), (c), (d)
                # Filter out (i) or (v) if they appeared before (a)
                first_a = re.search(r'\n\s*\(a\)\s+', blk)
                if first_a:
                    opts_after_a = list(re.finditer(r'\n\s*\(([a-e])\)\s+', blk[first_a.start():]))
                    opt_count = len(opts_after_a)
                else:
                    opt_count = 0
                    
                code_opt_count = len(cq.get('options', []))
                
                if opt_count > 0 and opt_count != code_opt_count:
                    print(f"[{year} W{wk} Q{idx+1}] Option count mismatch: PDF has {opt_count} options vs Code has {code_opt_count}")
                    
                # If question was heavily truncated (>40% shorter)
                if first_a:
                    p_q_prompt = blk[:first_a.start()].strip()
                    p_q_prompt = re.sub(r'^[0-9]+\.\s*', '', p_q_prompt).strip()
                    if len(cq['question']) < len(p_q_prompt) * 0.6 and len(p_q_prompt) > 100:
                        print(f"[{year} W{wk} Q{idx+1}] Prompt heavily truncated: PDF len {len(p_q_prompt)} vs Code len {len(cq['question'])}")

if __name__ == "__main__":
    audit()
