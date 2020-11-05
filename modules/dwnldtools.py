import requests
from tqdm import tqdm

def download(url, name):
        r = requests.get(url, stream=True)
        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024 
        t = tqdm(total=total_size, unit='B', unit_scale=True)
        with open(name, 'wb') as f:
         for data in r.iter_content(block_size):
          t.update(len(data))
          f.write(data)
        t.close()
        
def hidedownload(url, name):
        r = requests.get(url, stream=True)
        block_size = 1024 
        with open(name, 'wb') as f:
         for data in r.iter_content(block_size):
          f.write(data)
          
def cat(url):
    cat = requests.get(url, stream=True)
    textcat = cat.text
    return textcat