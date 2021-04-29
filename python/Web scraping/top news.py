from bs4 import BeautifulSoup
import requests

response=requests.get(url="https://news.ycombinator.com/news")


yc_webpage=response.text

soup=BeautifulSoup(yc_webpage,"html.parser")

# anchor_tag=soup.select_one(".title a")

# print(anchor_tag.getText())
# print(anchor_tag.get("href"))

article_tags=soup.find_all(name="a",class_="storylink")

article_texts=[]
article_links=[]

for article in article_tags:
    text=article.getText()
    article_texts.append(text)
    link=article.get("href")
    article_links.append(link)


article_upvotes=[int(score.getText().split(" ")[0]) for score in soup.find_all(name="span",class_="score")]


# print(article_texts)
# print(article_links)
# print(article_upvotes)



combined_list=list(zip(article_texts,article_links,article_upvotes))
# print(combined_list)


#the text having most upvotes

sorted_combined=sorted(combined_list,key= lambda x:x[2],reverse=True)

the_text=sorted_combined[0][0]
the_link=sorted_combined[0][1]
the_score=sorted_combined[0][2]
print(the_text)
print(the_link)
print(the_score)
