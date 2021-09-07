import bs4
import requests
import random

sports_url = "https://www.haberler.com/spor/"
latest_news_url = "https://www.haberler.com/son-dakika/"
paparazzi_news_url = "https://www.haberler.com/magazin/"
economy_news_url = "https://www.haberler.com/ekonomi/"
health_news_url = "https://www.haberler.com/saglik/"
general_earth_news_url = "https://www.haberler.com/dunya/"
automobile_news_url = "https://www.haberler.com/otomobil/"
politics_news_url = "https://www.haberler.com/politika/"
technology_news_url = "https://www.haberler.com/teknoloji/"

def get_news(category):
    
    """
    scrapes the haberler.com website with the specified category and returns the news title and detail as string

    Args: 
        category (string): category to scrape news e.g. spor, magazin, ekonomi, politika

    Returns:
        title (string): title of the news page
        detail (string): first paragraph of the news page
    """

    try: 
        if category == "spor":
            
            #get random news url
            request_result=requests.get(sports_url)
          
            soup = bs4.BeautifulSoup(request_result.text,"html.parser")
            
            random_news = random.randint(0, len(soup.findAll("div" , class_='hbBoxMainText'))-1)
            
            news_url = soup.findAll("div" , class_='box boxStyle color-sport')[random_news].findAll('a')[0].get('href')
            
            #get title and detail from the url
            news_request_result = requests.get(news_url)
            
            news_soup = bs4.BeautifulSoup(news_request_result.text,"html.parser")
            
            title = news_soup.findAll("div", class_='hbptHead')[0].text.replace("\n","")
            
            detail = news_soup.findAll("div", class_='hbptHead pb0')[0].text.replace("\n","")
            
            return title, detail
            
            
        elif category == "son dakika":
            
            request_result=requests.get(latest_news_url)
          
            soup = bs4.BeautifulSoup(request_result.text,"html.parser")
            
            random_news = random.randint(0, len(soup.findAll("div" , class_='hbBoxMainText'))-1)
            
            news_url = soup.findAll("div" , class_='hblnContent')[random_news].findAll('a')[0].get('href')
            
            #get title and detail from the url
            news_request_result = requests.get(news_url)
            
            news_soup = bs4.BeautifulSoup(news_request_result.text,"html.parser")
            
            title = news_soup.findAll("div", class_='hbptHead')[0].text.replace("\n","")
            
            detail = news_soup.findAll("div", class_='hbptHead pb0')[0].text.replace("\n","")
            
            return title, detail
        
        elif category == "magazin":
            
            request_result=requests.get(paparazzi_news_url)
          
            soup = bs4.BeautifulSoup(request_result.text,"html.parser")
            
            random_news = random.randint(0, len(soup.findAll("div" , class_='hbBoxMainText'))-1)
            
            news_url = soup.findAll("div" , class_='box boxStyle color-magazine')[random_news].findAll('a')[0].get('href')
            
            #get title and detail from the url
            news_request_result = requests.get(news_url)
            
            news_soup = bs4.BeautifulSoup(news_request_result.text,"html.parser")
            
            title = news_soup.findAll("div", class_='hbptHead')[0].text.replace("\n","")
            
            detail = news_soup.findAll("div", class_='hbptHead pb0')[0].text.replace("\n","")
            
            return title, detail
        
        elif category == "ekonomi":
            
            request_result=requests.get(economy_news_url)
          
            soup = bs4.BeautifulSoup(request_result.text,"html.parser")
            
            random_news = random.randint(0, len(soup.findAll("div" , class_='hbBoxMainText'))-1)
            
            news_url = soup.findAll("div" , class_='box boxStyle color-finance')[random_news].findAll('a')[0].get('href')
            
            #get title and detail from the url
            news_request_result = requests.get(news_url)
            
            news_soup = bs4.BeautifulSoup(news_request_result.text,"html.parser")
            
            title = news_soup.findAll("div", class_='hbptHead')[0].text.replace("\n","")
            
            detail = news_soup.findAll("div", class_='hbptHead pb0')[0].text.replace("\n","")
            
            return title, detail
        
        elif category == "sağlık":
            
            request_result=requests.get(health_news_url)
          
            soup = bs4.BeautifulSoup(request_result.text,"html.parser")
            
            random_news = random.randint(0, len(soup.findAll("div" , class_='hbBoxMainText'))-1)
            
            news_url = soup.findAll("div" , class_='box boxStyle color-general')[random_news].findAll('a')[0].get('href')
            
            #get title and detail from the url
            news_request_result = requests.get(news_url)
            
            news_soup = bs4.BeautifulSoup(news_request_result.text,"html.parser")
            
            title = news_soup.findAll("div", class_='hbptHead')[0].text.replace("\n","")
            
            detail = news_soup.findAll("div", class_='hbptHead pb0')[0].text.replace("\n","")
            
            return title, detail
        
        elif category == "dünya":
            
            request_result=requests.get(general_earth_news_url)
          
            soup = bs4.BeautifulSoup(request_result.text,"html.parser")
            
            random_news = random.randint(0, len(soup.findAll("div" , class_='hbBoxMainText'))-1)
            
            news_url = soup.findAll("div" , class_='box boxStyle color-general')[random_news].findAll('a')[0].get('href')
            
            #get title and detail from the url
            news_request_result = requests.get(news_url)
            
            news_soup = bs4.BeautifulSoup(news_request_result.text,"html.parser")
            
            title = news_soup.findAll("div", class_='hbptHead')[0].text.replace("\n","")
            
            detail = news_soup.findAll("div", class_='hbptHead pb0')[0].text.replace("\n","")
            
            return title, detail
        
        elif category == "otomobil":
            
            request_result=requests.get(automobile_news_url)
          
            soup = bs4.BeautifulSoup(request_result.text,"html.parser")
            
            random_news = random.randint(0, len(soup.findAll("div" , class_='hbBoxMainText'))-1)
            
            news_url = soup.findAll("div" , class_='box boxStyle color-general')[random_news].findAll('a')[0].get('href')
            
            #get title and detail from the url
            news_request_result = requests.get(news_url)
            
            news_soup = bs4.BeautifulSoup(news_request_result.text,"html.parser")
            
            title = news_soup.findAll("div", class_='hbptHead')[0].text.replace("\n","")
            
            detail = news_soup.findAll("div", class_='hbptHead pb0')[0].text.replace("\n","")
            
            return title, detail
        
        elif category == "politika":
            
            request_result=requests.get(politics_news_url)
          
            soup = bs4.BeautifulSoup(request_result.text,"html.parser")
            
            random_news = random.randint(0, len(soup.findAll("div" , class_='hbBoxMainText'))-1)
            
            news_url = soup.findAll("div" , class_='box boxStyle color-general')[random_news].findAll('a')[0].get('href')
            
            #get title and detail from the url
            news_request_result = requests.get(news_url)
            
            news_soup = bs4.BeautifulSoup(news_request_result.text,"html.parser")
            
            title = news_soup.findAll("div", class_='hbptHead')[0].text.replace("\n","")
            
            detail = news_soup.findAll("div", class_='hbptHead pb0')[0].text.replace("\n","")
            
            return title, detail
        
        elif category == "teknoloji":
            
            request_result=requests.get(technology_news_url)
          
            soup = bs4.BeautifulSoup(request_result.text,"html.parser")
            
            random_news = random.randint(0, len(soup.findAll("div" , class_='hbBoxMainText'))-1)
            
            news_url = soup.findAll("div" , class_='box boxStyle color-life')[random_news].findAll('a')[0].get('href')
            
            #get title and detail from the url
            news_request_result = requests.get(news_url)
            
            news_soup = bs4.BeautifulSoup(news_request_result.text,"html.parser")
            
            title = news_soup.findAll("div", class_='hbptHead')[0].text.replace("\n","")
            
            detail = news_soup.findAll("div", class_='hbptHead pb0')[0].text.replace("\n","")
            
            return title, detail
        
    except:
        
        return "Bir hata meydana geldi. Lütfen tekrar deneyin.", ""
    
if __name__ == "__main__":

    title, detail = get_news("spor")
    
    print(title + "\n" + detail)