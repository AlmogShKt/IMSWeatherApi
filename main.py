import json
import os

import requests
from dateutil import parser
from dotenv import load_dotenv


class TokenData:
    def __init__(self):
        load_dotenv()
        TOKEN = os.getenv('IMS_TOKEN')

        self.headers = {
            'Authorization': f'{TOKEN}'
        }

    def get_headers(self):
        return self.headers


my_token = TokenData()
print(my_token.get_headers())


def get_data_by_station_id(station_id):
    url = f"https://api.ims.gov.il/v1/envista/stations/{station_id}/data/latest"
    return requests.request("GET", url, headers=my_token.get_headers())


def get_rain_value(encode_data):
    return encode_data['data'][0]['channels'][0]['value']


def get_measurement_time(encode_data):
    UTC_time = encode_data['data'][0]['datetime']
    converted_time = parser.isoparse(UTC_time).time()
    return converted_time


def get_station_name(station_id):
    url = f"https://api.ims.gov.il/V1/Envista/stations/{station_id}"
    response = requests.request("GET", url, headers=my_token.get_headers())
    encode_data = get_encode_data(response)
    return encode_data['name']


def get_encode_data(data):
    return json.loads(data.text.encode('utf8'))




def main():
    station_id = 42

    unencrypted_data = get_data_by_station_id(station_id)
    encode_data = get_encode_data(unencrypted_data)

    station_name = (get_station_name(station_id)).lower()
    amount_of_rain = get_rain_value(encode_data)
    measurement_time = get_measurement_time(encode_data)

    print(f"The amount of rain in {station_name} is {amount_of_rain}. The measurement time is {measurement_time} ")

if __name__ == '__main__':
    main()