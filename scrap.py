from bs4 import BeautifulSoup
import requests
import csv


url = "https://www.scrapethissite.com/pages/" 

res = requests.get(url)
res.encoding = "utf-8"
print(res)

soup = BeautifulSoup(res.text, 'html.parser')

# articles = soup.find_all('h3')
articles = soup.find_all('div', {"class":"page"})
print(articles)

# Create an empty list
article_list = []
csv_col = []

for article in articles:

    # Create new variable --> obj to store
    # only course name getting rid of unwanted tags
    obj = article.a.string
    obj2 = article.p.string

    # Append each course into a course_list variable
    article_list.append(obj)
    article_list.append(obj2)
    csv_col.append(article_list)
    article_list = []

print(article_list)

# Define row and column (DataFrame)
title_col = ['Title', 'Description']
#csv_col = [article_list]

# Name a file, and put w as an argument to tell this is "writer" file
f = open('articles.csv', 'w')
with f:
    writer = csv.writer(f)
    writer.writerow(title_col)
    writer.writerows(csv_col)
    #for row in csv_col:
    #    writer.writerow(row)

# To count how many courses in the list
print(len(article_list))
# Display type of this object (Of course, it's "list")
print(type(article_list))


