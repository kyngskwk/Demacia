import requests
import json
import random

api_list = ['RGAPI-4dcd2099-2605-4440-9864-f53a305141e7', 'RGAPI-aced2823-ded5-4dce-89a6-c71484eb1227', 'RGAPI-268abef3-0d99-4311-b006-c5c9a9fc8120']
api = random.choice(api_list)
print(api)


nickname = 'Hide on Bush'

nicktoid = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+ str(nickname)+ "?api_key=" + str(api)
results = requests.get(nicktoid).json()
try:
    accountid = results['accountId']
except KeyError:
    print("사용자가 너무 많아 조금 후 다시 시도해주세요ㅠㅠ")

print(accountid)
accidtogameid = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + str(accountid) + "?endIndex=10&api_key=" + str(api)

result_set = {}

try:
    results = requests.get(accidtogameid).json()["matches"]
    # print(results)

    for idx in range(len(results)):
        game_id = results[idx]["gameId"]
        # print(game_id)
        # info_set[key]['games'][game_id] = results[idx]

        info = "https://kr.api.riotgames.com/lol/match/v4/matches/"+str(game_id)+"?api_key=" + str(api)
        result = requests.get(info).json()
    
        try:
            findwin = result["participants"]
            findplayerid = result["participantIdentities"]
            # print(findplayerid)
            ## participantId 찾기
            playerid = 0
            for k in range(len(findwin)):
                if findplayerid[k]["player"]["summonerName"] == nickname:
                    playerid = int(findplayerid[k]["participantId"]) - 1
                    break
            
            results[idx]["win"] = findwin[playerid]["stats"]["win"]
            results[idx]["kills"] = findwin[playerid]["stats"]["kills"]
            results[idx]["deaths"] = findwin[playerid]["stats"]["deaths"]
            results[idx]["assists"] = findwin[playerid]["stats"]["assists"]

        except KeyError:
            print("사용자가 너무 많아 조금 후 다시 시도해주세요ㅠㅠ")
            

except KeyError:
    print("사용자가 너무 많아 조금 후 다시 시도해주세요ㅠㅠ")

# print(results)