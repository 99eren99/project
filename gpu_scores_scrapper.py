import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
import numpy as np

urls=["https://www.videocardbenchmark.net/high_end_gpus.html",
      'https://www.videocardbenchmark.net/mid_range_gpus.html',
      'https://www.videocardbenchmark.net/midlow_range_gpus.html',
      'https://www.videocardbenchmark.net/low_end_gpus.html']

gpu_names_list=[]
scores_list=[]
prices_list=[]
for url in urls:
    page=requests.get(url)
    soup=BeautifulSoup(page.content, "html.parser")
    soup = soup.find('ul', class_='chartlist')
    gpu_names=soup.find_all("span",class_="prdname")
    scores=soup.find_all("span",class_="count")
    prices=soup.find_all("span",class_="price-neww")
    print(len(gpu_names), len(scores), len(prices))
    for item in gpu_names:
        gpu_names_list.append(item.text)
    for item in scores:
        scores_list.append(item.text)
    for item in prices:
        prices_list.append(item.text)

with open("gpu_benchmarks.csv","w",encoding="utf-8",newline="") as f:
    writer=csv.writer(f)
    header=["GPU Model","Score","Price"]
    writer.writerow(header)
    for i in range(len(gpu_names_list)):
        writer.writerow([gpu_names_list[i],scores_list[i],prices_list[i]])