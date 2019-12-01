from django.contrib import admin

# Register your models here.

# import requests
#
# req = requests.get("https://news.ycombinator.com/")
#
# # print(req.encoding)  # returns 'utf-8'
# print(req.status_code)  # returns 200
# print(req.elapsed)  # returns datetime.timedelta(0, 1, 666890)
# print(req.url)  # returns '<a href="https://edureka.co/">https://edureka.co/</a>'
#
# print(req.history)
# returns [<Response [301]>, <Response [301]>]
# print(req.text)
# print(req.headers['Content-Type'])
# returns 'text/html; charset=utf-8'
# print(req)



import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
# url = 'http://web.mta.info/developers/turnstile.html'
#
# # Connect to the URL
# response = requests.get(url)
#
# # Parse HTML and save to BeautifulSoup object¶
# soup = BeautifulSoup(response.text, "html.parser")
#
# # To download the whole data set, let's do a for loop through all a tags
# for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
#     one_a_tag = soup.findAll('a')[i]
#     link = one_a_tag['href']
#     download_url = 'http://web.mta.info/developers/'+ link
#     urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
#     time.sleep(1) #pause the code for a sec