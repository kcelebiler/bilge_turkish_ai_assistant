import bs4
import requests

base_url = "https://www.google.com/search?q="

def get_cryptocurrency(source, target):
    
    """
    scrapes the google search page and returns the price text as int

    Args:
        source (string): base cryptocurrency name
        target (string): target cryptocurrency name

    Returns:
        int: specified crypto price text
    """

    keywords = "1+"+source+"+ka%C3%A7+"+target

    keywords = keywords.replace(" ","+")
    
    search_url = base_url + keywords
    
    request_result=requests.get(search_url)
  
    soup = bs4.BeautifulSoup(request_result.text,"html.parser")
    
    price_text = soup.find("div" , class_='BNeawe').text
    
    price = round(int(price_text.split(" ")[0].split(",")[0].replace(".","")))
    
    return price
    