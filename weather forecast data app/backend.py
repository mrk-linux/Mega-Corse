import requests

API_key = "2b0416cb86dff983190e813c91a2cfc8"

def get_data(place, forecast_days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [item["main"]["temp"] for item in filtered_data]

    if kind == "Sky":
        filtered_data = [item["weather"][0]["main"] for item in filtered_data]
    return filtered_data


if __name__ == "__main__":
    get_data(place="Tehran", forecast_days=2, kind="Temperature")
