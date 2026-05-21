# 📰 News Email Sender

This Python script fetches the latest news from a news API and sends them to your email address.

---

## 🚀 Features

- Fetches top news articles from a news API
- Extracts article titles and descriptions
- Sends the news as an email to your inbox
- Limits to 20 most recent articles

---

## 🛠️ Requirements

Install the required packages:

```bash
pip install requests
```

You also need a `send_mail.py` module (custom email sender).

---

## 📝 Setup

1. **Get an API Key**  
   Sign up at [NewsAPI.org](https://newsapi.org) and get your free API key.

2. **Update the URL**  
   Replace the URL with your desired news source.  
   Example:  
   `https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY`

3. **Configure Email Sender**  
   Make sure `send_mail.py` is properly configured with your email credentials.

---

## 📁 Project Structure

```
project/
├── main.py              # Main script
├── send_mail.py         # Email sending module
└── README.md
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

The script will:
1. Fetch news from the API
2. Extract titles and descriptions
3. Send them to your email

---

## 📌 Notes

- The script sends up to 20 articles
- Empty titles are automatically skipped
- Email subject: "Today's news"

