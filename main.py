import requests
from bs4 import BeautifulSoup

##url to be scraped
url = 'https://knowthychoice.in/blog/'

my_headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OSX 10_14_3) "
                           "AppleWebKit/537.36 (KHTML, like Gecko)Chrome/71.0.3578.98 Safari/537.36",
              "Accept": "*/*", "content-encoding": "gzip", "content-type": "text/html; charset=utf-8"}

response = requests.get(url, headers=my_headers)
soup = BeautifulSoup(response.content, 'html.parser')

## empty dictionary to append the results
result = {}

##scrapping all the main page course information
titles = soup.findAll('div', class_='blog-post-content')

## looping into each course
for title in titles:

    ## extracting url of course
    page = requests.get(title.a.get("href"))
    soup = BeautifulSoup(page.content, 'html.parser')

    ##using selector method to grab the topics covered lists
    topics_covered = (soup.select('#content > section.blog-single > div > div > div > article > ul:nth-child(15) > li'))

    ##empty list to append each topic separetly which is currently raw form
    topics = []
    for topic in topics_covered:
        topics.append(topic.text)

    ##appending into the dictonary as key,value pair title, [topics covered]
    result[title.a.text] = topics

print(result)




