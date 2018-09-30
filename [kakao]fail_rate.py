# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 16:25:38 2018

@author: user
"""


  
N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]

N=3
stages=[2]
#import numpy as np

#fail rate
fail_rate=[0 for x in range(N)]
for i in range(N):
    #i+1 번째 스테이지에 도전하는 사람수
    challenger=[1 if level>=i+1 else 0 for level in stages]
    challenger=sum(challenger)
    #실패율
    if challenger:
            fail_rate[i]= stages.count(i+1) /challenger
        else:
            fail_rate[i]=0

answer=sorted(sorted([(x,v+1) for v,x in enumerate(fail_rate)],key=lambda t:t[1],reverse=False),\
          key=lambda t:t[0],reverse=True)

print( [b for a,b in answer])

#print(solution(N,stages))