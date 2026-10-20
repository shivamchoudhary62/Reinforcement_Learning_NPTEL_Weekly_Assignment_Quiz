import re
import os
import sys
import questions

sys.stdout.reconfigure(encoding='utf-8')

def parse_pdf_questions(txt_path):
    with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    # Split by questions: 1. , 2. , etc.
    q_pattern = re.compile(r'(?:^|\n)\s*([0-9]+)\.\s+', re.MULTILINE)
    matches = list(q_pattern.finditer(text))
    
    parsed = []
    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i+1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end].strip()
        q_num = int(matches[i].group(1))
        
        # In this block, find options (a), (b), (c), (d), (e)...
        # Also find Sol. or Answer:
        sol_m = re.search(r'(?:^|\n)\s*(?:Sol\.|Answer:?)\s*([^\n]+)', block, re.IGNORECASE)
        sol_text = sol_m.group(1).strip() if sol_m else ""
        
        # Find where options start: usually (a)
        opt_start_m = re.search(r'(?:^|\n)\s*\(a\)\s+', block)
        if opt_start_m:
            q_text = block[:opt_start_m.start()].strip()
            # Remove leading "1. ", etc.
            q_text = re.sub(r'^[0-9]+\.\s*', '', q_text).strip()
            
            # Extract options
            opts_part = block[opt_start_m.start():]
            if sol_m:
                opts_part = block[opt_start_m.start():sol_m.start()]
            
            # Split options by (a), (b), (c), (d), (e), (f), (g), (h)
            opt_splits = re.split(r'(?:^|\n)\s*\(([a-z])\)\s*', opts_part)
            # opt_splits will be ['', 'a', 'text...', 'b', 'text...']
            pdf_opts = []
            for j in range(1, len(opt_splits), 2):
                letter = opt_splits[j]
                opt_content = opt_splits[j+1].strip()
                pdf_opts.append(f"({letter}) {opt_content}")
        else:
            q_text = block
            pdf_opts = []
            
        parsed.append({
            "num": q_num,
            "q_text": q_text,
            "options": pdf_opts,
            "sol": sol_text,
            "full_block": block
        })
    return parsed

def audit_exact():
    diffs = []
    
    for year in ['2026', '2025']:
        for wk in range(1, 13):
            fname = f"extracted/{year}_week{wk:02d}.txt"
            if not os.path.exists(fname):
                continue
            pdf_qs = parse_pdf_questions(fname)
            var_name = f"W{wk}_{year}"
            code_qs = getattr(questions, var_name, [])
            
            for idx in range(max(len(pdf_qs), len(code_qs))):
                p_q = pdf_qs[idx] if idx < len(pdf_qs) else None
                c_q = code_qs[idx] if idx < len(code_qs) else None
                
                if not p_q or not c_q:
                    diffs.append(f"[{year} Week {wk} Q{idx+1}] Count mismatch: PDF has {len(pdf_qs)}, Code has {len(code_qs)}")
                    continue
                
                # Check option count
                p_opt_count = len(p_q["options"])
                c_opt_count = len(c_q.get("options", []))
                
                opt_count_mismatch = (p_opt_count > 0 and p_opt_count != c_opt_count)
                
                # Check option text similarity
                text_divergence = False
                if not opt_count_mismatch and p_opt_count > 0:
                    for k in range(p_opt_count):
                        p_o = re.sub(r'^\([a-z]\)\s*', '', p_q["options"][k]).strip()
                        c_o = c_q["options"][k].strip()
                        # Clean spaces
                        p_clean = re.sub(r'\s+', '', p_o).lower()
                        c_clean = re.sub(r'\s+', '', c_o).lower()
                        if p_clean != c_clean and len(c_clean) < len(p_clean) * 0.7:
                            text_divergence = True
                            break
                            
                # Check question text truncation
                p_q_clean = re.sub(r'\s+', '', p_q["q_text"]).lower()
                c_q_clean = re.sub(r'\s+', '', c_q["question"]).lower()
                q_truncated = len(c_q_clean) < len(p_q_clean) * 0.7 and len(p_q_clean) > 80
                
                if opt_count_mismatch or text_divergence or q_truncated:
                    diffs.append(f"\n==================================================")
                    diffs.append(f"[{year} Week {wk} Q{idx+1}]")
                    if opt_count_mismatch:
                        diffs.append(f"  * OPTION COUNT MISMATCH: PDF has {p_opt_count} options, Code has {c_opt_count} options")
                    if text_divergence:
                        diffs.append(f"  * OPTION TEXT CONDENSED/PARAPHRASED")
                    if q_truncated:
                        diffs.append(f"  * QUESTION TEXT TRUNCATED/SHORTENED (PDF len {len(p_q_clean)} vs Code len {len(c_q_clean)})")
                    diffs.append(f"  PDF Question Snippet:  {p_q['q_text'][:120]}")
                    diffs.append(f"  Code Question Snippet: {c_q['question'][:120]}")
                    diffs.append(f"  PDF Options: {p_q['options'][:4]}")
                    diffs.append(f"  Code Options: {c_q['options'][:4]}")

    with open("text_audit_report.txt", "w", encoding="utf-8") as out:
        out.write("\n".join(diffs))
    print(f"Audit completed. Found {len(diffs)} notes. Written to text_audit_report.txt")

if __name__ == "__main__":
    audit_exact()
