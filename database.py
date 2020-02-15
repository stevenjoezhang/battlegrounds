import codecs, json
#import time
#import battle
zap={'name': 'Zapp Slywick', 'nameCN': '扎普·斯里维克', 'id': 'BGS_022', 'goldenId': 'TB_BaconUps_091', 'tier': 6, 'tribe': 'None', 'atk': 7, 'health': 10, 'taunt': False, 'divineShield': False, 'poisonous': False, 'windfury': True, 'deathrattle': False, 'cleave': False, 'legendary': False, 'isBaconPoolMinion': True, 'cost': 8}
with codecs.open('data.json', encoding='utf8') as f:
  database = json.load(f)

def get_minions_by_cost(cost):
  return list(filter(lambda x: x['isBaconPoolMinion'] == True and x['cost'] == cost, database))

def get_deathrattle_minions():
  lst=list(filter(lambda x: x['isBaconPoolMinion'] == True and x['deathrattle'] == True, database))
  del lst[-3]
  return lst

def get_legendary_minions():
  lst=list(filter(lambda x: x['isBaconPoolMinion'] == True and x['legendary'] == True, database))[:-1]
  lst.append(zap)
  return lst

def get_avail_minions():
  return list(filter(lambda x: x['isBaconPoolMinion'] == True , database))
def get_minions_by_name(name):
  return list(filter(lambda x: x['name'] ==name , database))
def get_minions_by_tribe(name):
  return list(filter(lambda x: x['tribe'] ==name , database))
def get_uncollect_minions():
  return list(filter(lambda x: x['isBaconPoolMinion'] == False, database))
def get_names():
  lst=list(filter(lambda x: x['isBaconPoolMinion'] == True , database))
  lst1=[]
  for i in lst:
    lst1.append(i["name"])
  return lst1
'''
#start_time = time.time()
lst= get_names()
lst1=get_uncollect_minions()
#end_time = time.time()
#print (end_time-start_time)
print (lst)
print ("\n")
for i in lst1:
  print (i)

 # '''
'''
a=battle.minion("cat",1,1)
b=a.copy()
b.set_name("dog")
print (a,b)
'''

