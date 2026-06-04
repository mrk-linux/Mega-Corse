
# 🌦️ Weather Data API

A Flask-based REST API for accessing historical weather data from weather stations. This API provides endpoints to retrieve temperature data for specific stations, dates, and years.

---

## 🚀 Features

- List all available weather stations
- Get temperature for a specific station and date
- Get all temperature data for a specific station
- Get yearly temperature data for a specific station

---

## 📁 Project Structure

```
your weather api/
├── main.py                          # Flask application
├── data-small/
│   ├── stations.txt                 # Station metadata
│   └── TG_STAIDXXXXXX.txt           # Temperature data files
├── templates/
│   └── home.html                    # Web interface template
└── README.md
```
---

## 🛠️ Requirements

Install the required packages:

```bash
pip install flask pandas
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

The server will start at: `http://127.0.0.1:5001`

---

## 📡 API Endpoints

### 1. Home Page (Web Interface)

```
GET /
```

Displays an HTML page with:
- API usage instructions
- List of all available weather stations

---

### 2. Get Temperature for Specific Station and Date

```
GET /api/v1/<station>/<date>
```

**Parameters:**
| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `station` | int | Station ID | `10` |
| `date` | string | Date (YYYY-MM-DD) | `1988-10-25` |

**Example Request:**
```
http://127.0.0.1:5001/api/v1/10/1988-10-25
```

**Response:**
```json
{
    "station": "10",
    "date": "1988-10-25",
    "temperature": -2.3
}
```

---

### 3. Get All Data for a Specific Station

```
GET /api/v1/<station>
```

**Parameters:**
| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `station` | int | Station ID | `10` |

**Example Request:**
```
http://127.0.0.1:5001/api/v1/10
```

**Response:** Array of all records for that station
```json
[
    {"DATE": "1988-10-01", "TG": 15},
    {"DATE": "1988-10-02", "TG": 16},
    ...
]
```

---

### 4. Get Yearly Data for a Specific Station

```
GET /api/v1/yearly/<station>/<year>
```

**Parameters:**
| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `station` | int | Station ID | `10` |
| `year` | int | Year (YYYY) | `1988` |

**Example Request:**
```
http://127.0.0.1:5001/api/v1/yearly/10/1988
```

**Response:** Array of records for that year
```json
[
    {"DATE": "1988-01-01", "TG": -5},
    {"DATE": "1988-01-02", "TG": -3},
    ...
]
```

---

## 📊 Data Format

- Temperature values are stored in tenths of degrees Celsius
- The API automatically divides values by 10 to return actual Celsius degrees
- Data files are sourced from weather stations with 6-digit IDs (padded with leading zeros)

---

## 🌐 Web Interface

The home page displays:
- API usage examples
- A table of all available weather stations with their names and IDs

---

## 📌 Notes

- Station IDs are automatically padded to 6 digits (e.g., station `1` → `000001`)
- Date format must be `YYYY-MM-DD`
- Year format must be `YYYY`
- Temperature is returned in degrees Celsius

