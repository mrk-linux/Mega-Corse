# 🌌 NASA Astronomy Picture of the Day (APOD) Viewer

This Streamlit app fetches and displays NASA's Astronomy Picture of the Day along with its title and explanation.

---

## 🚀 Features

- Fetches the latest APOD from NASA API
- Displays the image title, full-resolution image, and detailed explanation
- Downloads and caches the image locally

---

## 📁 Project Structure

```
project/
├── app.py               # Main Streamlit application
├── image.png            # Downloaded APOD image (generated at runtime)
└── README.md
```

---

## 🛠️ Requirements

Install the required packages:

```bash
pip install requests streamlit
```

---

## 🔑 API Key Setup

1. Go to [NASA API Portal](https://api.nasa.gov/)
2. Sign up for a free API key
3. Replace `"your api key"` in the code with your actual API key

```python
api_key = "YOUR_ACTUAL_API_KEY"
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

The app will:
1. Fetch the latest APOD data from NASA
2. Download the image
3. Display the title, image, and explanation

---

## 📝 Code Explanation

| Step | Description |
|------|-------------|
| 1 | Send GET request to NASA API |
| 2 | Parse JSON response |
| 3 | Extract title, image URL, and explanation |
| 4 | Download image from the URL |
| 5 | Display content in Streamlit |

---

## 📌 Notes

- The API endpoint uses `https` for secure connection
- Images are saved locally as `image.png`
- For video APOD entries, additional handling would be required
