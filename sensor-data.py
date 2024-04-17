import sacaqm
import datetime
import json


sensor_array = [
    {"Sensor ID": "350457790675308", "Station Name": "Siyabonga Secondary"},
    {"Sensor ID": "350457790675316", "Station Name": "Nkone Maruping Pry"},
    {"Sensor ID": "350457790739948", "Station Name": "J.B Marks Secondary "},
    {"Sensor ID": "350457790740896", "Station Name": "Ikusasalethu Sec"},
    {"Sensor ID": "350457790740979", "Station Name": "Meadowlands West"},
    {"Sensor ID": "350457790741191", "Station Name": "Thulani"},
    {"Sensor ID": "350457791747395", "Station Name": "Slovoville"},
    {"Sensor ID": "350457791749920", "Station Name": "N M Mandela Pry"},
    {"Sensor ID": "350457791750027", "Station Name": "Dobsonville"},
    {"Sensor ID": "350457791750134", "Station Name": "Tshepisong"},
]


cli = sacaqm.sacaqm()
today = datetime.datetime.today()
delta = datetime.timedelta(days=60)

for sensor in sensor_array:
    sensor_id = sensor["Sensor ID"]
    filename = f"{sensor_id}.json"  # Use sensor ID as filename

    # Fetch data for the current sensor
    data = cli.get_sen55(sensor_id, today - delta)

    # Save data to file
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Data for {sensor['Station Name']} saved to {filename}")
