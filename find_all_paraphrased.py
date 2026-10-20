import re
import os
import sys
import questions

sys.stdout.reconfigure(encoding='utf-8')

def check_all_weeks():
    report = []
    
    for year in ['2026', '2025']:
        for wk in range(1, 13):
            fname = f"extracted/{year}_week{wk:02d}.txt"
            if not os.path.exists(fname): continue
            
            with open(fname, "r", encoding="utf-8", errors="ignore") as f:
                raw_text = f.read()
                
            var_name = f"W{wk}_{year}"
            code_qs = getattr(questions, var_name, [])
            
            # Split raw_text by questions
            q_splits = re.split(r'\n(?=[0-9]+\.\s+)', raw_text)
            pdf_blocks = q_splits[1:]
            
            report.append(f"\n=======================================================")
            report.append(f"=== {year} WEEK {wk}: {len(pdf_blocks)} in PDF, {len(code_qs)} in Code ===")
            report.append(f"=======================================================")
            
            for i in range(min(len(pdf_blocks), len(code_qs))):
                p_blk = pdf_blocks[i]
                c_q = code_qs[i]
                
                # Extract options from p_blk
                opt_matches = re.findall(r'(?:^|\n)\s*\(([a-z])\)\s*(.*?)(?=\n\s*\([a-z]\)|\n\s*(?:Sol\.|Answer:?|Solution)|\Z)', p_blk, re.DOTALL)
                pdf_opt_texts = [m[1].strip().replace('\n', ' ') for m in opt_matches]
                code_opts = c_q.get('options', [])
                
                # Check option counts
                if len(pdf_opt_texts) != len(code_opts) and len(pdf_opt_texts) > 0:
                    report.append(f"  [Q{i+1}] OPTION COUNT MISMATCH: PDF={len(pdf_opt_texts)} options vs Code={len(code_opts)} options")
                    report.append(f"       PDF options: {pdf_opt_texts[:5]}")
                    report.append(f"       Code options: {code_opts}")
                    
                # Check if option text was drastically shortened
                shortened_opts = []
                for idx_o in range(min(len(pdf_opt_texts), len(code_opts))):
                    po = pdf_opt_texts[idx_o]
                    co = code_opts[idx_o]
                    # If PDF option is long (>30 chars) and Code option is less than half length
                    if len(po) > 30 and len(co) < len(po) * 0.5:
                        shortened_opts.append((idx_o, po, co))
                if shortened_opts:
                    report.append(f"  [Q{i+1}] OPTION(S) HEAVILY SHORTENED/PARAPHRASED:")
                    for idx_o, po, co in shortened_opts:
                        report.append(f"       Opt ({chr(ord('a')+idx_o)}): PDF: '{po[:80]}' vs Code: '{co}'")
                        
                # Check if question text was heavily shortened
                # Get question part before (a)
                m_a = re.search(r'\n\s*\(a\)', p_blk)
                if m_a:
                    p_prompt = p_blk[:m_a.start()].strip()
                    p_prompt = re.sub(r'^[0-9]+\.\s*', '', p_prompt).replace('\n', ' ')
                    c_prompt = c_q['question'].replace('\n', ' ')
                    if len(p_prompt) > 80 and len(c_prompt) < len(p_prompt) * 0.5:
                        report.append(f"  [Q{i+1}] QUESTION PROMPT HEAVILY SHORTENED:")
                        report.append(f"       PDF: '{p_prompt[:120]}...'")
                        report.append(f"       Code: '{c_prompt[:120]}...'")

    with open("paraphrased_summary.txt", "w", encoding="utf-8") as out:
        out.write("\n".join(report))
    print("Report written to paraphrased_summary.txt")

if __name__ == "__main__":
    check_all_weeks()
