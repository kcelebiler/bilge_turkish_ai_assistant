import webbrowser
import requests
import json

def get_direction(target):

    """
    opens the webbrowser with the direction to the target from current location

    Args:
        target (string): target location to go e.g. eiffel tower, times square

    Returns:
        none
    """
    
    send_url = "http://api.ipstack.com/check?access_key="
    api = "02f03cbaa372a00cd46218243e5118e5"
    url = send_url + api
    geo_req = requests.get(url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    
    url = "https://www.google.com/maps/dir/"
    
    location = str(latitude) + "," + str(longitude)
    
    target = target.replace(" ","+")
    
    direction_url = url + location + "/" + target
    
    webbrowser.open(direction_url)
