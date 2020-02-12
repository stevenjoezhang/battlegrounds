import codecs, json
import time
with codecs.open('data.json', encoding='utf8') as f:
  database = json.load(f)

def get_minions_by_cost(cost):
  return list(filter(lambda x: x['isBaconPoolMinion'] == True and x['cost'] == cost, database))

def get_deathrattle_minions():
  return list(filter(lambda x: x['isBaconPoolMinion'] == True and x['deathrattle'] == True, database))

def get_legendary_minions():
  return list(filter(lambda x: x['isBaconPoolMinion'] == True and x['legendary'] == True, database))

def get_avail_minions():
  return list(filter(lambda x: x['isBaconPoolMinion'] == True , database))
def get_minion_by_name(name):
  return list(filter(lambda x: x['name'] ==name , database))
#'''
start_time = time.time()
lst=get_minions_by_cost(5)
end_time = time.time()
print (end_time-start_time)
for i in lst:
  print (i)
print (lst)
#'''

