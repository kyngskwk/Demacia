import requests
import json
# from .change_text import new_time as time1
# from .change_text import gameId


def timeline(time1, gameId):
    if time1 == None or gameId == None:
        time_part_set = None
        new_part_set = None
        gameId = None
    else:
    # def live_and_before(time1,gameId):
        time = []
        for t in range(int(time1[0][0])+1,int(time1[1][0])+2):
            time.append(t)
        # print(time)
        # print(gameId)
        url = "https://kr.api.riotgames.com/lol/match/v4/timelines/by-match/"+str(gameId)+"?api_key=RGAPI-4dcd2099-2605-4440-9864-f53a305141e7"
        time_data = requests.get(url).json()["frames"]
        # print(time_data)

        # 필수 이벤트
        events_creator_id = ["WARD_PLACED"]
        events_killer_id = ["WARD_KILL", "BUILDING_KILL", "CHAMPION_KILL"]
        events_moster_kill = ["ELITE_MONSTER_KILL"]

        time_part_set = [dict() for _ in range(11)]
        # print(time_part_set)
        time_set = dict()

        #------------------------ 영상 이전 기록-----------------------------------------
        for t in range(1,time[0]+1):
            events = time_data[t]["events"]
            for event in events:
                # 이벤트가 필수 이벤트(creatorId)라면
                if event["type"] in events_creator_id:
                    real_event = event["type"]
                    # 해당 인덱스의 dict에 횟수를 누적한다
                    time_part_set[event["creatorId"]].setdefault(real_event, 0)
                    time_part_set[event["creatorId"]][real_event] += 1

                # 이벤트가 필수 이벤트(killerId)라면
                elif event["type"] in events_killer_id:
                    real_event = event["type"]
                    # 해당 인덱스의 dict에 횟수를 누적한다
                    time_part_set[event["killerId"]].setdefault(real_event, 0)
                    time_part_set[event["killerId"]][real_event] += 1
                
                # 이벤트가 필수 이벤트(monsterkill)라면
                elif event["type"] in events_moster_kill:
                    real_event = event["type"]
                    # 해당 인덱스의 dict에 횟수를 누적한다
                    time_part_set[event["killerId"]].setdefault(real_event, [])
                    if event["monsterType"] == "DRAGON":
                        time_part_set[event["killerId"]][real_event] += [event["monsterSubType"]]
                    else:
                        time_part_set[event["killerId"]][real_event] += [event["monsterType"]]


            
            # 사건 직전 누적 골드
            if t == time[0]:
                part_info = time_data[t]["participantFrames"]
                # 1번 부터 10번까지 누적 기록 저장
                for idx in range(1, 11):
                    time_part_set[idx]["totalGold"] = part_info[str(idx)]["totalGold"]
                    time_part_set[idx]["level"] = part_info[str(idx)]["level"]
                    time_part_set[idx]["totalminionsKilled"] = part_info[str(idx)]["minionsKilled"] + part_info[str(idx)]["jungleMinionsKilled"]


        # print(part_set)


        #---------------------------------------영상 실시간 기록---------------------------------

        new_part_set = [dict() for _ in range(11)]
        # print(part_set)
        time_set1 = dict()
        for t in time:
            events = time_data[t]["events"]
            for event in events:
                # 이벤트가 필수 이벤트(creatorId)라면
                if event["type"] in events_creator_id:
                    real_event = event["type"]
                    # 해당 인덱스의 dict에 횟수를 누적한다
                    new_part_set[event["creatorId"]].setdefault(real_event, 0)
                    new_part_set[event["creatorId"]][real_event] += 1

                # 이벤트가 필수 이벤트(killerId)라면
                elif event["type"] in events_killer_id:
                    real_event = event["type"]
                    # 해당 인덱스의 dict에 횟수를 누적한다
                    new_part_set[event["killerId"]].setdefault(real_event, 0)
                    new_part_set[event["killerId"]][real_event] += 1
                
                # 이벤트가 필수 이벤트(monsterkill)라면
                elif event["type"] in events_moster_kill:
                    real_event = event["type"]
                    # 해당 인덱스의 dict에 횟수를 누적한다
                    new_part_set[event["killerId"]].setdefault(real_event, [])
                    new_part_set[event["killerId"]][real_event] += [event["monsterType"]]

            # print(new_part_set)
            # winrate_algo.winning_rate(part_set,new_part_set,gameId)
    return time_part_set, new_part_set, gameId
