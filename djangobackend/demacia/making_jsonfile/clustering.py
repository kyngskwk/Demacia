import json # import json module

# with statement
with open('champion_stats.json') as json_file:
    json_data = json.load(json_file)

    json_string = json_data[0]
    print(json_string)