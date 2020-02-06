import random
from copy import deepcopy
ch_list=("beast","murloc","mech","demon","all")
special_list=("dire_worf_alpha","murloc_warleader","phalanx_commander","siege_breaker","malganis","oldmurkeye")
#m_b_list=("dire_worf_alpha","murloc_warleader","phalanx_commander","siege_breaker","malganis","oldmurkeye")
#d_s_list=("Mecharoo","")
class minion:
    def __init__(self,na="",at=0,he=0,ch="",t=False,sh=False,p=False,w=False,d=0,m=0,g=False,spe=""):
        self.name= na
        self.attack = at
        self.health= he
        self.character=ch  #种族
        self.taunt=t
        self.shield=sh
        self.poison=p
        self.wind=w
        self.damage=d
        self.move=m #这一轮是否动过,0 未动，1动过，2待定
        self.buff=[0,0] #记录临时的minion_buff，永久的buff直接在health和attack上加
        self.golden=g
        self.special=spe #特殊描述，为一个二维元组，第一个为special_list里的，第二个为细分的list里的

    def set_attack(self,at):
        self.attack+=at
        if self.attack<=0:
            print ("error: wrong set attack")

    def get_attack(self):
        return self.attack

    def set_name(self,na):
        self.name=na

    def get_name(self):
        return self.name

    def set_health(self, he):
        self.health+=he
        if self.health <=0:
            print ("error: wrong set health")

    def get_health(self):
        return self.health

    def set_damage(self, da):
        self.damage+=da

    def remove_damage(self):
        self.damage=0

    def get_damage(self):
        return self.damage

    def set_move(self, mo):
        if mo!=0 and mo!=1 and mo!=2:
            print ("error: wrong state")
        else:
            self.move=mo

    def get_move(self):
        return self.move

    def set_character(self, ch):
        if ch in ch_list:
            self.character = ch
        else:
            print ("error: wrong character set")

    def get_character(self):
        return self.character

    def set_shield(self,sh):
        if str(sh)== "True" or str(sh)=="False":
            self.shield = sh
        else:
            print ("error: wrong shield set")

    def get_shield(self):
        return self.shield

    def set_golden(self, go):
        if str(go)== "True" or str(go)=="False":
            self.golden = go
        else:
            print ("error: wrong golden set")

    def get_golden(self):
        return self.golden

    def set_taunt(self,t):
        if str(t)== "True" or str(t)=="False":
            self.taunt = t
        else:
            print ("error: wrong taunt set")

    def get_taunt(self):
        return self.taunt

    def set_poison(self,p):
        if str(p)== "True" or str(p)=="False":
            self.poison = p
        else:
            print ("error: wrong poison set")

    def get_posion(self):
        return self.poison

    def set_wind(self,w):
        if str(w)== "True" or str(w)=="False":
            self.wind = w
        else:
            print ("error: wrong wind set")

    def get_wind(self):
        return self.wind

    def set_buff(self,lst):
        if len(lst)==2:
            self.buff[0] += lst[0]
            self.buff[1]+=lst[1]
        else:
            print ("error: wrong buff set")

    def get_buff_attack(self):
        return self.buff[0]

    def get_buff_health(self):
        return self.buff[1]

    def remove_buff(self):
        self.buff=[0,0]

    def set_special(self,sp):
        if sp in special_list:
            self.special=sp
        else:
            print ("error: wrong special set")

    def get_special(self):
        return self.special

    def __str__(self):
        return "name "+self.name+" attack "+str(self.attack)+"+"+str(self.buff[0])+" health "+str(self.health)+"+"+str(self.buff[1])+" damage "+str(self.damage)+" shield "+str(self.shield)+" "+self.special

    def minion_attack(self,other):
          if self.shield:
              self.set_shield(False)
          elif other.poison:
              self.set_damage(10000) #poison is 10000 attack
          else:
              self.set_damage(other.attack+other.buff[0])
             # print (self.damage)

    def __eq__(self, other):
        if self.name==other.name:
            return True
        else:
            return False

    def get_calculated_health(self):
        return self.get_health()+self.get_buff_health()-self.get_damage()

    def get_calculated_attack(self):
        return self.get_attack()+self.get_buff_attack()

