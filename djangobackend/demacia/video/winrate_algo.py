
# 해당 시간 이전의 승률 데이터로 승률 만들기
# 요소 포탑처치, totalgold, 에픽몬스터, 와드설치, 킬수

import requests
import json

# def winning_rate(part_set,part_set1,gameId):
gameId = "4664501922"
url = "https://kr.api.riotgames.com/lol/match/v4/matches/"+str(gameId)+"?api_key=RGAPI-4dcd2099-2605-4440-9864-f53a305141e7"
time_data = requests.get(url).json()["participants"]
file_path = "../../champions.json"
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)


for t in range(10):
    participantId = time_data[t]["participantId"]
    championId = time_data[t]["championId"]
    for i in range(len(json_data)):
        if championId == int(json_data[i]["key"]):
            print(json_data[i]["id"])


events_creator_id = ["WARD_PLACED"]
events_killer_id = ["WARD_KILL", "BUILDING_KILL", "CHAMPION_KILL"]
events_moster_kill = ["ELITE_MONSTER_KILL"]
part_set = [{}, {'WARD_PLACED': 4, 'totalGold': 4243, 'level': 10, 'totalminionsKilled': 90}, {'WARD_PLACED': 6, 'CHAMPION_KILL': 1, 'WARD_KILL': 1, 'totalGold': 5333, 'level': 9, 'totalminionsKilled': 90}, {'WARD_PLACED': 4, 'CHAMPION_KILL': 3, 'totalGold': 4974, 'level': 11, 'totalminionsKilled': 81}, {'WARD_PLACED': 9, 'CHAMPION_KILL': 1, 'WARD_KILL': 1, 'totalGold': 4311, 'level': 8, 'totalminionsKilled': 87}, {'WARD_PLACED': 
4, 'CHAMPION_KILL': 3, 'WARD_KILL': 4, 'ELITE_MONSTER_KILL': ['FIRE_DRAGON'], 'totalGold': 3448, 'level': 8, 'totalminionsKilled': 11}, {'WARD_PLACED': 7, 'CHAMPION_KILL': 4, 'WARD_KILL': 1, 'totalGold': 8153, 'level': 12, 'totalminionsKilled': 128}, {'WARD_PLACED': 5, 'WARD_KILL': 1, 'ELITE_MONSTER_KILL': ['RIFTHERALD', 'AIR_DRAGON'], 'BUILDING_KILL': 1, 'totalGold': 5783, 'level': 10, 'totalminionsKilled': 104}, {'WARD_PLACED': 7, 'WARD_KILL': 2, 'CHAMPION_KILL': 1, 'totalGold': 4883, 'level': 9, 'totalminionsKilled': 90}, {'CHAMPION_KILL': 8, 'WARD_PLACED': 5, 'BUILDING_KILL': 1, 'totalGold': 5832, 'level': 9, 'totalminionsKilled': 109}, {'WARD_PLACED': 7, 'WARD_KILL': 1, 'CHAMPION_KILL': 1, 'totalGold': 5395, 'level': 9, 'totalminionsKilled': 14}]
# 요소 포탑처치, 킬수, totalgold, 에픽몬스터, 와드설치, 레벨차이
blueteam = {'WARD_PLACED': 0,'CHAMPION_KILL': 0,'level': 0,'ELITE_MONSTER_KILL': [],'totalGold': 0,'BUILDING_KILL': 0}
redteam = {'WARD_PLACED': 0,'CHAMPION_KILL': 0,'level': 0,'ELITE_MONSTER_KILL': [],'totalGold': 0,'BUILDING_KILL': 0}
for i in range(1,11):
    if i <= 5:
        for key,value in part_set[i].items():
            if key in blueteam:
                blueteam[key] +=part_set[i][key]
    else:
        for key,value in part_set[i].items():
            if key in redteam:
                redteam[key] +=part_set[i][key]
print(blueteam)
print(redteam)
bluescore = 50
wardgap = blueteam['WARD_PLACED'] - redteam['WARD_PLACED']
killgap = blueteam['CHAMPION_KILL'] - redteam['CHAMPION_KILL']
levelgap = blueteam['level'] - redteam['level']
goldgap = blueteam['totalGold'] - redteam['totalGold']
buildinggap = blueteam['BUILDING_KILL'] - redteam['BUILDING_KILL']
dragongap = len(blueteam['ELITE_MONSTER_KILL']) - len(redteam['ELITE_MONSTER_KILL'])

print(wardgap,killgap,levelgap,goldgap,buildinggap,dragongap)
bluescore += wardgap/5 + killgap*0.5 + levelgap*0.2 + goldgap/2000 + buildinggap*0.5 + dragongap*3
bluescore = round(bluescore,2)

redscore = 100-bluescore
print(bluescore,'vs',redscore)
    # print(part)
# print(part_set)
# print(part_set1)
    

