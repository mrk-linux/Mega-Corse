# 📹 Motion Detection with Email Alert

This project detects motion using a webcam, captures images when motion is detected, and sends an email alert with the captured image.

---

## 🚀 Features

- Real-time motion detection using OpenCV
- Captures and saves images when motion is detected
- Sends email alerts with the captured image
- Displays motion mask and bounding boxes
- Simple and easy to use

---

## 📁 Project Structure

```
motion-detection/
├── main.py              # Main application script
├── email_sender.py      # Email sending module
├── images/              # Folder for captured images
│   └── (captured images)
└── README.md
```

---

## 🛠️ Requirements

Install the required packages:

```bash
pip install opencv-python
```

### Email Setup

1. Enable **2-Step Verification** in your Gmail account
2. Generate an **App Password** from [Google App Passwords](https://myaccount.google.com/apppasswords)
3. Update the `email_sender.py` file with your credentials

---

## 📧 Email Configuration

In `email_sender.py`, update these values:

```python
PASSWORD = "your_app_password"  # Your Gmail app password
SENDER = "your_email@gmail.com" # Your Gmail address
RECEIVER = "your_email@gmail.com" # Receiver email address
```

---

## ▶️ Usage

1. Make sure the `images/` folder exists
2. Run the script:

```bash
python main.py
```

3. Press `q` to exit the program

---

## 📊 How It Works

| Step | Description |
|------|-------------|
| 1 | Captures video from the webcam |
| 2 | Detects motion by comparing frames with the background |
| 3 | Draws a green rectangle around moving objects |
| 4 | Saves the frame as an image in the `images/` folder |
| 5 | Sends an email with the captured image after motion stops |

---

## 📌 Notes

- The script saves images in the `images/` folder
- Only images larger than 3000 pixels are considered valid (to reduce noise)
- The middle image from the captured sequence is sent via email
- The threshold for motion detection is set to 60 (adjustable)

