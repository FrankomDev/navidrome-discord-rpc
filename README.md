# Navidrome Discord Rich Presence

### Fellow selfhosters, if you ever wanted to show on Discord what you listen (like Spotify does) this script should help you. <br>
![image](https://github.com/FrankomDev/navidrome-discord-rpc/blob/main/image.png) <br>
Maybe this image isn't great example because I don't have configured metadata but there's title on top and artist on bottom <br>

Usage:
```shell
https://github.com/FrankomDev/navidrome-discord-rpc.git
cd navidrome-discord-rpc
pip install -r requirements.txt
cp env.py.example env.py
vim env.py
python3 navidrome-rpc.py
```
or with venv:
```shell
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
cp env.py.example env.py
vim env.py
./venv/bin/python3 navidrome-rpc.py
```