def max_value(data, key):
  z = "" ;
  i = 0;
  for value in data:
    for k in value:
      x = value[key]
      if z < x :
        z = x
        i += 1;
  return z


def init_dictionary(dictlist,k):
  a={}
  for i in dictlist:
    for b in i:
      v=0
      if(b==k):
        i[b]=v
        a[v]=0
  return a

def sum_matches(lod,k,v,blyt):
  a=0
  for i in lod:
    for key in i:
      if(key==k):
       if(i[k]==v):
        a=a+i[blyt]
  return a

def copy_matching(data, key, value):
  array2 = []
  for line in data:
    if line[key] == value:
      array2.append(line)
  return array2
