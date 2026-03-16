# Tax Calculator (1099-B Parser)

This is a Python script designed to parse IRS Form 1099-B PDF documents (specifically from Morgan Stanley at Work/Shareworks) and extract the total proceeds, cost basis, and wash sale amounts for short-term and long-term tax categories. It distinguishes between **Covered** and **Noncovered** securities.

## Prerequisites

- Python 3.x
- `pdfplumber` library for parsing PDFs

## Setup Instructions

1. **Create and activate a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Make sure the script is executable (if it isn't already):
   ```bash
   chmod +x parse.py
   ```

2. Run the script and pass the path to your 1099-B PDF file as a command-line argument:
   ```bash
   ./parse.py "path_to_your_1099.pdf"
   ```

   *Alternatively, you can run it via Python directly:*
   ```bash
   python parse.py "path_to_your_1099.pdf"
   ```

## Example Output

```text
Category               | Proceeds (1d)   | Cost Basis (1e)   | Wash Sale (1g) 
-----------------------------------------------------------------------------
Short-Term Covered     | $     12,450.25 | $      10,200.50 | $        150.00
Short-Term Noncovered  | $     45,320.10 | $      48,100.00 | $        620.45
Long-Term Covered      | $     85,900.75 | $      62,400.25 | $          0.00
Long-Term Noncovered   | $     15,230.40 | $      12,050.80 | $         45.50
```
