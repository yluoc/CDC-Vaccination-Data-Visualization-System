def dic_list_gen(alist,blist):
  dictlist=[]
  for y in blist:
    out={}
    for b in range(len(alist)):
      out[alist[b]]=y[b]
    dictlist.append(out)
  return dictlist

import csv
def read_values(file):
  out=[]
  x=open(file,"r")
  y=csv.reader(x)
  z=0
  for line in y:
    if z != 0:
      out.append(line)
    z+=1
  return out



def make_lists(alist,dictlist):
  out2=[]
  for x in dictlist:
    out1=[]
    for y in alist:
      z=x.keys()
      if(y in z):
        out1.append(x[y])
    out2.append(out1)
  return out2
    

import csv
def write_values(file,alist):
  x=open(file,"a")
  y=csv.writer(x)
  y.writerows(alist)

import json
import urllib.request
def json_loader(urlname):
  response = urllib.request.urlopen(urlname)
  content = response.read().decode()
  x=json.loads(content)
  return x

def make_values_numeric(keylist,dict):
  for key1 in keylist:
    for key2 in dict:
      if(key1==key2):
        x=float(dict[key2])
        dict.update({key2:x})
  return dict

import csv
def save_data(keylist,dictlist,file):
  x=open(file,"a")
  a=csv.writer(x)
  a.writerow(keylist)
  out2=[]
  for x in dictlist:
    out1=[]
    for y in keylist:
      z=x.keys()
      if(y in z):
        out1.append(x[y])
    out2.append(out1)
  a.writerows(out2)
  
import csv
def load_data(file):
  x=open(file,"r")
  y=csv.reader(x)
  out=[]
  result=[]
  for line in y:
    out.append(line)
  for i in out[1:]:
    dict={}
    for j in range(len(out[0])):
      dict[out[0][j]]=i[j]
    result.append(dict)
  return result


  

  

    



    




