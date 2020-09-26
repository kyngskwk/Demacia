
# 해당 시간 이전의 승률 데이터로 승률 만들기
# 요소 포탑처치, totalgold, 에픽몬스터, 
# 토탈골드 차이 500당 1% 차이
# 에픽몬스터 용이면 3%, 4용이면 3%*4 +3% = 15%, 바론이나 장로 +5%, 포탑 한개당 2%, 킬뎃1차이당 0.5%
import requests
import json

# def winning_rate(part_set,part_set1,gameId):
# 챔피언 지정
gameId = "4664501922"
url = "https://kr.api.riotgames.com/lol/match/v4/matches/"+str(gameId)+"?api_key=RGAPI-4dcd2099-2605-4440-9864-f53a305141e7"
time_data = requests.get(url).json()["participants"]
print(time_data)
file_path = "../../champions.json"
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)

part_set = [dict() for _ in range(11)]
for t in range(10):
    participantId = time_data[t]["participantId"]
    championId = time_data[t]["championId"]
    for i in range(len(json_data)):
        if championId == int(json_data[i]["key"]):
            print(json_data[i]["id"])
    

