import webbrowser
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 

def getLocation():

    """
    source code :
    https://codeburst.io/how-i-understood-getting-accurate-geolocation-using-python-web-scraping-and-selenium-7967d721587a
    """

    options = Options()
    options.add_argument("--use--fake-ui-for-media-stream")
    driver = webdriver.Chrome(executable_path = 'chromedriver.exe',options=options)
    driver.get("https://mycurrentlocation.net/")
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]') 
    longitude = [x.text for x in longitude]    
    longitude = str(longitude[0])    
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')    
    latitude = [x.text for x in latitude]    
    latitude = str(latitude[0])    
    driver.quit()    
    return (latitude,longitude)

def get_direction(target):

    """
    opens the webbrowser with the direction to the target from current location

    Args:
        target (string): target location to go e.g. eiffel tower, times square

    Returns:
        none
    """
    
    url = "https://www.google.com/maps/dir/"
    
    latitude, longitude = getLocation()

    location = str(latitude) + "," + str(longitude)
    
    target = target.replace(" ","+")
    
    direction_url = url + location + "/" + target
    
    webbrowser.open(direction_url)

if __name__ == "__main__":

    get_direction("taksim meydanı")