# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 17:03:18 2018

@author: user
"""

from collections import deque
from itertools import combinations

#from operation import itemgetter
relation=[["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"],\
          ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], \
          ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]

n_row=len(relation)
n_col=len(relation[0])  #->runtime error 우려되는 부분

candidates=[]
for i in range(1,n_col+1):
    candidates.extend(combinations(range(n_col),i))

final=[]
for keys in candidates:
    tmp=[tuple([item[key] for key in keys]) for item in relation]
    if len(set(tmp))==n_row:
        final.append(keys)

answer=set(final[:])
for i in range(len(final)):
    for j in range(i+1,len(final)):
        if len(final[i])==len(set(final[i]).intersection(set(final[j]))):
            answer.discard(final[j])
            
print(len(answer))
    


final=deque()
fail=deque([set([x]) for x in range(n_col)])    #[{0},{1}]
    
#addable_single_key=[x for x in range(n_col)]

addable_single_key=[]
for keys in fail:
    tmp=[tuple([item[key] for key in keys]) for item in relation]
    if len(set(tmp))!=n_row:
            addable_single_key.append(keys.pop())
                

while fail:
    #print(fail)
    keys=fail.popleft()
        
    tmp=[tuple([item[key] for key in keys]) for item in relation] #tmp=[['ryan','music']]
          
    #유일하게 구분해내는 key인가 , 맞다면 성공
    if len(set(tmp))==n_row:
        final.append(keys)    
        #fail.remove(keys)
        
        #add_key 후보군에서 제외
        for key in keys:
            if key in addable_single_key: addable_single_key.remove(key)
    
    #유일성 만족하지 못하는 key
    else:
        #print('failed keys:' , keys)
        for add_key in addable_single_key:
            if add_key in keys:
                continue
            else:
                #print(keys,add_key)
                new_key=keys.union([add_key])
                #print("newkey: ",new_key)
                if new_key not in fail:
                    fail.append(new_key)
                #print("fail : " ,fail)
        #fail.remove(keys)
    #update
           

print(len(final))

