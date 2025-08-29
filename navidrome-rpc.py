from pypresence import Presence
import time
import requests
from bs4 import BeautifulSoup
import sys
import env as env

RPC = Presence(env.application_id)
RPC.connect()

def update_status():
    try:
        r=requests.get(env.server_url+'/rest/getNowPlaying?u='+env.username+'&t='+env.token+'&s='+env.salt+'&v=1.16.1&c=navidrome')
        soup = BeautifulSoup(r.text, 'html.parser')
        
        try:
            artist = soup.entry.get('artist')
            title = soup.entry.get('title')
            RPC.update(details=title, state=artist)
        except Exception:
            RPC.update(details="Nothing playing currently!")

    except Exception:
        print("Can't connect to server!")
        sys.exit()

while True:
    update_status()
    time.sleep(15)