from googlesearch import search
import webbrowser

def open_movie_tvshow(name):
    
    query = name + " izle"
    
    link = list(search(query, num=1, stop=1))[0]
    
    webbrowser.open(link)
