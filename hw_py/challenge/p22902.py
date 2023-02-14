character={
    "name":"기사",
    "level":13,
    "items":{
        "sword":"검",
        "armor":"풀플"
    },
    "skill":["베기","세게 베기","아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for i in character[key]:
            print(i,":",character[key][i])
    elif type(character[key]) is list:
        for j in character[key]:
            print("skill:",j)
    else:
        print(key,":",character[key])