import json
import csv
import bottle
import processing
import data 
import os.path


@bottle.route('/')
def chart():
  return bottle.static_file("chart.html", root='.')

@bottle.route('/lyc')
def javascript_file():
  code_js = bottle.static_file("chart.js", root='.')
  return code_js

@bottle.route('/showBar')
def bar():
  dic = {}
  with open('saved_data.csv',"r") as f:
    reader = csv.reader(f)
    next(reader)
    for line in reader:
      if line[1] not in dic:
        dic[line[1]] = float(line[6])
  dic = json.dumps(dic)
  return dic


@bottle.route('/showPie')
def pie():
  a=0
  b=0
  c=0
  d=0
  x=open("saved_data.csv","r")
  y=csv.reader(x)
  da=[]
  next(y)
  for line in y:
    da.append(line[0])
  latest = max(da)
  x=open("saved_data.csv","r")
  y=csv.reader(x)
  for line in y:
    if(line[0]==latest):
        a+=int(line[2])
        b+=int(line[3])
        c+=int(line[4])
        d+=int(line[5])
  dic = {"janssen":a, "moderna":b, "pfizer":c, "unknow":d}
  dic1 = json.dumps(dic)
  return dic1

@bottle.post('/showLine')
def line():
  state = bottle.request.body.read().decode()
  lst = []
  f= open('saved_data.csv')
  reader = csv.reader(f)
  next(reader)
  for line in reader:
    if (line[1] == state):
      lst.append({"date": line[0], "series_complete_pop_pct":line[6]})
  lst.sort
  lst = json.dumps(lst)
  return lst



def load_data():
   csv_file = 'saved_data.csv'
   if not os.path.isfile(csv_file):
      url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
      info = data.json_loader(url)
      heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf','series_complete_pop_pct']
      data.save_data(heads, info, 'saved_data.csv')

load_data()


bottle.run(host="0.0.0.0", port=8080)
