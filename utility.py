import urllib2 
import os
import re
from bs4 import BeautifulSoup
def merge(list1,list2):

    if not list1:
       return list2

    elif not list2:
       return list1
    else:
        list1=list(set(list1)|set(list2))
        return list1
  

def download(link_list,file_name):
  os.chdir(file_name)
  for link in link_list:
    if (".pdf" or ".doc" or ".zip" or ".mp3") in link:
      req=urllib2.Request(link)

      try:
        usock = urllib2.urlopen(req) 
      except urllib2.HTTPError, e:
        print e.code
        continue
      except urllib2.URLError, e:
        print e.args
        continue                         
      
      file_name =link.split('/')[-1]                                
      f = open(file_name, 'wb')                                     
      #file_size = int(usock.info().getheaders("Content-Length")[0]) 
      print "Downloading: %s " % (file_name)#, file_size)

      downloaded = 0
      block_size = 8192     
      while True:                                     
       buff = usock.read(block_size)
       if not buff:
        break
       
       downloaded = downloaded + len(buff)
       f.write(buff)
       #download_status = r"%3.2f%%" % (downloaded * 100.00 / file_size) 
       #download_status = download_status + (len(download_status)+1) * chr(8)
      f.close()
      print "done"#download_status,"done"
    else:
      print "following link is not downloadable-> %s"%link  
  
def form_list(search):
  return re.sub("[^\w]"," ",search).split()
def strict_list(visited,search_list):
  strict=[]
  
  for link in visited:
    flag=0
    for word in search_list:
      if word.lower() in link.lower():
        flag=1
        continue
      else:
        falg=0
        break
    if flag==1:
       strict.append(link)
  return strict 

def lenient_list(visited,search_list):
  lenient=[]
  for link in visited:
    if any(word.lower() in link.lower() for word in search_list):
      lenient.append(link)
  return lenient     

def source(link1,seed,depth):
    
      
  link_list=[]
  list_url=[]
  depth_0=[]
  list_url.append(seed)
  req=urllib2.Request(link1)
  
  print "active link-->"+link1
  if (".pdf" or ".zip" or ".doc" or ".mp3") in link1:
    print "no link to crawl .Link represents file "
    return list_url,depth_0
  try:
    resp=urllib2.urlopen(req)
  except urllib2.HTTPError, e:
    print e.code
    return list_url,depth_0
  except urllib2.URLError, e:
    print e.args
    return list_url,depth_0
  content=BeautifulSoup(resp)
  position=0
  a_list=content.find_all('a')

  if not a_list:
    return list_url,depth_0
  else:
    for link in a_list:

      x=link.get('href')
      if x is not None:
        x=str(x)
        if x :
          if x.find("htt")==-1:
            
            if  len(x[x.find("/")+1:])!=0 and x.find("..")!=-1:
              x=seed+x[x.find("/")+1:]
            elif x[0]!='/':
              
              
              x=link1[:link1.rfind("/")+1]+x
              
            else:
              x=seed

            
          if x not in list_url or x in depth_0:
            list_url.append(x)

            if depth !=0:
              #print "depth =%d"%depth

              log=open("log.txt",'w') 
              log.write("\n".join(list_url))
              log.close()
              #xyz=raw_input("enter any key to check recursion")
              link_list,depth_0_1=source(x,seed,depth-1)
              #print "depth=%d" %depth
              #print "returned from recursiop"
              depth_0=merge(depth_0,depth_0_1)
              list_url=merge(list_url,link_list)
              log=open("log.txt",'w') 
              log.write("\n".join(list_url))
              log.close()
              #xyz=raw_input("enter any key to continue")

            else:
              depth_0.append(x)
  #print list_url
  return list_url,depth_0



