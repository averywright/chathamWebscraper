from bs4 import BeautifulSoup
import requests
import numpy as np
import random
import math
import time
import pandas as pd
from io import StringIO
import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

def find_source(url):


    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def scrape(query):

    query = urllib.parse.quote_plus(query)
    response = find_source("https://www.google.com/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')
    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links
x = scrape('sportsbooks')
print(x)

