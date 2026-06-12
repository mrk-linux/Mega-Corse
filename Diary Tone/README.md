
# 📓 Diary Tone Analyzer

A Streamlit web application that analyzes the emotional tone of diary entries using sentiment analysis. The app visualizes daily positivity and negativity trends from text files.

---

## 🚀 Features

- Analyzes sentiment of diary entries using **NLTK VADER**
- Displays separate **positivity** and **negativity** line charts
- Reads all `.txt` files from a specified folder
- Extracts dates from filenames automatically

---

## 📁 Project Structure

```
Diary Tone/
├── diary/                     # Folder containing diary text files
│   ├── 2025-01-01.txt
│   ├── 2025-01-02.txt
│   └── ...
├── main.py                    # Streamlit application
└── README.md
```

---

## 🛠️ Requirements

Install the required packages:

```bash
pip install streamlit plotly nltk
```

### Download NLTK Data

The app requires the VADER lexicon for sentiment analysis:

```python
import nltk
nltk.download('vader_lexicon')
```

---

## 📄 Diary File Format

- Each file must be a `.txt` file
- Filename format: `YYYY-MM-DD.txt` (e.g., `2025-01-01.txt`)
- File content: Any text (no specific format required)

**Example (`2025-01-01.txt`):**
```
Today was a wonderful day! I felt happy and productive.
```

---

## ▶️ Usage

1. Place your diary `.txt` files in the `diary/` folder
2. Run the Streamlit app:

```bash
streamlit run main.py
```

3. The app will display:
   - Positivity trend line chart
   - Negativity trend line chart

---

## 📊 How It Works

| Step | Description |
|------|-------------|
| 1 | Reads all `.txt` files from the `diary/` folder |
| 2 | Extracts dates from filenames |
| 3 | Uses NLTK's VADER to calculate sentiment scores |
| 4 | Generates interactive line charts using Plotly |
| 5 | Displays results in a Streamlit web interface |

---

## 📌 Notes

- Sentiment scores range from **0 (lowest)** to **1 (highest)**
- The VADER analyzer is specifically tuned for social media text
- Only **English** language is supported
