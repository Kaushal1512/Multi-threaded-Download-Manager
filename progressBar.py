from tqdm import tqdm
import time
import requests


data_fragment_size=1024
dfs=data_fragment_size

url="https://acadpubl.eu/jsi/2018-118-7-9/articles/7/31.pdf"

r=requests.get(url, stream=True)

total_size =int(r.headers['content-length'])

with open("Python.pdf",'wb') as f:
	for data in tqdm(iterable=r.iter_content(chunk_size=dfs),total=total_size/dfs,unit= 'KB'):
		f.write(data)

print("Download Complete!")

 
