import get_data as get
import json

def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
  
    a = []
    for i in s["results"] :
        d = {}
        d["first_name"] = i["name"]["first"]
        d["last_name"] = i["name"]["last"]
        d["phone_number"] = i["phone"]
        a.append(d)
    return a
data=open("randomuser_data.json").read()
s = json.loads(data)  
print(get_users_data("randomuser_data.json"))
