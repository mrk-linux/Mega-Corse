from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
"""The flask object implements a WSGI application and acts as the central
    object.  It is passed the name of the module or package of the
    application.  Once it is created it will act as a central registry for
    the view functions, the URL rules, template configuration and much more."""
stations = pd.read_csv("D:\porgram\code\mega corse\your weather api\data-small\stations.txt", skiprows= 17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html",Data = stations.to_html()) 
# Render a template by name with the given context.

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = f"D:\porgram\code\mega corse\your weather api\data-small\TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows= 20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"]== date]["   TG"].squeeze() / 10
    return {"station": station, "date": date, "temperature": temperature}

@app.route("/api/v1/<station>")
def all_data(station):
    filename = f"D:\porgram\code\mega corse\your weather api\data-small\TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows= 20, parse_dates=["    DATE"])
    result = df.to_dict(orient= "records")
    # Convert the DataFrame to a dictionary.
    return result

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = f"D:\porgram\code\mega corse\your weather api\data-small\TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows= 20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient= "records")
    return result


if __name__ == "__main__":  
    app.run(debug=True, port = 5001) 
    #the port of the webserver. Defaults to 5000 or the port defined in the SERVER_NAME config variable if present