from googlesearch import search
import webbrowser

def open_movie_tvshow(name):

    """
    gets the first url of the google search and opens it

    Args:
        name (string): name of the movie or tv show

    Returns:
        none

    """
    
    query = name + " izle"
    
    link = list(search(query, num=1, stop=1))[0]
    
    webbrowser.open(link)
