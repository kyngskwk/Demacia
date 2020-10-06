
# 해당 시간 이전의 승률 데이터로 승률 만들기
# 요소 포탑처치, totalgold, 에픽몬스터, 와드설치, 킬수
# part_set 영상이전 기록,part_set1 영상 시점 기록
# from .timeline import time_part_set
# from .timeline import new_part_set
# from .timeline import gameId
import requests
import json
from collections import OrderedDict
# def winning_rate(part_set,part_set1,gameId):
# videoname = '10-19_KR-4664501922_06.mp4'
# def video(videoname):
def winrate_algo(time_part_set, new_part_set, gameId):
# def final(time_part_set, new_part_set, gameId):
    if time_part_set!= None and new_part_set!= None and gameId != None :
        url = "https://kr.api.riotgames.com/lol/match/v4/matches/"+str(gameId)+"?api_key=RGAPI-4dcd2099-2605-4440-9864-f53a305141e7"
        time_data = requests.get(url).json()["participants"]
        file_path = "./champions.json"
        with open(file_path, "r") as json_file:
            json_data = json.load(json_file)

        champions_records = []
        for t in range(10):
            participantId = time_data[t]["participantId"]
            championId = time_data[t]["championId"]
            for i in range(len(json_data)):
                if championId == int(json_data[i]["key"]):
                    champions_records.append([json_data[i]["id"]])
        # print(champions_records)


        events_creator_id = ["WARD_PLACED"]
        events_killer_id = ["WARD_KILL", "BUILDING_KILL", "CHAMPION_KILL"]
        events_moster_kill = ["ELITE_MONSTER_KILL"]
        # time_part_set = [{}, {'WARD_PLACED': 4, 'totalGold': 4243, 'level': 10, 'totalminionsKilled': 90}, {'WARD_PLACED': 6, 'CHAMPION_KILL': 1, 'WARD_KILL': 1, 'totalGold': 5333, 'level': 9, 'totalminionsKilled': 90}, {'WARD_PLACED': 4, 'CHAMPION_KILL': 3, 'totalGold': 4974, 'level': 11, 'totalminionsKilled': 81}, {'WARD_PLACED': 9, 'CHAMPION_KILL': 1, 'WARD_KILL': 1, 'totalGold': 4311, 'level': 8, 'totalminionsKilled': 87}, {'WARD_PLACED': 
        # 4, 'CHAMPION_KILL': 3, 'WARD_KILL': 4, 'ELITE_MONSTER_KILL': ['FIRE_DRAGON'], 'totalGold': 3448, 'level': 8, 'totalminionsKilled': 11}, {'WARD_PLACED': 7, 'CHAMPION_KILL': 4, 'WARD_KILL': 1, 'totalGold': 8153, 'level': 12, 'totalminionsKilled': 128}, {'WARD_PLACED': 5, 'WARD_KILL': 1, 'ELITE_MONSTER_KILL': ['RIFTHERALD', 'AIR_DRAGON'], 'BUILDING_KILL': 1, 'totalGold': 5783, 'level': 10, 'totalminionsKilled': 104}, {'WARD_PLACED': 7, 'WARD_KILL': 2, 'CHAMPION_KILL': 1, 'totalGold': 4883, 'level': 9, 'totalminionsKilled': 90}, {'CHAMPION_KILL': 8, 'WARD_PLACED': 5, 'BUILDING_KILL': 1, 'totalGold': 5832, 'level': 9, 'totalminionsKilled': 109}, {'WARD_PLACED': 7, 'WARD_KILL': 1, 'CHAMPION_KILL': 1, 'totalGold': 5395, 'level': 9, 'totalminionsKilled': 14}]
        # time_part_set1 = [{}, {}, {}, {'CHAMPION_KILL': 1}, {'WARD_PLACED': 2}, {}, {'WARD_PLACED': 3, 'WARD_KILL': 1}, {'CHAMPION_KILL': 1, 'WARD_PLACED': 1}, {'WARD_PLACED': 2, 'BUILDING_KILL': 1}, {'WARD_PLACED': 2, 'CHAMPION_KILL': 5, 'BUILDING_KILL': 1}, {'WARD_PLACED': 1}]
        # 요소 포탑처치, 킬수, totalgold, 에픽몬스터, 와드설치, 레벨차이
        blueteam = {'WARD_PLACED': 0,'CHAMPION_KILL': 0,'level': 0,'ELITE_MONSTER_KILL': [],'totalGold': 0,'BUILDING_KILL': 0}
        redteam = {'WARD_PLACED': 0,'CHAMPION_KILL': 0,'level': 0,'ELITE_MONSTER_KILL': [],'totalGold': 0,'BUILDING_KILL': 0}
        for i in range(1,11):
            if i <= 5:
                for key,value in time_part_set[i].items():
                    if key in blueteam:
                        blueteam[key] +=time_part_set[i][key]
            else:
                for key,value in time_part_set[i].items():
                    if key in redteam:
                        redteam[key] +=time_part_set[i][key]
        # print(blueteam)
        # print(redteam)
        bluescore = 50
        wardgap = blueteam['WARD_PLACED'] - redteam['WARD_PLACED']
        killgap = blueteam['CHAMPION_KILL'] - redteam['CHAMPION_KILL']
        levelgap = blueteam['level'] - redteam['level']
        goldgap = blueteam['totalGold'] - redteam['totalGold']
        buildinggap = blueteam['BUILDING_KILL'] - redteam['BUILDING_KILL']
        dragongap = len(blueteam['ELITE_MONSTER_KILL']) - len(redteam['ELITE_MONSTER_KILL'])

        # print(wardgap,killgap,levelgap,goldgap,buildinggap,dragongap)
        bluescore += wardgap/5 + killgap*0.5 + levelgap*0.2 + goldgap/7000 + buildinggap*0.5 + dragongap*3
        bluescore = round(bluescore,2)

        redscore = 100-bluescore
        before_bluescore = bluescore
        before_redscore = redscore
        # print(bluescore,'vs',redscore) # 영상 이전 승률

        # ---------------------------------영상 내용이 승률에 영향을 미침 -------------#
        # 초기화
        blueteam1 = {'WARD_PLACED': 0,'CHAMPION_KILL': 0,'level': 0,'ELITE_MONSTER_KILL': [],'totalGold': 0,'BUILDING_KILL': 0}
        redteam1 = {'WARD_PLACED': 0,'CHAMPION_KILL': 0,'level': 0,'ELITE_MONSTER_KILL': [],'totalGold': 0,'BUILDING_KILL': 0}
        for i in range(1,11):
            if i <= 5:
                for key,value in new_part_set[i].items():
                    if key in blueteam:
                        blueteam1[key] +=new_part_set[i][key]
            else:
                for key,value in new_part_set[i].items():
                    if key in redteam:
                        redteam1[key] +=new_part_set[i][key]

        # print(blueteam1)
        # print(redteam1)

        wardgap = blueteam1['WARD_PLACED'] - redteam1['WARD_PLACED']
        killgap = blueteam1['CHAMPION_KILL'] - redteam1['CHAMPION_KILL']
        levelgap = blueteam1['level'] - redteam1['level']
        goldgap = blueteam1['totalGold'] - redteam1['totalGold']
        buildinggap = blueteam1['BUILDING_KILL'] - redteam1['BUILDING_KILL']
        dragongap = len(blueteam1['ELITE_MONSTER_KILL']) - len(redteam1['ELITE_MONSTER_KILL'])
        # print(wardgap,killgap,levelgap,goldgap,buildinggap,dragongap)
        # print(bluescore,wardgap/5 + killgap*0.5 + levelgap*0.2 + goldgap/7000 + buildinggap*0.5 + dragongap*3)
        bluescore += wardgap/5 + killgap*0.5 + levelgap*0.2 + goldgap/7000 + buildinggap*0.5 + dragongap*3
        bluescore = round(bluescore,2)
        redscore = 100-bluescore
        # print(bluescore,'vs',redscore) # 영상 이후 승률
        after_bluescore = bluescore
        after_redscore = redscore


        print(champions_records)
        for i in range(1,11):
            for key,value in new_part_set[i].items():
                champions_records[i-1].append([key,value])
        
        group_data = OrderedDict()
        group_data["before_bluescore"] = before_bluescore
        group_data["before_redscore"] = before_redscore
        group_data["after_bluescore"] = after_bluescore
        group_data["after_redscore"] = after_redscore
        data = []
        for i in range(1,11):
            data.append(str(i))
        for i in range(10):
            champ = data[i]
            champ = OrderedDict()
            champ["name"] = str(champions_records[i][0])
            champ["WARD_PLACED"] = 0
            champ["WARD_KILL"] = 0
            champ["CHAMPION_KILL"] = 0
            champ["ELITE_MONSTER_KILL"] = []
            champ["BUILDING_KILL"] = 0
            group_data[data[i]] = champ

            if len(champions_records[i])>= 2:
                length = len(champions_records[i])
                for k in range(length):
                    if champions_records[i][k][0] == "ELITE_MONSTER_KILL":

                        champ[champions_records[i][k][0]]+=champions_records[i][k][1]
                    elif champions_records[i][k][0] in champ:
                        champ[champions_records[i][k][0]] = champions_records[i][k][1]
        # dict_result = json.dumps(group_data, ensure_ascii=False, indent="\t")
        return group_data
        # for i in range(10):
            # print(champions_records[i])
        # return [before_bluescore, before_redscore, after_bluescore, after_redscore, champions_records]

        # winning_rate( [{}, {'WARD_PLACED': 4, 'totalGold': 4243, 'level': 10, 'totalminionsKilled': 90}, {'WARD_PLACED': 6, 'CHAMPION_KILL': 1, 'WARD_KILL': 1, 'totalGold': 5333, 'level': 9, 'totalminionsKilled': 90}, {'WARD_PLACED': 4, 'CHAMPION_KILL': 3, 'totalGold': 4974, 'level': 11, 'totalminionsKilled': 81}, {'WARD_PLACED': 9, 'CHAMPION_KILL': 1, 'WARD_KILL': 1, 'totalGold': 4311, 'level': 8, 'totalminionsKilled': 87}, {'WARD_PLACED': 
        # 4, 'CHAMPION_KILL': 3, 'WARD_KILL': 4, 'ELITE_MONSTER_KILL': ['FIRE_DRAGON'], 'totalGold': 3448, 'level': 8, 'totalminionsKilled': 11}, {'WARD_PLACED': 7, 'CHAMPION_KILL': 4, 'WARD_KILL': 1, 'totalGold': 8153, 'level': 12, 'totalminionsKilled': 128}, {'WARD_PLACED': 5, 'WARD_KILL': 1, 'ELITE_MONSTER_KILL': ['RIFTHERALD', 'AIR_DRAGON'], 'BUILDING_KILL': 1, 'totalGold': 5783, 'level': 10, 'totalminionsKilled': 104}, {'WARD_PLACED': 7, 'WARD_KILL': 2, 'CHAMPION_KILL': 1, 'totalGold': 4883, 'level': 9, 'totalminionsKilled': 90}, {'CHAMPION_KILL': 8, 'WARD_PLACED': 5, 'BUILDING_KILL': 1, 'totalGold': 5832, 'level': 9, 'totalminionsKilled': 109}, {'WARD_PLACED': 7, 'WARD_KILL': 1, 'CHAMPION_KILL': 1, 'totalGold': 5395, 'level': 9, 'totalminionsKilled': 14}],[{}, {}, {}, {'CHAMPION_KILL': 1}, {'WARD_PLACED': 2}, {}, {'WARD_PLACED': 3, 'WARD_KILL': 1}, {'CHAMPION_KILL': 1, 'WARD_PLACED': 1}, {'WARD_PLACED': 2, 'BUILDING_KILL': 1}, {'WARD_PLACED': 2, 'CHAMPION_KILL': 5, 'BUILDING_KILL': 1}, {'WARD_PLACED': 1}],'4659518008')

        # print("최종결과물",[before_bluescore, before_redscore, after_bluescore, after_redscore, champions_records])

        # print(video('10-19_KR-4664501922_06.mp4'))
    else:
        before_bluescore = None
        before_redscore = None 
        after_bluescore = None 
        after_redscore = None
        champions_records = None
        # print("빈값")
        return 0

