from flask import Flask, jsonify

from multiprocessing import Process, Queue, cpu_count
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='', static_folder='public')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

from battle import minion, battlefeild, battle

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
    ba=battlefeild()
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
