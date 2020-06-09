#!/usr/bin/env python
# coding: utf-8

# In[30]:


# coding=utf-8
import requests as rq
from bs4 import BeautifulSoup

f=open('temple.txt','w')
re=rq.get('http://twgod.com/CwP/P/P1.html') #怎麼找到得? 忘記了
soup = BeautifulSoup(re.content,"html.parser",from_encoding="utf-8") #re.content才能解碼
sel=soup.select(".ListType2 a")
dic={} #廟的字典
god_dic={} #神明字典
for temple in sel[:5]:
    url='http://twgod.com/CwP/P/'+temple["href"] #每間廟的網址only Taipei
    re=rq.get(url)
    soup = BeautifulSoup(re.content,"html.parser",from_encoding="utf-8")
    sel=soup.select("#CwMm #CwMm td div") #每間廟網頁裡的廟宇資訊
    detail =[]
    for item in sel:
        detail.append(item.text)
        dic.update({temple.text:detail}) #存廟的資訊進去廟的字典
    if detail[5] not in god_dic:#存神明的資訊進去神明的字典
        god_dic.update({detail[5]:{temple.text:detail}}) # or god_dic.update({detail[5]:{temple.text}})分兩本字典
    else:
        god_dic[detail[5]].update({temple.text:detail}) #god_dic[detail[5]].update({temple.text})
#    print(detail[5],detail[1])
    #print()
#print(len(god_dic))    
for key, value in god_dic["釋迦牟尼佛"].items():
    print(key, value,file=f)
    #print((),file=f)
#print(god_dic,file=f)
f.close()


# In[27]:


print("a")


# In[ ]:




