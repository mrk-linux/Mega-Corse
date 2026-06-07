import requests

API_key = "2b0416cb86dff983190e813c91a2cfc8"

def get_data(place, forecast_days):
    
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    get_data(place="Tehran", forecast_days=2)
