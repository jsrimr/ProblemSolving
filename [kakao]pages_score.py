# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:22:15 2018

@author: user
"""


  
word="Muzi"
pages=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n \
       <meta charset=\"utf-8\">\n  <meta property=\"og:url\"\
       content=\"https://careers.kakao.com/interview/list\"/>\n</head> \
       \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\">\
       </a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\"\
       xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n \
       <meta charset=\"utf-8\">\n  <meta property=\"og:url\" \
       content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\
       \ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"\
       ></a>\n\n\t^\n</body>\n</html>"]
       
#word="blind"
#pages=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

import re

re.search(r'\b'+word+'\b',pages[0])
base=[]
n_link=[]
link_score=[]

for page in pages:
    cnt=0
    external=0
    splitted=page.split()
               
    for piece in splitted:
        if "</a>" in piece:
            external+=1
            
    cnt+=len(re.findall(r'\b'+word+'\b',pages[0]))
                
    base.append(cnt)
    n_link.append(external)
    
link_score=[base[x]/n_link[x] for x in range(len(pages))]

s=sum(link_score)
total=[s-link_score[x] for x in range(len(pages))]


answer = total.index(min(total))
print( answer)