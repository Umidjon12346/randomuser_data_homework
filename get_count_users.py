import get_data
import json

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    s = 0
    for i in a["results"]:
        if i["login"]["username"] in a["results"]:
            s+=1
    return s
data = open("randomuser_data.json").read()
a = json.loads(data)
print(get_count_users("randomuser_data.json"))
    
