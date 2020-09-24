import requests
import json

url = "https://kr.api.riotgames.com/lol/match/v4/timelines/by-match/4659518008?api_key=RGAPI-4dcd2099-2605-4440-9864-f53a305141e7"
time_data = requests.get(url).json()["frames"]
print(time_data)

time = 22 # 사건이 22 ~ 23 분이라고 했을 때 
events_set = ["BUILDING_KILL", "CHAMPION_KILL", "ELITE_MONSTER_KILL", "WARD_KILL", "WARD_PLACED"]


# for t in range(time):