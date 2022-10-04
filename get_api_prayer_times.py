
import requests

#get api from e-solat jakim
def get_api():
    url="https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period=week&zone=SGR01"
    response=requests.get(url).json()["prayerTime"]
    return response

get_api()
