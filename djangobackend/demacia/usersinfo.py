import sys
import requests
import json

sys.stdin = open("input.txt", "r", encoding='utf-8')

# print(input())
accounts = {}
info_set = {}
for _ in range(5):
    try:
        other = list(input())
        if len(other) > 15:
            name = ''.join(other[:-15])
            ### 닉네임 -> accountid
            nicktoid = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+ str(name)+ "?api_key=RGAPI-4dcd2099-2605-4440-9864-f53a305141e7"
            results = requests.get(nicktoid).json()
            accounts[name] = results['accountId']
    except EOFError:
        break

for key,val in accounts.items():
    info_set[key] = {}
    accidtogameid = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/"+str(val)+"?endIndex=10&api_key=RGAPI-4dcd2099-2605-4440-9864-f53a305141e7"
    results = requests.get(accidtogameid).json()["matches"]
    for idx in range(len(results)):
        game_id = results[idx]["gameId"]
        info_set[key][game_id] = results[idx]

        info = "https://kr.api.riotgames.com/lol/match/v4/matches/"+str(game_id)+"?api_key=RGAPI-4dcd2099-2605-4440-9864-f53a305141e7"
        result = requests.get(info).json()
        findwin = result["participants"]
        findplayerid = result["participantIdentities"]
        ## participantId 찾기
        playerid = 0
        for k in range(len(findwin)):
            if findplayerid[k]["player"]["summonerName"] == key:
                playerid = int(findplayerid[k]["participantId"]) - 1
                break
        
        info_set[key][game_id]["win"] = findwin[playerid]["stats"]["win"]

print(info_set)