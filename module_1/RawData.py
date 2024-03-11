'''This module contains the RawData class which is used to scrape the raw html data from a provided URL. 
   It also contains the InputOutput class which is used to read and write data to and from files.''' 

'''Single Responsibility Principle'''

import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
"""this helps to access websites that don't like web scraping."""

## Class to get the raw html data from a provided URL
class RawData:
    def scrape(url):
        ## Scrape the page source from the URL
        response = requests.get(url, headers=HEADERS)
        lookUp = BeautifulSoup(response.text, 'html.parser')

        ## return html as BeautifulSoup object
        return lookUp

## Class to read and write data to and from files
class InputOutput:
    def read_urls(filename):
        ## Read URLs from a .txt file
        with open(filename, 'r') as file:
            urls = file.readlines()
        urls = [url.strip() for url in urls]
        return urls
    
    def write_to_file(article, filename):
        """Write the article to a .txt file"""
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(article)

    # def read_file(filename):
    #     """Read lines from a file and return them as a string"""
    #     with open(filename, 'r', encoding='utf-8') as file:
    #         lines = file.readlines()
    #     return lines