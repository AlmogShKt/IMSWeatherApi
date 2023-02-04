import json
import os

import requests
from dateutil import parser
from dotenv import load_dotenv


# This class contains the logic to retrieve the token from environment variables
# and store it in the headers
class TokenData:
    def __init__(self):
        # Load the environment variables
        load_dotenv()
        # Retrieve the token from environment variables
        TOKEN = os.getenv('IMS_TOKEN')

        self.headers = {
            'Authorization': f'{TOKEN}'
        }

    # Method to retrieve the headers containing the token
    def get_headers(self):
        return self.headers


# Instance of the TokenData class
my_token = TokenData()


# Function to decode the response from the API
def get_encode_data(data):
    return json.loads(data.text.encode('utf8'))


def get_all_stations():
    url = f"https://api.ims.gov.il/v1/envista/stations/"
    stations_data = get_encode_data(requests.request("GET", url, headers=my_token.get_headers()))
    all_stations = {"station name": "station id"}
    for station in stations_data:
        all_stations.update({station['name']: station['stationId']})

    return all_stations


def print_station_names(all_stations):
    print("The stations are:")
    for station_name, station_id in all_stations.items():  # dct.iteritems() in Python 2
        print("{} - {}".format(station_name, station_id))
    print('\n \n')


# Function to retrieve data from API for the provided station id
def get_data_by_station_id(station_id):
    # URL to retrieve data from
    url = f"https://api.ims.gov.il/v1/envista/stations/{station_id}/data/latest"
    # Return the data using GET method with headers containing the token
    return requests.request("GET", url, headers=my_token.get_headers())


# Function to retrieve the rain value from the API response
def get_rain_value(encode_data):
    return encode_data['data'][0]['channels'][0]['value']


# Function to convert the UTC time to local time and retrieve it
def get_measurement_time(encode_data):
    UTC_time = encode_data['data'][0]['datetime']
    # Parse the UTC time to local time
    converted_time = parser.isoparse(UTC_time).time()
    return converted_time


# Function to retrieve the station name for the provided station id
def get_station_name(station_id):
    # URL to retrieve station name from
    url = f"https://api.ims.gov.il/V1/Envista/stations/{station_id}"
    # Retrieve the response from the API
    response = requests.request("GET", url, headers=my_token.get_headers())
    # Decode the response
    encode_data = get_encode_data(response)
    return encode_data['name']


def get_temp(encode_data):
    temperature_data = {}

    measurements_values = ['TDmax', "TDmin", "TG"]

    for channel_id in encode_data['data'][0]['channels']:
        if channel_id['name'] == measurements_values[0]:
            # TDMax - max temp
            temperature_data.update({channel_id['name']: channel_id['value']})
        if channel_id['name'] == measurements_values[1]:
            # TDMax - max temp
            temperature_data.update({channel_id['name']: channel_id['value']})
        if channel_id['name'] == measurements_values[2]:
            # TDMax - max temp
            temperature_data.update({channel_id['name']: channel_id['value']})

    if len(temperature_data) != 3:
        for key in measurements_values:
            if key not in temperature_data.keys():
                temperature_data.update({key: "missing"})

    return temperature_data


def is_snow_conditions(temperature_data, amount_of_rain):
    if amount_of_rain > 0.0 and temperature_data['TG']:
        return True
    else:
        return False


get_all_stations()


def main():
    to_print_station_name = input("Do you want to print all stations name: (only once) Y/N:")
    if to_print_station_name.lower() == 'y':
        all_stations = get_all_stations()
        print_station_names(all_stations)
    else:
        print("You can Find all station names and id here: ")
    while True:
        # Input for the station id
        print("To stop enter 'q'")
        station_id = input("Enter Station id:")
        # Retrieve the data for the provided station id
        if (station_id.lower() == 'q'):
            break
        unencrypted_data = get_data_by_station_id(station_id)

        # If data is returned
        if unencrypted_data.text:
            try:
                # Decode the data
                encode_data = get_encode_data(unencrypted_data)
                # Get the station name
                station_name = (get_station_name(station_id)).lower()
                # Get the amount of rain
                amount_of_rain = get_rain_value(encode_data)
                # Get the measurement time
                measurement_time = get_measurement_time(encode_data)
                # Get the temperature data
                temperature_data = get_temp(encode_data)
                # Check if there is conditions for snow
                is_snowing = is_snow_conditions(temperature_data, amount_of_rain)

                print('\n \n')
                print("_________________________")
                print(f"Station Name: {station_name} | id: {station_id}")
                print(f"Measurement time is: {measurement_time}")
                print(f"The amount of rain is: {amount_of_rain}mm")
                print(f"The Max temperature is: {temperature_data['TDmax']}°")
                print(f"The Min temperature is: {temperature_data['TDmin']}°")
                print(f"The ground temperature is: {temperature_data['TG']}°")
                if is_snowing:
                    print("**There is snow conditions!!**")
                print("_________________________")
                print('\n \n')
            except:
                print("Error - please choose different station")
            else:
                print("Station Id is wrong")


if __name__ == '__main__':
    main()