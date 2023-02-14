dictionary={
    "name":"기사",
    "level":13,
    "items":{
        "sword":"검",
        "armor":"풀플"
    },
    "skill":["베기","세게 베기","아주 세게 베기"]
}

for key in dictionary:
    if type(dictionary[key])==str:
        print(key,":",dictionary[key])
    elif type(dictionary[key])==int:
        print(key,":",dictionary[key])
    elif type(dictionary[key])==dict:
        print(key,":",dictionary[key])
    else:
        print(key,":",dictionary[key])