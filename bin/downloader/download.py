#!/usr/bin/env python3
import requests
from urllib.request import urlretrieve

def download_file(url: str):
    local_filename = "out.mp4" 
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            i = 0
            for chunk in r.iter_content(chunk_size=8192): 
                print(8192*i)
                f.write(chunk)
                i += 1

def download_file_2(url: str):
    dst = "elo.mp4"
    urlretrieve(url, dst)

vid = "https://rr4---sn-f5f7lnee.googlevideo.com/videoplayback?expire=1641005419\&ei=C23PYeODGKOc7ATRo4yoCQ\&ip=89.64.112.188\&id=o-ABSTc6Xorsw-8QBKx8PvafPIAxmzikqxQzPIEGzpZRZH\&itag=248\&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278\&source=youtube\&requiressl=yes\&mh=eT\&mm=31%2C26\&mn=sn-f5f7lnee%2Csn-4g5e6ns7\&ms=au%2Conr\&mv=m\&mvi=4\&pl=18\&initcwndbps=1292500\&vprv=1\&mime=video%2Fwebm\&ns=TiDcCmSt8VtflKA9ywmPJzUG\&gir=yes\&clen=216430242\&dur=1101.300\&lmt=1640938205101434\&mt=1640983493\&fvip=4\&keepalive=yes\&fexp=24001373%2C24007246\&c=WEB\&txp=5437434\&n=eU0YEuvh8JskoA\&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt\&sig=AOq0QJ8wRQIgIChY43QBgj3lhpuLApYXol7k9Rwn8duNiUuYdhj3Ux8CIQCAOL6FC04yQiWGaGtWXGxcgZRfUELLw5B3ETwh_4ywUg%3D%3D\&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps\&lsig=AG3C_xAwRAIgA5Jt81yyHew1sb1egOavG2TpxaBVZGEf7_tm4qPdvzoCIH74myVddsKCGeaK_O_zlYXKS-z5UqGq8OGZDd7RVz8E".replace("\&", "&")

download_file_2(vid)
