import requests
import json
import datetime
import re



def prob_to_tchkzpt(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, ';', str(s))


query = 'super'

print(prob_to_tchkzpt(query))

for p in range(1, 5):
    r = requests.get('http://api.stackexchange.com/2.2/search?', 
        params = {
        'page' : p,
        'order' : 'desc', 
        'sort' : 'activity', 
        'tagged' : prob_to_tchkzpt(query),
        'site' : 'stackoverflow',
        'pagesize' : 5
        }
        ).json()
    print(r)

    for i in range(len(r['items'])):
        title = r['items'][i]['title']
        name = r['items'][i]['owner']['display_name']
        label = str(query)
        print(title, name, label)

# result = DBSession.query(Search).filter_by(label=str(query)).all()

# print(result)