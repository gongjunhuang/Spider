import zipfile
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import requests
import urllib

proxy="http://127.0.0.1:1080"
# 创建一个ProxyHandler对象
proxy_support=urllib.request.ProxyHandler({'http':proxy})
# 创建一个opener对象
opener = urllib.request.build_opener(proxy_support)
# 给request装载opener
urllib.request.install_opener(opener)

print("download and unzip files")
dates = pd.date_range(pd.to_datetime('2001-05-01'), pd.to_datetime('2018-06-30'), freq='M')

for date in dates:
    url = 'http://mis.nyiso.com/public/csv/pal/{0}{1}01pal_csv.zip'.format(date.year, str(date.month).zfill(2))
    urllib.request.urlretrieve(url, 'C:/Users/JOE/DM/energy_forecasting_notebooks/data/nyiso/{0}'.format(url.split('/')[-1]))