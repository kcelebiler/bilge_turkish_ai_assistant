import bs4
import requests
import random

joke_url = "http://turkdili.gen.tr/secme-f-kralar.html"

def make_joke():
    
    """
    scrapes the website and returns the text inside of a random paragraph

    Returns:
        random joke (string): text inside of the paragraph
    """

    request_result=requests.get(joke_url)
    
    soup = bs4.BeautifulSoup(request_result.content.decode('utf-8'),"html.parser")
    
    random_joke = soup.findAll("p" , class_='imTAJustify')[random.randint(0,len(soup.findAll("p" , class_='imTAJustify'))-1)].text
    
    random_joke = random_joke.replace("―"," ")
    
    return random_joke

if __name__ == "__main__":

    random_joke = make_joke()

    print(random_joke)