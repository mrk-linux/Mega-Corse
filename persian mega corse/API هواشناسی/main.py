from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
"""شیء Flask یک برنامه WSGI را پیاده‌سازی می‌کند و به عنوان هسته مرکزی عمل می‌کند.
    نام ماژول یا بسته برنامه به آن ارسال می‌شود. پس از ایجاد، به عنوان یک مرکز ثبت
    برای توابع دید، قوانین آدرس‌ها، تنظیمات قالب و موارد دیگر عمل می‌کند."""

stations = pd.read_csv("D:\porgram\code\mega corse\persian mega corse\API هواشناسی\data-small\stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html", Data=stations.to_html())
# یک قالب را با نام و زمینه داده شده رندر می‌کند.


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = f"D:\porgram\code\mega corse\persian mega corse\API هواشناسی\data-small\TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"station": station, "date": date, "temperature": temperature}


@app.route("/api/v1/<station>")
def all_data(station):
    filename = f"D:\porgram\code\mega corse\your weather api\data-small\TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    # دیتافریم را به دیکشنری تبدیل می‌کند.
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = f"D:\porgram\code\mega corse\persian mega corse\API هواشناسی\data-small\TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True, port=5001)
    # پورت وب سرور. مقدار پیش‌فرض 5000 است یا پورتی که در متغیر تنظیمات SERVER_NAME تعریف شده باشد.