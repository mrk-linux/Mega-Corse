# 👨‍💻 Personal Portfolio

This is a **Streamlit-based personal portfolio website** showcasing my projects, skills, and background as a Python developer.

---

## 🚀 Features

- Clean, professional layout with two columns
- Personal introduction and profile image
- Project cards displaying:
  - Project title
  - Description
  - Image preview
  - Source code link
- Projects split into two columns for better readability

---

## 📁 Project Structure

```
your_project/
├── main.py                # Main Streamlit application
├── data.csv               # Project data (title, description, image, url)
├── image/
│   ├── me.jpg             # Profile picture
│   └── project_images/    # Project screenshots
└── README.md
```

---

## 📄 data.csv Format

The `data.csv` file should contain the following columns (separator: `;`):

| Column        | Description                          |
|---------------|--------------------------------------|
| `title`       | Project title                        |
| `description` | Short description of the project     |
| `image`       | Image filename (inside `image/` folder) |
| `url`         | Link to the source code (GitHub, etc.) |

**Example:**
```csv
title;description;image;url
Weather App;Get real-time weather data;weather.png;https://github.com/...
Todo App;Task management app;todo.png;https://github.com/...
```

---

## 🛠️ Requirements

Install the required packages:

```bash
pip install streamlit pandas
```

---

## ▶️ Usage

Run the application:

```bash
streamlit run main.py
```

---

## 🎨 Layout Details

| Column | Content                          |
|--------|----------------------------------|
| Left   | Profile image                    |
| Right  | Introduction + bio               |
| Left (bottom) | First 10 projects         |
| Right (bottom)| Remaining projects         |

---

## 📌 Notes

- Images should be placed in the `image/` folder
- The `data.csv` file must use semicolon (`;`) as separator
- Profile image is displayed with a fixed width of 600px