def origin_minion_buff(lst):  #所有minion_buff
    minionlist=len(lst)
    for i in range(minionlist):
        if lst[i].get_special()=="dire_worf_alpha":
            if minionlist==1:
                pass
            elif i==0:
                if lst[i].get_golden():
                    lst[i+1].set_attack(-2)
                    lst[i+1].set_buff([2,0])
                else:
                    lst[i + 1].set_attack(-1)
                    lst[i + 1].set_buff([1, 0])
            elif i==minionlist-1:
                if lst[i].get_golden():
                    lst[i-1].set_attack(-2)
                    lst[i-1].set_buff([2,0])
                else:
                    lst[i - 1].set_attack(-1)
                    lst[i - 1].set_buff([1, 0])
            else:
                if lst[i].get_golden():
                    lst[i-1].set_attack(-2)
                    lst[i-1].set_buff([2,0])
                    lst[i + 1].set_attack(-2)
                    lst[i + 1].set_buff([2, 0])
                else:
                    lst[i - 1].set_attack(-1)
                    lst[i - 1].set_buff([1, 0])
                    lst[i + 1].set_attack(-1)
                    lst[i + 1].set_buff([1, 0])
        elif lst[i].get_special()=="murloc_warleader":
            for j in range(minionlist):
                if j==i:
                    pass
                else:
                    if lst[j].get_character()==("murloc" or "all"):
                        if lst[i].get_golden():
                            lst[j].set_attack(-4)
                            lst[j].set_buff([4, 0])
                        else:
                            lst[j].set_attack(-2)
                            lst[j].set_buff([2, 0])
        elif lst[i].get_special()=="phalanx_commander":
            for j in range(minionlist):
                if lst[j].get_taunt():
                    if lst[i].get_golden():
                        lst[j].set_attack(-4)
                        lst[j].set_buff([4, 0])
                    else:
                        lst[j].set_attack(-2)
                        lst[j].set_buff([2, 0])
        elif lst[i].get_special()=="siege_breaker":
            for j in range(minionlist):
                if j == i:
                    pass
                else:
                    if lst[j].get_character() == ("demon" or  "all"):
                        if lst[i].get_golden():
                            lst[j].set_attack(-2)
                            lst[j].set_buff([2, 0])
                        else:
                            lst[j].set_attack(-1)
                            lst[j].set_buff([1, 0])
        elif lst[i].get_special() == "malganis":
            for j in range(minionlist):
                if j == i:
                    pass
                else:
                    if lst[j].get_character() == ("demon" or  "all"):
                        if lst[i].get_golden():
                            lst[j].set_attack(-4)
                            lst[j].set_health(-4)
                            lst[j].set_buff([4, 4])
                        else:
                            lst[j].set_attack(-2)
                            lst[j].set_health(-2)
                            lst[j].set_buff([2, 2])
        else:
            pass
def add_minion_buff(lst):  #所有minion_buff
    minionlist=len(lst)
    for i in range(minionlist):
        if lst[i].get_special()=="dire_worf_alpha":
            if minionlist==1:
                pass
            elif i==0:
                if lst[i].get_golden():
                    lst[i+1].set_buff([2,0])
                else:
                    lst[i + 1].set_buff([1, 0])
            elif i==minionlist-1:
                if lst[i].get_golden():
                    lst[i-1].set_buff([2,0])
                else:
                    lst[i - 1].set_buff([1, 0])
            else:
                if lst[i].get_golden():
                    lst[i-1].set_buff([2,0])
                    lst[i + 1].set_buff([2, 0])
                else:
                    lst[i - 1].set_buff([1, 0])
                    lst[i + 1].set_buff([1, 0])
        elif lst[i].get_special()=="murloc_warleader":
            for j in range(minionlist):
                if j==i:
                    pass
                else:
                    if lst[j].get_character()==("murloc" or "all"):
                        if lst[i].get_golden():
                            lst[j].set_buff([4, 0])
                        else:
                            lst[j].set_buff([2, 0])
        elif lst[i].get_special()=="phalanx_commander":
            for j in range(minionlist):
                if lst[j].get_taunt():
                    if lst[i].get_golden():
                        lst[j].set_buff([4, 0])
                    else:
                        lst[j].set_buff([2, 0])
        elif lst[i].get_special()=="siege_breaker":
            for j in range(minionlist):
                if j == i:
                    pass
                else:
                    if lst[j].get_character() == ("demon" or  "all"):
                        if lst[i].get_golden():
                            lst[j].set_buff([2, 0])
                        else:
                            lst[j].set_buff([1, 0])
        elif lst[i].get_special() == "malganis":
            for j in range(minionlist):
                if j == i:
                    pass
                else:
                    if lst[j].get_character() == ("demon" or  "all"):
                        if lst[i].get_golden():
                            lst[j].set_buff([4, 4])
                        else:
                            lst[j].set_buff([2, 2])
        else:
            pass

