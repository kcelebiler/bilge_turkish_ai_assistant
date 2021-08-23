import webbrowser
from selenium import webdriver


base_url = "https://www.youtube.com/results?search_query="

def play_video(keyword):
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    
    driver = webdriver.Chrome("chromedriver.exe", chrome_options=options)
    
    keyword = keyword.replace(" ","%20")
    
    searching_url = base_url + keyword
    
    driver.get(searching_url)
    
    first_video = driver.find_elements_by_css_selector('.text-wrapper.style-scope.ytd-video-renderer')[0]
    
    link = first_video.find_element_by_css_selector('.title-and-badge.style-scope.ytd-video-renderer a').get_attribute('href')
    
    webbrowser.open(link)
    