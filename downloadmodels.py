import sys
import os
import requests

from oneconfig import URL_SPM_MODEL, URL_ONEMT_MODEL, URL_SDIC, URL_TDIC

urls = [URL_SPM_MODEL, URL_ONEMT_MODEL, URL_SDIC, URL_TDIC]
filenames = ["models/IL2ILEN_June7_2024.model","models/checkpoint17.pt","models/dict.SRC.txt","models/dict.TGT.txt"]

for url, filename in zip(urls, filenames):
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=256):
            fd.write(chunk)
    print(f"file {filename} downloaded succesfully")