class battlefeild:
    def __init__(self, up=[], down=[]):
        self.up = up #记录上方
        self.down = down #记录下方
        #self.begin=None #True 表示上面先动
        self.now =None  #表示运行到第几个,第一表示该第几个，第二表示示该上方或下方,True 表示上方
        #self.special_minion=[]

    def set_now(self,num,side):
        if num>6 or num<0:
            print ("error: wrong position")
        elif str(side) !="True" and str(side) !="False":
            print ("error: wrong side")
        else:
            self.now=[num,side]

    def add_minion(self,mi,side,pos):
        if side=="up":
            if pos>=0 and len(self.up)+1 <= 7:
                self.up.insert(pos,mi)  #这里注意如果列表只有4个minion，直接插入第六个会使其变成第五而不是第六
            else:
                print ("error: wrong position to add a minion1")
        elif side=="down":
            if pos>=0 and len(self.up)+1 <= 7:
                self.down.insert(pos,mi)  #这里注意如果列表只有4个minion，直接插入第六个会使其变成第五而不是第六
            else:
                print ("error: wrong position to add a minion2")
        else:
            print ("error:wrong side to add a minion")

    def up_minion(self):
        return len(self.up)

    def get_up(self):
        return self.up

    def get_down(self):
        return self.down

    def down_minion(self):
        return  len(self.down)

    def battle_begin(self):  #确定开始方和处理minion_buff
        minionup=len(self.up)
        miniondown=len(self.down)
        if minionup> miniondown:
            #self.begin=True
            self.set_now(0,True)
        elif minionup< miniondown:
            #self.begin=False
            self.set_now(0, False)
        else:
            a=random.random()
            if a>=0.5:
               # self.begin = True
                self.set_now(0, True)
            else:
                #self.begin =False
                self.set_now(0,False)
        origin_minion_buff(self.up)
        origin_minion_buff(self.down)#oldmurkeye比较特殊，考虑对面,专门处理
        murloc_num=0
        for i in self.up:
            if i.get_character()==("murloc" or "all"):
                murloc_num+=1
        for i in self.down:
            if i.get_character()==("murloc" or "all"):
                murloc_num+=1
        for i in self.up:
            if i.get_special() == "oldmurkeye":
                if i.get_golden():
                    i.set_attack(-2*(murloc_num-1))
                    i.set_buff([2*(murloc_num-1), 0])
                else:
                    i.set_attack(-(murloc_num-1))
                    i.set_buff([murloc_num-1, 0])
        for i in self.down:
            if i.get_special() == "oldmurkeye":
                if i.get_golden():
                    i.set_attack(-2*(murloc_num-1))
                    i.set_buff([2*(murloc_num-1), 0])
                else:
                    i.set_attack(-(murloc_num-1))
                    i.set_buff([murloc_num-1, 0])

    def minion_select(self): #side 是动的那边,选择另一边的目标
        side=self.now[1]
        if  str(side) !="True" and str(side) !="False":
            print ("error: which side to attack")
        elif side:
            num=[]
            for i in range(len(self.down)):
                if self.down[i].get_taunt():
                    num.append(i)
            if len(num)==0:
                return random.randint(0,len(self.down)-1)
            elif len(num)>0 and len(num)<len(self.down):
                return num[random.randint(0, len(num)-1)]
            else:
                print ("error: wrong select 1")
        else:
            num = []
            for i in range(len(self.up)):
                if self.up[i].get_taunt():
                    num.append(i)
            if len(num) == 0:
                return random.randint(0, len(self.up) - 1)
            elif len(num) > 0 and len(num) < len(self.up):
                return num[random.randint(0, len(num) - 1)]
            else:
                print ("error: wrong select 2")

    def minion_battle(self,j):
            if self.now[1]:
                i=self.now[0]
                if j > len(self.down) - 1 or j < 0:
                    print ("error:wrong battle object1")
                else:
                    self.up[i].minion_attack(self.down[j])
                    self.down[j].minion_attack(self.up[i])   #这里要考虑狂战问题
                    self.up[i].set_move(2)
                print("ATTACK UP{} DOWN{}".format(i, j))
            else:
                i = self.now[0]
                if j > len(self.up) - 1 or j < 0:
                    print ("error:wrong battle object1")
                else:
                    self.down[i].minion_attack(self.up[j])
                    self.up[j].minion_attack(self.down[i])  # 这里要考虑狂战问题
                    self.down[i].set_move(2)
                print("ATTACK DOWN{} UP{}".format(i, j))

    def detect_death(self):
        up1=[]
        down1=[]
        for i in range(len(self.up)):
            if self.up[i].get_damage()>= (self.up[i].get_health()+self.up[i].get_buff_health()):
                #print (self.up[i].get_damage(),self.up[i].get_health()+self.up[i].get_buff_health(),"up")
                up1.append(i)
        for j in range(len(self.down)):
            if self.down[j].get_damage()>= (self.down[j].get_health()+self.down[j].get_buff_health()):
                #print (self.down[j].get_damage(),self.down[j].get_health()+self.down[j].get_buff_health(),"down")
                down1.append(j)
       # print (down1)
        for i in up1:
            del self.up[i]
        for j in down1:
            del self.down[j]

    def summon(self,lst):
        pass

    def renew_attack(self):
        side= not self.now[1]
        uppos,downpos=-1,-1
        if self.now[1]:  #移除待定替换为已动，注意有奇怪的延迟，刚行动的马上被对面移除，子产物会行动，移动待定状态会延迟一回合
            for i in self.down:
                if i.get_move()==2:
                    i.set_move(1)
        else:
            for i in self.up:
                if i.get_move()==2:
                    i.set_move(1)
        if side:
            for i in range(len(self.up)):
                if self.up[i].get_move()==0:
                    uppos=i
                    break
            if uppos==-1:
                uppos=0
                for i in self.up:
                    i.set_move(0)
            self.set_now(uppos,side)
        else:
            for j in range(len(self.down)):
                if self.down[j].get_move()==0:
                    downpos=j
                    break
            if downpos==-1:
                downpos=0
                for i in self.down:
                    i.set_move(0)
            self.set_now(downpos, side)

    def renew_buff(self):
        temp_up=[]
        temp_down=[]
        murloc_num = 0
        for i in self.up:
            temp_up.append(i.get_buff_health())
            i.remove_buff()
            if i.get_character() == ("murloc" or "all"):
                murloc_num += 1
        for i in self.down:
            temp_down.append(i.get_buff_health())
            i.remove_buff()
            if i.get_character() == ("murloc" or "all"):
                murloc_num += 1
        add_minion_buff(self.up)
        add_minion_buff(self.down)
        for i in range(len(self.up)):
            if self.up[i].get_special() == "oldmurkeye":
                if self.up[i].get_golden():
                    self.up[i].set_buff([2 * (murloc_num - 1), 0])
                else:
                    self.up[i].set_buff([murloc_num - 1, 0])
            if temp_up[i]- self.up[i].get_buff_health()>self.up[i].get_damage():
                self.up[i].remove_damage()
            elif temp_up[i]- self.up[i].get_buff_health()>0:
                self.up[i].set_damage(self.up[i].get_buff_health()-temp_up[i])
            else:
                pass
        for i in range(len(self.down)):
            if self.down[i].get_special() == "oldmurkeye":
                if self.down[i].get_golden():
                    self.down[i].set_buff([2 * (murloc_num - 1), 0])
                else:
                    self.down[i].set_buff([murloc_num - 1, 0])
            if temp_down[i]- self.down[i].get_buff_health()>self.down[i].get_damage():
                self.down[i].remove_damage()
            elif temp_down[i]- self.down[i].get_buff_health()>0:
                self.down[i].set_damage(self.down[i].get_buff_health()-temp_down[i])
            else:
                pass

    def __str__(self):
        str1="up:\n"
        for i in self.up:
            str1+=str(i)+"\n"
        str1+="down:\n"
        for i in self.down:
            str1+=str(i)+"\n"
        str1+="now:"+str(self.now)
        return str1

