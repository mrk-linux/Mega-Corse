# 🏨 Hotel Reservation System

This project is a **hotel reservation system** that reads hotel data, credit card information, and security passwords from CSV files.

---

## 🚀 Features

- Check hotel availability from CSV database
- Book a hotel and update availability status
- Validate credit card information (number, expiration, holder, CVV)
- Authenticate credit card with security password
- Generate a reservation ticket for the customer

---

## 📁 Project Structure

```
Hotel_Reservation/
├── hotel_reservation.py   # Main script
├── hotels.csv             # Hotel database
├── cards.csv              # Credit card information
└── card_security.csv      # Card security passwords
```

---

## 🛠️ Requirements

Install the required Python package:

```bash
pip install pandas
```

---

## 📝 CSV File Format

### `hotels.csv`

| Column      | Description                          |
|-------------|--------------------------------------|
| `id`        | Hotel ID (string)                    |
| `name`      | Hotel name                           |
| `available` | Availability status (yes/no)         |

### `cards.csv`

| Column      | Description                          |
|-------------|--------------------------------------|
| `number`    | Credit card number (string)          |
| `expiration`| Expiration date (MM/YY)              |
| `holder`    | Cardholder name                      |
| `cvc`       | Security code (string)               |

### `card_security.csv`

| Column      | Description                          |
|-------------|--------------------------------------|
| `number`    | Credit card number (string)          |
| `password`  | Security password                    |

---

## ▶️ Usage

Run the script from the terminal:

```bash
python hotel_reservation.py
```

Enter the hotel ID when prompted. The system will:

1. Check if the hotel is available
2. Validate the credit card (hardcoded example)
3. Authenticate the password
4. Book the hotel
5. Generate a reservation ticket

---

## 🧠 How It Works

1. Read hotel data from `hotels.csv` using Pandas
2. User enters a hotel ID
3. Check if the hotel is available
4. Validate credit card information from `cards.csv`
5. Authenticate password from `card_security.csv`
6. Update hotel availability to "no" and save to CSV
7. Generate a reservation ticket with customer name

---

## 📌 Notes

- Credit card number and password are **hardcoded** in the script for demo purposes
- This code is for **educational purposes only**
- Do not use this in production
- You can edit the CSV files to add more hotels or cards

---

## 🔧 Suggested Improvements

- [ ] Get credit card information from user input
- [ ] Add exception handling
- [ ] Use a database (SQLite or PostgreSQL) instead of CSV
- [ ] Build a GUI or web interface
- [ ] Add reservation date and check-in/check-out

---

## 👨‍💻 Developer

- Name: [alimrk]

- GitHub: [https://github.com/mrk-linux](https://github.com/username)

---

## 📄 License

This project is released under the **MIT** license.

---

**Made with ❤️ in Iran**