# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

from pymongo import MongoClient

def get_reviews_num(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    reviews = soup.find('div',{"id": "REVIEWS"})
    num_str = reviews.find('b').text.replace(",","")
    return(int(num_str))

def get_review(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('p', {"property": "reviewBody"})
    
    return content.text

def get_reviews_list(url):
    rev_list = []
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    for review in soup.find_all('div', {"class": "review-container"}):
        rank_div = review.find('div', {"class": "rating reviewItemInline"})
        rank_span = rank_div.find('span') 
        rank = rank_span["class"][1]
        i = rank.find("_")
        score = int(rank[i+1:]) // 5
        
        title = review.find('div', {"class": "quote"})
        link = title.find('a')["href"]
        #content = review.find('div', {"class": "entry"}).text
        content = get_review("https://www.tripadvisor.co.kr%s" % link)
        
        rev_list.append(
            {
                "score": score,
                "link": link,
                "title": title.text,
                "content": content,
            }
        )
    return rev_list

def get_attraction_list(url):
    att_list = []
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    for attraction in soup.find_all('div', {"class": "attraction_element"}):
        title = attraction.find('div', {"class": "listing_title"})
        
        url = attraction.find("a")
        
        rank_div = attraction.find('div', {"class": "listing_rating"})
        rank_span = rank_div.find('span') 
        rank = rank_span["class"][1]
        i = rank.find("_")
        score = int(rank[i+1:]) // 5
        
        
        att_list.append(
            {
                "title":title.text.replace("\n",""),
                "url":url["href"],
                "score":score,
            }
        )
    return att_list

def get_attraction_page_num(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    page = soup.find('div', {"class": "pageNumbers"})
    pages = page.find_all('a')
    return(int(pages[-1].text))

def insert_mongo(att_dict):
    db = client.test
    attractions = db.attractions

    try:
        attractions.insert(att_dict)
    except pymongo.errors.DuplicateKeyError as e:
        print("Duplicate" + e)

if __name__ == "__main__":
    main_url = "https://www.tripadvisor.co.kr"
    att_tmpl = "/Attractions-g294197-Activities-%sSeoul.html#ATTRACTION_LIST"
    
    page_str = ""
    att_url = att_tmpl % (page_str)
    url = "%s%s" % (main_url, att_url)
    page_num = get_attraction_page_num(url)

    client = MongoClient('mongodb://localhost:27017/')

    #for i in range(page_num):
    for i in range(1):
        if i > 0:
            page_str = "oa%d-" % (i * 30)
        att_url = att_tmpl % (page_str)
        url = "%s%s" % (main_url, att_url)
        att_list = get_attraction_list(url)
        for att in att_list:
            rev_url = att['url']
            url = "%s%s" % (main_url, rev_url)
            rev_list = get_reviews_list(url)
            att['reviews'] = rev_list
            # 여행지: att['title']
            # 리뷰내용 : att['title']['reviews']['content']
            print(att['title'])
            insert_mongo(att)
