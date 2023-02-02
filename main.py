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
# Print the headers containing the token
print(my_token.get_headers())


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


# Function to decode the response from the API
def get_encode_data(data):
    return json.loads(data.text.encode('utf8'))


def main():
    while (True):
        # Input for the station id
        print("To stop enter q")
        station_id = input("Enter Station id:")
        # Retrieve the data for the provided station id
        if (station_id.lower() == 'q'):
            break
        unencrypted_data = get_data_by_station_id(station_id)

        # If data is returned
        if (unencrypted_data.text):
            # Decode the data
            encode_data = get_encode_data(unencrypted_data)
            # Get the station name
            station_name = (get_station_name(station_id)).lower()
            # Get the amount of rain
            amount_of_rain = get_rain_value(encode_data)
            # Get the measurement time
            measurement_time = get_measurement_time(encode_data)

            print(
                f"The amount of rain in {station_name} is {amount_of_rain}mm. The measurement time is {measurement_time} ")
        else:
            print("Station Id is wrong")


if __name__ == '__main__':
    main()
