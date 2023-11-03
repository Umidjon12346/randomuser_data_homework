import get_data
import json

def get_gender_users(data:dict) -> list:
    """
    Take the gender of the users and return the list.
    
    The list items are as follows:
        If the user is male: {"Male":1}
        If the user is female: {"Female":0}
    
    Args:
        data(dict): data
    Returns:
        list: users get gender list
    """
    d = {}
    for i in a["results"]: 
        d [i["gender"]]=d.get(i["gender"],0)+1
        return d
data = open("randomuser_data.json").read()
a = json.loads()
print(get_gender_users("randomuser_data.json"))