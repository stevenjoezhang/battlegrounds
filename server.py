from flask import Flask, jsonify

from multiprocessing import Process, Queue, cpu_count
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='', static_folder='public')

from battle import minion, battlefeild

class mimibattlefeild(battlefeild):
    def __init__(self, *args, **kwargs):
        super(mimibattlefeild, self).__init__(*args, **kwargs)
        self.history = []
        self.atkHistory = []
        self.log = ""
    def dump(self):
        self.log += self.__str__() + "\n";
        #print (self,"\n")
        #print(self.history)
        current = {
            "up": [],
            "down": []
        }
        for [name, board] in [["up", self.up], ["down", self.down]]:
            for minion in board:
                current[name].append({
                    "id": id(minion),
                    "atk": minion.get_calculated_attack(),
                    "health": minion.get_calculated_health(),
                    "shield": minion.get_shield(),
                    "taunt": minion.get_taunt(),
                    "poison": minion.get_posion()
                })
        self.history.append(current)

def battle(field):
    field.battle_begin()
    field.dump()
    while field.up_minion()>0 and field.down_minion()>0:
        attack_list=field.minion_battle()
        field.atkHistory.append(attack_list)
        #print (attack_list)
        field.minion_battle()
        #field.detect_death()
        field.remove_death()
        field.renew_attack()
        field.renew_buff()
        field.dump()

def run(queue):
    a=minion("cat",10,11,spe="the_boogeymonster",g=True,ch="murloc")
    b=minion("dog",3,12,p=True,ch="murloc")
    c=minion("cat",10,11,ch="murloc")
    d=minion("cat",10,11,ch="murloc")
    e=minion("cat",10,11,ch="murloc")
    f=minion("cat",10,11,ch="murloc",spe="oldmurkeye")
    g=minion("test",1,3,sh=True,t=True,ch="murloc")
    #a.minion_attack(b)
    #a.minion_attack(b)
    #a.set_attack(2)
    ba=mimibattlefeild()
    ba.add_minion(a,"up",0)
    ba.add_minion(c,"up",1)
    ba.add_minion(e,"up",2)
    ba.add_minion(b,"down",0)
    ba.add_minion(d,"down",0)
    ba.add_minion(f,"down",0)
    ba.add_minion(g,"down",0)
    battle(ba)
    queue.put([ba.history,ba.atkHistory,ba.log])

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/battle.json')
def data():
    q = Queue()
    spawn = Process(target = run, args = (q,))
    spawn.start()
    t = q.get()
    #print(len(t[0]), len(t[1]))
    spawn.join()
    return jsonify(t)

if __name__ == "__main__":
    app.run(port=8080, debug=False)
