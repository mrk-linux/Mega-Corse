# 📑 Invoice to PDF Generator

This Python script converts Excel invoice files (`.xlsx`) into professional PDF invoices.

---

## 🚀 Features

- Reads all Excel files from the `Invoices/` folder
- Extracts invoice number and date from filename
- Creates a formatted PDF with:
  - Invoice number and date
  - Product table (product ID, name, quantity, price, total)
- Saves each PDF in the `Pdfs/` folder

---

## 📁 Project Structure

```
project/
├── Invoices/          # Place your Excel files here
│   ├── 101-2025.xlsx
│   └── 102-2025.xlsx
├── Pdfs/              # Generated PDFs will appear here
|   ├── 101-2025.pdf
|   ├── 102-2025.pdf
├── main.py            # The script
└── README.md
```

---

## 📝 Excel File Format

Your Excel file should have these columns:

| Column Name        | Description              |
|--------------------|--------------------------|
| `product_id`       | Product identifier       |
| `product_name`     | Name of the product      |
| `amount_purchased` | Quantity purchased       |
| `price_per_unit`   | Price for one unit       |
| `total_price`      | Total price for product  |

### File Naming Convention

Name your Excel files like:  
`{invoice_number}-{date}.xlsx`

Examples:
- `101-2025-01-15.xlsx`
- `102-2025-01-20.xlsx`

---

## 🛠️ Requirements

Install the required packages:

```bash
pip install pandas fpdf
```

---

## ▶️ Usage

1. Place your `.xlsx` files in the `Invoices/` folder
2. Run the script:

```bash
python main.py
```

3. Find your PDF invoices in the `Pdfs/` folder

---

## 🧠 How It Works

1. Scans `Invoices/` for all `.xlsx` files
2. For each file:
   - Reads the Excel data
   - Creates a PDF page
   - Extracts invoice number and date from filename
   - Adds a table with product information
   - Saves the PDF to `Pdfs/`

---

## 📌 Notes

- The `Pdfs/` folder is created automatically (if it doesn't exist)
- Column names are cleaned automatically (underscores → spaces, title case)

---