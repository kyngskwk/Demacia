import requests
import json
from pprint import pprint

# 호니 코드 불러올 예정
champion_winnig_rate = dict()
# mbti 조합 dict mbti : [좋은조합, 나쁜조합]
mbti_couple = {
    'entj': ['isfp', 'isfj'],
    'entp': ['isfj', 'isfp'],
    'intj': ['esfp', 'esfj'],
    'intp': ['esfj', 'esfp'],
    'estj': ['infp', 'infj'],
    'esfj': ['intp', 'intj'],
    'istj': ['enfp', 'enfj'],
    'isfj': ['entp', 'entj'],
    'enfj': ['istp', 'istj'],
    'enfp': ['istj', 'istp'],
    'infj': ['estp', 'estj'],
    'infp': ['estj', 'estp'],
    'estp': ['infj', 'infp'],
    'esfp': ['intj', 'intp'],
    'istp': ['enfj', 'enfp'],
    'isfp': ['entj', 'entp']
} 


result = []
with open('champions.json', 'r') as chams:

    cham_infos = json.load(chams)
    for cham_info in cham_infos:
        table = {}
        table["models"] = "appname.champion"
        table["pk"] = cham_info["key"]
        cham_id = cham_info["key"]

        # 필드 채우기
        table["fields"] = {}
        table["fields"]["chamkey"] = cham_id
        table["fields"]["chamname"] = cham_info["id"]
        table["fields"]["chamtags"] = cham_info["tags"]
        # table["fields"]["partype"] = ''

        # 챔피언 딕셔너리
        table["fields"]["dictionary"] = ''

        # 챔피언 라인
        table["fields"]["lane"] = cham_info["lane"]
        
        # 챔피언 mbti
        # cham_mbti = cham_info["?????"]
        # table["fields"]["mbti"] = cham_mbti
        table["fields"]["mbti"] = ''

        # 챔피언별 승률
        table["fields"]["winningRate"] = '' 
        # 코드 불러온 후
        # table["fields"]["winningRate"] = champion_winnig_rate[cham_id]

        # mbti 좋은 조합
        table["fields"]["goodmbti"] = '' 
        # table["fields"]["goodmbti"] = mbti_couple["cham_mbti"][0]


        # mbti 나쁜 조합
        table["fields"]["badmbti"] = '' 
        # table["fields"]["goodmbti"] = mbti_couple["cham_mbti"][1]


        result.append(table)

with open('cham.json', 'w', encoding="UTF-8") as make_file:
    json.dump(result, make_file, indent="\t")