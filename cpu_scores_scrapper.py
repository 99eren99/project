import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
import numpy as np

urls=["https://www.cpubenchmark.net/high_end_cpus.html",
      'https://www.cpubenchmark.net/mid_range_cpus.html',
      'https://www.cpubenchmark.net/midlow_range_cpus.html',
      'https://www.cpubenchmark.net/low_end_cpus.html']

cpu_names_list=[]
scores_list=[]
prices_list=[]
for url in urls:
    page=requests.get(url)
    soup=BeautifulSoup(page.content, "html.parser")
    cpu_names=soup.find_all("span",class_="prdname")
    scores=soup.find_all("span",class_="count")
    prices=soup.find_all("span",class_="price-neww")
    for item in cpu_names:
        cpu_names_list.append(item.text)
    for item in scores:
        scores_list.append(item.text)
    for item in prices:
        prices_list.append(item.text)

with open("cpu_benchmarks.csv","w",encoding="utf-8",newline="") as f:
    writer=csv.writer(f)
    header=["CPU Model","Score","Price"]
    writer.writerow(header)
    for i in range(len(cpu_names_list)):
        writer.writerow([cpu_names_list[i],scores_list[i],prices_list[i]])