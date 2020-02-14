from flask import Flask, jsonify

from multiprocessing import Process, Queue, cpu_count
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='', static_folder='public')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

from battle import minion, battlefeild, battle
import test

def run(queue):
    ba=test.test13()
    battle(ba)
    queue.put([ba.history,ba.atkHistory,ba.log])

import codecs, json

with codecs.open('data.json', encoding='utf8') as f:
  database = json.load(f)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/data.json')
def data():
    return jsonify(database)

@app.route('/battle.json')
def battledata():
    q = Queue()
    spawn = Process(target = run, args = (q,))
    spawn.start()
    t = q.get()
    t.append(1000)
    #print(len(t[0]), len(t[1]))
    spawn.join()
    return jsonify(t)

if __name__ == "__main__":
    app.run(port=8080, debug=False)
