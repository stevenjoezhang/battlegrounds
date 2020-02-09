import codecs, json

with codecs.open('data.json', encoding='utf8') as f:
  database = json.load(f)

def get_minions_by_cost(cost):
  return list(filter(lambda x: x['cost'] == cost, database))

def get_deathrattle_minions():
  return list(filter(lambda x: x['deathrattle'] == True, database))

def get_legendary_minions():
  return list(filter(lambda x: x['legendary'] == True, database))
