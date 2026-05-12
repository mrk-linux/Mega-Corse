# 📄 PDF Generator from CSV

This project generates a **PDF document** with formatted pages, headers, grid lines, and footers based on data from a CSV file.

---

## 🚀 Features

- Reads topics and page counts from a CSV file
- Creates a separate page for each topic
- Adds a title, horizontal grid lines, and a footer on each page
- Supports multi-page topics
- Customizable fonts, colors, and layout

---

## 📁 Project Structure

```
PDF_Templates/
├── main.py               # Main script to generate PDF
├── topics.csv            # Input data file
└── output.pdf            # Generated PDF file
```

---

## 🛠️ Requirements

Install the required Python packages:

```bash
pip install fpdf pandas
```

---

## 📝 CSV File Format

The `topics.csv` file should contain the following columns:

| Column  | Description                          |
|---------|--------------------------------------|
| `Topic` | Title of the topic (appears on each page) |
| `Pages` | Number of pages for that topic       |

Example:

```csv
Topic,Pages
Introduction,1
Python Basics,2
Advanced Topics,3
```

---

## ▶️ Usage

Run the script from the terminal:

```bash
python main.py
```

After execution, the `output.pdf` file will be created in the same folder.

---

## 🧠 How It Works

1. Reads data from `topics.csv`
2. For each topic:
   - Creates a new page
   - Adds the topic title
   - Draws a line under the title
   - Draws horizontal grid lines
   - Adds a footer with the topic title
   - Creates additional pages if needed
3. Saves the final PDF as `output.pdf`

---

## 📌 Notes

- Make sure the CSV file is in the same directory as the script (or update the file path)
- The script uses `A4` page size and `mm` units
- You can customize fonts, colors, and margins by editing the script

