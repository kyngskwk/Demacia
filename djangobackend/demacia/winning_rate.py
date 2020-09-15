from account_id import account_ids
import requests
import json

#game_id 추출
#match-v4-accountid
game_ids = []
for account_id in account_ids:
    match_v4_accountid = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/"+str(account_id)+"?api_key=RGAPI-4dcd2099-2605-4440-9864-f53a305141e7"
    results = requests.get(match_v4_accountid).json()["matches"]
    for i in range(len(results)):
        game_ids.append(results[i]["gameId"])

game_ids = list(set(game_ids)) # game_Ids 집합으로 해야함

champion_info = dict() # "timo" : [이긴횟수, 진횟수]
champion id 별 이긴횟수, 진횟수 딕셔너리 만들기
match-v4-gameid
for game_id in game_ids:
    match_v4_gameId ="https://kr.api.riotgames.com/lol/match/v4/matches/"+str(game_id)+"?api_key=RGAPI-4dcd2099-2605-4440-9864-f53a305141e7"
    results = requests.get(match_v4_gameId).json()["teams"]
    for team in results:
        if team["win"] == "Fail":
            for champ in team["bans"]:
                if champ["championId"] not in champion_info:
                    champion_info[champ["championId"]] = [0,1]
                else:
                    champion_info[champ["championId"]][1] += 1
        elif team["win"] == "Win":
            for champ in team["bans"]:
                if champ["championId"] not in champion_info:
                    champion_info[champ["championId"]] = [1,0]
                else:
                    champion_info[champ["championId"]][0] += 1


# 확률 구하기
champion_winnig_rate = dict()
for champion_id in champion_info:
    champion_winnig_rate[champion_id] = champion_info[champion_id][0] / sum(champion_info[champion_id])
