import urllib
from urllib import request
from bs4 import BeautifulSoup
file=open("web.txt","r+")
fileout=open('output.txt','w+')
print("Webscrapping using python and beautifulsoup",file=fileout)
print("Description of mobiles phone are below",file=fileout)
cot=file.readlines()
for i in cot:
    s=str(i)
    lis_name=s.split('/')
    ss=lis_name[len(lis_name)-1]
    print("-----------------------------------",file=fileout)
    print("Mobile Name=",ss[:len(ss)-5],file=fileout)
    print("Printing description",file=fileout)
    print("------------------------------------",file=fileout)
    the_page = urllib.request.urlopen(i)
    soup = BeautifulSoup(the_page, "html.parser")
    for cont in soup.select('table'):
        list1 = []
        list2 = []
        for val in cont.select('.ttl > a'):
            list1.append(val.contents[0])
        for val in cont.select('.nfo'):
            if val.contents:
                list2.append(val.contents[0])
        if len(list1) == len(list2):
            for i in range (0,len(list1)):
                if(list1[i]!='Technology'):
                    print(list1[i],'=',list2[i],file=fileout)
    print("-------------------------------------",file=fileout)
fileout.close()