def battle(field):
    field.battle_begin()
    #print (field,"\n")
    lst=[deepcopy(field)]
    while field.up_minion()>0 and field.down_minion()>0:
        num=field.minion_select()
        field.minion_battle(num)
        field.detect_death()
        field.renew_attack()
        field.renew_buff()
        lst.append(deepcopy(field))
        #print (field,"\n")
    return lst

a=minion("cat",10,11,spe="murloc_warleader",g=True,ch="murloc")
b=minion("dog",3,12,p=True,ch="murloc")
c=minion("cat",10,10,sh=True,ch="murloc")
d=minion("cat",10,11,sh=True,ch="murloc")
e=minion("cat",10,10,ch="murloc")
f=minion("cat",10,10,sh=True,ch="murloc",spe="oldmurkeye")
g=minion("test",5,3,sh=True,ch="murloc")
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
a=battle(ba)

print(a[0].get_up()[0].get_calculated_health())
'''
lst=[0,2,3]
lst.insert(6,'x')
print (lst,len(lst))
'''
db = []
for i in range(len(a)):
    up = []
    target = a[i].get_up()
    for k in range(len(target)):
        index = target[k].get_name()
        health = target[k].get_calculated_health()
        attack = target[k].get_calculated_attack()
        shield = target[k].get_shield()
        up.append([index, health, attack, shield])
    down = []
    target = a[i].get_down()
    for k in range(len(target)):
        index = target[k].get_name()
        health = target[k].get_calculated_health()
        attack = target[k].get_calculated_attack()
        shield = target[k].get_shield()
        down.append([index, health, attack, shield])
    db.append([up, down])

import json
import codecs
with codecs.open('datahs.json', 'w', encoding='utf8') as outfile:
    json.dump(db, outfile, ensure_ascii=False)
