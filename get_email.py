import get_data
import json

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    a = []
    for i in s["results"]:
        a.append(i["email"])
    return a
data = open("randomuser_data.json").read()
s = json.loads(data)
print(get_email("randomuser_data.json"))