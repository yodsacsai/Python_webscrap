from asyncore import write
from turtle import title
from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.scrapethissite.com/pages/" 

#request
res = requests.get(url)
res.encoding = "utf-8"
#print(res)

#call BeatifulSoup package
soup = BeautifulSoup(res.text, 'html.parser')


articles = soup.find_all('div', {"class":"page"})
#print(articles)

# Create an empty list
article_list = []
csv_col = []

for article in articles:
    
    title = article.a.string
    description = article.p.string
    
    article_list.append(title)
    article_list.append(description)
    csv_col.append(article_list)
    article_list = []
    
print(csv_col)

title_col = ['Title', 'Description']

f = open('articles.csv', 'w')
with f:
    writer = csv.writer(f)
    writer.writerow(title_col)
    writer.writerows(csv_col)
    
print(len(article_list))
print(type(article_list))