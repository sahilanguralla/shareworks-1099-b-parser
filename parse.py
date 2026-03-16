#!/usr/bin/env python3
import pdfplumber
import re
import sys

def parse_ms_1099_b_complete(pdf_path):
    summary = {
        "Short-Term Covered": {"Proceeds": 0.0, "Cost Basis": 0.0, "Wash Sale (1g)": 0.0},
        "Short-Term Noncovered": {"Proceeds": 0.0, "Cost Basis": 0.0, "Wash Sale (1g)": 0.0},
        "Long-Term Covered": {"Proceeds": 0.0, "Cost Basis": 0.0, "Wash Sale (1g)": 0.0},
        "Long-Term Noncovered": {"Proceeds": 0.0, "Cost Basis": 0.0, "Wash Sale (1g)": 0.0}
    }
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            for line in text.split('\n'):
                # Extract all dollar amounts in this line in order (e.g., $57,004.49)
                amounts = re.findall(r'\$([\d,]+\.\d{2})', line)
                
                if "Total Short Term – Covered" in line and len(amounts) >= 3:
                    summary["Short-Term Covered"]["Proceeds"] += clean_currency(amounts[-3])
                    summary["Short-Term Covered"]["Cost Basis"] += clean_currency(amounts[-2])
                    summary["Short-Term Covered"]["Wash Sale (1g)"] += clean_currency(amounts[-1])
                    
                elif "Total Short Term – Noncovered" in line and len(amounts) >= 3:
                    summary["Short-Term Noncovered"]["Proceeds"] += clean_currency(amounts[-3])
                    summary["Short-Term Noncovered"]["Cost Basis"] += clean_currency(amounts[-2])
                    summary["Short-Term Noncovered"]["Wash Sale (1g)"] += clean_currency(amounts[-1])
                    
                elif "Total Long Term – Covered" in line and len(amounts) >= 3:
                    summary["Long-Term Covered"]["Proceeds"] += clean_currency(amounts[-3])
                    summary["Long-Term Covered"]["Cost Basis"] += clean_currency(amounts[-2])
                    summary["Long-Term Covered"]["Wash Sale (1g)"] += clean_currency(amounts[-1])
                    
                elif "Total Long Term – Noncovered" in line and len(amounts) >= 3:
                    summary["Long-Term Noncovered"]["Proceeds"] += clean_currency(amounts[-3])
                    summary["Long-Term Noncovered"]["Cost Basis"] += clean_currency(amounts[-2])
                    summary["Long-Term Noncovered"]["Wash Sale (1g)"] += clean_currency(amounts[-1])

    print_summary(summary)

def clean_currency(value):
    """Removes commas and converts to float."""
    if not value: return 0.0
    return float(value.replace(',', ''))

def print_summary(summary):
    print(f"{'Category':<22} | {'Proceeds (1d)':<15} | {'Cost Basis (1e)':<17} | {'Wash Sale (1g)':<15}")
    print("-" * 77)
    for cat, values in summary.items():
        print(f"{cat:<22} | ${values['Proceeds']:>14,.2f} | ${values['Cost Basis']:>15,.2f} | ${values['Wash Sale (1g)']:>14,.2f}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <path_to_pdf>")
        sys.exit(1)
    parse_ms_1099_b_complete(sys.argv[1])