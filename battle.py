import random
import database
import itertools
import copy
ch_list=("Beast","Murloc","Mech","Demon","All")
special_list=("Dire Wolf Alpha","Murloc Warleader","Phalanx Commander","Siegebreaker","Mal'Ganis","Old Murk-Eye",\
              "Zapp Slywick","Foe Reaper 4000","Cave Hydra","Ironhide Direhorn","The Boogeymonster",\
              "Festeroot Hulk","Bolvar, Fireblood","Scavenging Hyena","Junkbot", "Soul Juggler", \
              "Baron Rivendare","Cobalt Guardian","Murloc Tidecaller","Khadgar", "Mama Bear","Pack Leader",\
              "Security Rover","Imp Gang Boss")
#m_b_list=("Dire Wolf Alpha","Murloc Warleader","Phalanx Commander","Siegebreaker","Mal'Ganis","Old Murk-Eye")
#d_s_list=("Mecharoo","")

##"Ironhide Direhorn" no summon

class minion:
    def __init__(self,na="",at=0,he=0,ch="",t=False,sh=False,p=False,w=1,d=0,m=0,dea=False,g=False,spe="",ra="",tie=0):
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
        self.death=dea
        self.special=spe #特殊描述
        self.deathrattle=ra
        self.rattle=False
        self.source="origin"
        self.tier=tie
        self.id = next(self.id_iter)

    id_iter = itertools.count()
    def set_attack(self,at):
        self.attack+=at
        if self.attack<0:
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
        if mo in [0,1,2]:
            self.move = mo
        else:
            print ("error: wrong move state")
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
        if str(sh) in ["True","False"]:
            self.shield = sh
        else:
            print ("error: wrong shield set")
    def get_shield(self):
        return self.shield

    def set_golden(self, go):
        if str(go)in ["True","False"]:
            self.golden = go
        else:
            print ("error: wrong golden set")
    def get_golden(self):
        return self.golden

    def set_taunt(self,t):
        if str(t)in ["True","False"]:
            self.taunt = t
        else:
            print ("error: wrong taunt set")
    def get_taunt(self):
        return self.taunt

    def set_poison(self,p):
        if str(p) in ["True","False"]:
            self.poison = p
        else:
            print ("error: wrong poison set")
    def get_poison(self):
        return self.poison

    def set_wind(self,w):
        if w in [1,2,4]:
            self.wind = w
        else:
            print ("error: wrong wind set")
    def get_wind(self):
        return self.wind

    def set_rattle(self,ra):
        if str(ra) in ["True","False"]:
            self.rattle = ra
        else:
            print ("error: wrong rattle set")
    def get_rattle(self):
        return self.rattle

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

    def set_death(self,dea):
        if str(dea) in ["True","False"]:
            self.death = dea
        else:
            print ("error: wrong death set")
    def get_death(self):
        return self.death

    def set_deathrattle(self,ra):
        if self.deathrattle:
            self.deathrattle+="+"+ra
        else:
            self.deathrattle=ra
    def get_deathrattle(self):
        return self.deathrattle

    def set_special(self,sp):
        if sp in special_list:
            self.special=sp
        else:
            print ("error: wrong special set")
    def get_special(self):
        return self.special

    def set_source(self,so):
        if so in ["origin","overkill","damage","deathrattle"]:
            self.source=so
        else:
            print ("error: wrong source set")
    def get_source(self):
       return self.source

    def get_calculated_health(self):
        return self.health+self.buff[1]-self.damage
    def get_calculated_attack(self):
        return self.attack + self.buff[0]

    def set_tier(self, tie):
        if tie>0 and tie<7:
            self.tier = tie
        else:
            print ("error:wrong tier set")
    def get_tier(self):
        return self.tier

    def __str__(self):
        return "name "+self.name+" attack "+str(self.attack)+"+"+str(self.buff[0])+" health "+str(self.health)+"+"+str(self.buff[1])+" damage "+str(self.damage)+" shield "+str(self.shield)+" "+self.special

    def minion_attack(self,other):
          if self.shield and other.get_calculated_attack()>0:
              self.set_shield(False)
          elif other.poison and other.get_calculated_attack()>0:
              self.set_damage(other.get_calculated_attack())
              self.set_death(True)
          else:
              self.set_damage(other.get_calculated_attack())
             # print (self.damage)

    def copy(self):
        new=minion(self.name,self.attack,self.health,self.character,self.taunt,self.shield,self.poison,self.wind,self.damage,\
                   self.move,self.death,self.golden,self.special,self.deathrattle)
        new.set_source(self.source)
        return new

    def __eq__(self, other):
        if str(self)==str(other):
            return True
        else:
            return False

def origin_minion_buff(lst):  #所有minion_buff
    minionlist=len(lst)
    for i in range(minionlist):
        if lst[i].get_special()=="Dire Wolf Alpha":
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
        elif lst[i].get_special()=="Murloc Warleader":
            for j in range(minionlist):
                if j==i:
                    pass
                else:
                    if lst[j].get_character() in ["Murloc","All"]:
                        if lst[i].get_golden():
                            lst[j].set_attack(-4)
                            lst[j].set_buff([4, 0])
                        else:
                            lst[j].set_attack(-2)
                            lst[j].set_buff([2, 0])
        elif lst[i].get_special()=="Phalanx Commander":
            for j in range(minionlist):
                if lst[j].get_taunt():
                    if lst[i].get_golden():
                        lst[j].set_attack(-4)
                        lst[j].set_buff([4, 0])
                    else:
                        lst[j].set_attack(-2)
                        lst[j].set_buff([2, 0])
        elif lst[i].get_special()=="Siegebreaker":
            for j in range(minionlist):
                if j == i:
                    pass
                else:
                    if lst[j].get_character() in ["Demon","All"]:
                        if lst[i].get_golden():
                            lst[j].set_attack(-2)
                            lst[j].set_buff([2, 0])
                        else:
                            lst[j].set_attack(-1)
                            lst[j].set_buff([1, 0])
        elif lst[i].get_special() == "Mal'Ganis":
            for j in range(minionlist):
                if j == i:
                    pass
                else:
                    if lst[j].get_character() in ["Demon","All"]:
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
        if lst[i].get_special()=="Dire Wolf Alpha" and (not lst[i].get_death()):
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
        elif lst[i].get_special()=="Murloc Warleader" and (not lst[i].get_death()):
            for j in range(minionlist):
                if j==i:
                    pass
                else:
                    if lst[j].get_character() in ["Murloc","All"]:
                        if lst[i].get_golden():
                            lst[j].set_buff([4, 0])
                        else:
                            lst[j].set_buff([2, 0])
        elif lst[i].get_special()=="Phalanx Commander" and (not lst[i].get_death()):
            for j in range(minionlist):
                if lst[j].get_taunt():
                    if lst[i].get_golden():
                        lst[j].set_buff([4, 0])
                    else:
                        lst[j].set_buff([2, 0])
        elif lst[i].get_special()=="Siegebreaker" and (not lst[i].get_death()):
            for j in range(minionlist):
                if j == i:
                    pass
                else:
                    if lst[j].get_character() in ["Demon","All"]:
                        if lst[i].get_golden():
                            lst[j].set_buff([2, 0])
                        else:
                            lst[j].set_buff([1, 0])
        elif lst[i].get_special() == "Mal'Ganis" and (not lst[i].get_death()):
            for j in range(minionlist):
                if j == i:
                    pass
                else:
                    if lst[j].get_character() in ["Demon","All"]:
                        if lst[i].get_golden():
                            lst[j].set_buff([4, 4])
                        else:
                            lst[j].set_buff([2, 2])
        else:
            pass
'''未移除death minion的选择目标
def select_minion(lst): #选择目标
    num=[]
    avail=[]
    for i in range(len(lst)): #不选择死亡随从为目标
        if (not lst[i].get_death()):
            avail.append(i)
    if len(avail)==0: #死光了
        return -1
    for i in avail:
        if lst[i].get_taunt():
            num.append(i)
    if len(num)==0:
        return avail[random.randint(0,len(avail)-1)]
    elif len(num)>0 and len(num)<=len(avail):
        return num[random.randint(0, len(num)-1)]
    else:
        print ("error: wrong select")
        
  if m.get_special() == "Zapp Slywick":
        if m.get_golden():
            m.set_wind(4)
        else:
            m.set_wind(2)
        avail = []
        for i in range(len(m_lst)):#记录所有可攻击对象的序号
            if (not m_lst[i].get_death()):
                avail.append(i)
        if len(avail) != 0:
            temp = []
            for i in avail: #记录所有可攻击对象的攻击
                temp.append(m_lst[i].get_calculated_attack())
            temp1 = []
            min1 = min(temp)
            for i in range(len(temp)):
                if temp[i] == min1:
                    temp1.append(avail[i])  #记录所有最低攻对应的序号
            aim = random.choice(temp1)
            be_attack.append(aim)
            usual_minion_battle(m,m_lst[aim])
        '''
def select_minion(lst): #选择目标
    num=[]
    for i in range(len(lst)):
        if lst[i].get_taunt():
            num.append(i)
    if len(num)==0:#无taunt
        return random.randint(0,len(lst)-1)
    elif len(num)>0 and len(num)<=len(lst):
        return random.choice(num)
    else:
        print ("error: wrong select")
def usual_minion_battle(minion1,minion2): #minion1是攻击方
    minion1.minion_attack(minion2)
    minion2.minion_attack(minion1)
    minion1.set_move(2)
def single_minion_battle(m,m_lst):
    be_attack=""
    aim=-2
    Flag=False
    if m.get_special() == "Zapp Slywick":
        if m.get_golden():
            m.set_wind(4)
        else:
            m.set_wind(2)
        temp=[]
        temp1 = []
        for i in m_lst: #记录所有可攻击对象的攻击和序号
            temp.append(i.get_calculated_attack())
        min1 = min(temp)
        for i in range(len(temp)):
            if temp[i] == min1:
                temp1.append(i)  #记录所有最低攻对应的序号
        aim = random.choice(temp1)
        be_attack=m_lst[aim].id
        flag=m_lst[aim].get_shield()
        usual_minion_battle(m,m_lst[aim])
        if flag:
            lose_shield(m_lst,1)
        else:
           after_injury(m_lst,aim)
    elif (m.get_special() in ["Foe Reaper 4000","Cave Hydra"]):
        aim =select_minion(m_lst)
        be_attack=m_lst[aim].id
        minionlist = len(m_lst)
   #     if aim !=-1:
        if minionlist == 1:
            flag = m_lst[aim].get_shield()
            m.minion_attack(m_lst[aim])
            m_lst[aim].minion_attack(m)
            if flag:
                lose_shield(m_lst, 1)
            else:
               after_injury(m_lst,aim)
        elif aim == 0:
            Flag1=m_lst[aim].get_shield()
            Flag2=m_lst[aim+1].get_shield()
            num = (1 if Flag1 else 0)+(1 if Flag2 else 0)
            m.minion_attack(m_lst[aim])
            m_lst[aim].minion_attack(m)
            m_lst[aim + 1].minion_attack(m)
            lose_shield(m_lst, num)
            len1=len(m_lst)
            if not Flag1:
                after_injury(m_lst,aim)
            if not Flag2 :#招完之后还没满，attack无dead
                after_injury(m_lst, aim+1+len(m_lst)-len1)
        elif aim == minionlist - 1:
            Flag1 = m_lst[aim-1].get_shield()
            Flag2 = m_lst[aim].get_shield()
            num = (1 if Flag1 else 0) + (1 if Flag2 else 0)
            m.minion_attack(m_lst[aim])
            m_lst[aim].minion_attack(m)
            m_lst[aim - 1].minion_attack(m)
            lose_shield(m_lst, num)
            len1 = len(m_lst)
            if not Flag1:
                after_injury(m_lst, aim-1)
            if (not Flag2):  # 招完之后还没满，attack无dead
                after_injury(m_lst, aim+len(m_lst)-len1)
        else:
            Flag1 = m_lst[aim - 1].get_shield()
            Flag2 = m_lst[aim].get_shield()
            Flag3=m_lst[aim+1].get_shield()
            num = (1 if Flag1 else 0) + (1 if Flag2 else 0)+(1 if Flag3 else 0)
            m.minion_attack(m_lst[aim])
            m_lst[aim].minion_attack(m)
            m_lst[aim + 1].minion_attack(m)
            m_lst[aim - 1].minion_attack(m)
            lose_shield(m_lst, num)
            len1 = len(m_lst)
            if not Flag1:
                after_injury(m_lst, aim - 1)
            if (not Flag2) :  # 招完之后还没满，attack无dead
                after_injury(m_lst, aim + len(m_lst)-len1)
            if (not Flag3) :  # 招完之后还没满，attack无dead
                after_injury(m_lst, aim + 1+len(m_lst)-len1)
        m.set_move(2)
    elif m.get_special() == "The Boogeymonster":
        aim = select_minion(m_lst)
        be_attack=m_lst[aim].id
       # if aim!=-1:
        flag=m_lst[aim].get_shield()
        usual_minion_battle(m,m_lst[aim])
        if flag:
            lose_shield(m_lst,1)
        else:
            after_injury(m_lst,aim)
        if m_lst[aim].get_damage() >= (m_lst[aim].get_health() + m_lst[aim].get_buff_health()) and m.get_damage() < (m.get_health() + m.get_buff_health()):
            if m.get_golden():
                m.set_health(4)
                m.set_attack(4)
            else:
                m.set_health(2)
                m.set_attack(2)
    elif m.get_special() == "Ironhide Direhorn":
        aim = select_minion(m_lst)
        be_attack=m_lst[aim].id
      #  if aim!=-1:
        flag=m_lst[aim].get_shield()
        usual_minion_battle(m,m_lst[aim])
        if m_lst[aim].get_damage() > (m_lst[aim].get_health() + m_lst[aim].get_buff_health()):
            Flag=True
        if flag:
            lose_shield(m_lst,1)
        else:
           after_injury(m_lst,aim)
    else:
        aim = select_minion(m_lst)
        be_attack=m_lst[aim].id
       # if aim!=-1:
        flag=m_lst[aim].get_shield()
        usual_minion_battle(m,m_lst[aim])
        if flag:
            lose_shield(m_lst,1)
        else:
            after_injury(m_lst, aim)
    return [Flag,be_attack]

def after_attack(lst):
    for i in lst:
        if i.get_special() == "Festeroot Hulk":
            if i.get_golden():
                i.set_attack(2)
            else:
                i.set_attack(1)
def after_death(ch,lst,lst2):#lst己方，lst2对方
    if ch in ["Beast","All"]:
        for i in lst:
            if i.get_special() == "Scavenging Hyena" and (not i.get_death()):
                if i.get_golden():
                    i.set_health(2)
                    i.set_attack(4)
                else:
                    i.set_health(1)
                    i.set_attack(2)
    if ch in ["Mech","All"] :
        for i in lst:
            if i.get_special() == "Junkbot" and (not i.get_death()):
                if i.get_golden():
                    i.set_health(4)
                    i.set_attack(4)
                else:
                    i.set_health(2)
                    i.set_attack(2)
    if ch in ["Demon","All"]:
        for i in lst:
            if i.get_special() == "Soul Juggler" and (not i.get_death()):
                times = 2 if i.get_golden() else 1
                for j in range(times):
                    target=select_undead(lst2)
                    if target!=-1:
                        if lst2[target].get_shield():
                            lst2[target].set_shield(False)
                            lose_shield(lst2,1)
                        else:
                            lst2[target].set_damage(3)
                            after_injury(lst2,target)

def lose_shield(lst,num):
    for i in lst:
        if i.get_special()=="Bolvar, Fireblood":
            if i.get_golden():
                i.set_attack(4*num)
            else:
                i.set_attack(2*num)
def after_injury(lst,pos):
    if lst[pos].get_special()=="Security Rover":
        summon("Guard Bot", lst[pos].get_move(), pos + 1, lst, "damage", lst[pos].get_golden())
    elif lst[pos].get_special()=="Imp Gang Boss":
        summon("Imp", lst[pos].get_move(), pos + 1, lst, "damage", lst[pos].get_golden())
    else:
        pass

def summon_buff(minion1,lst):
    if minion1.get_character()=="Beast":
        for j in lst:
            if j.get_special()=="Mama Bear" and(not j.get_death()):
                if j.get_golden():
                    minion1.set_health(8)
                    minion1.set_attack(8)
                else:
                    minion1.set_health(4)
                    minion1.set_attack(4)
            elif j.get_special()=="Pack Leader" and(not j.get_death()):
                if j.get_golden():
                    minion1.set_attack(6)
                else:
                    minion1.set_attack(3)
def duplicate(lst):
    times=0
    num=0
    for i in lst:
        if i.get_special()=="Khadgar" and (not i.get_death()):
            if i.get_golden():
                times+=1
                num+=2**times
            else:
                times+=1
                num+=2**(times-1)
    return num

def set_minion(temp,attack_state,golden):#从database的dictionary形式变成minion类
    num=2 if golden else 1
    a=minion(na=temp["name"],at=temp["atk"]*num,he=temp["health"]*num,ch=temp["tribe"],t=temp["taunt"],sh=temp["divineShield"],p=temp["poisonous"],w=2 if temp["windfury"] else 1,g=golden,tie=temp["tier"])
    if temp["name"] in special_list:
        a.set_special(temp["name"])
    if attack_state==1:
        a.set_move(1)
    if temp["deathrattle"]:
        a.set_deathrattle((temp["name"]))
    return a

def deathrattle_time(lst):
    time=1
    for i in lst:
        if i.get_special()=="Baron Rivendare":
            if i.get_golden():
                time=3
                break
            else:
                time=2
    return time

def select_undead(lst):
    avail = []
    for i in range(len(lst)):  # 不选择死亡随从为目标
        if (not lst[i].get_death()) and lst[i].get_calculated_health() > 0:
            avail.append(i)
    if avail:  # 没死光
        target = random.choice(avail)
        return target
    else:
        return -1

def single_deathrattle(name,dead,lst1,lst2,pos):
    if name == "Kaboom Bot":
        times=2 if dead.get_golden() else 1
        for j in range(times):
            target=select_undead(lst2)
            if target!=-1:
                if lst2[target].get_shield():
                    lst2[target].set_shield(False)
                    lose_shield(lst2,1)
                else:
                    lst2[target].set_damage(4)
                    after_injury(lst2,target)
    elif name=="Fiendish Servant":
        times = 2 if dead.get_golden() else 1
        for j in range(times):
            target = select_undead(lst1)
            if target != -1:
                lst1[target].set_attack(dead.get_calculated_attack())
    elif name=="Selfless Hero":
        times = 2 if dead.get_golden() else 1
        for j in range(times):
            avail = []
            for i in range(len(lst1)):  # 不选择死亡和有盾的随从为目标
                if (not lst1[i].get_death()) and lst1[i].get_calculated_health() > 0 and (not lst1[i].get_shield()):
                    avail.append(i)
            if avail:
                target = random.choice(avail)
                lst1[target].set_shield(True)
    elif name=="Spawn of N'Zoth":
        buff = 2 if dead.get_golden() else 1
        for i in lst1:
            if (not i.get_death()):
                i.set_attack(buff)
                i.set_health(buff)
    elif name=="Tortollan Shellraiser":
        buff = 2 if dead.get_golden() else 1
        target = select_undead(lst1)
        if target != -1:
            lst1[target].set_attack(buff)
            lst1[target].set_health(buff)
    elif name=="King Bagurgle":
        buff = 4 if dead.get_golden() else 2
        for i in lst1:
            if (not i.get_death()) and (i.get_character() in ["Murloc","All"]):
                i.set_attack(buff)
                i.set_health(buff)
    elif name=="Goldrinn, the Great Wolf":
        buff = 8 if dead.get_golden() else 4
        for i in lst1:
            if (not i.get_death()) and (i.get_character() in ["Beast","All"]):
                i.set_attack(buff)
                i.set_health(buff)
    elif name=="Mecharoo":
        summon("Jo-E Bot",dead.get_move(),pos,lst1,"deathrattle",dead.get_golden())
    elif name == "Kindly Grandmother":
        summon("Big Bad Wolf", dead.get_move(), pos, lst1, "deathrattle", dead.get_golden())
    elif name=="Mounted Raptor":
        times=2 if dead.get_golden() else 1
        i=0
        while i<times and alive_num(lst1)<7:
            temp=len(lst1)
            name=random.choice(database.get_minions_by_cost(1))["name"]
            summon(name,dead.get_move(),pos,lst1,"deathrattle",False)
            pos+=len(lst1)-temp
            i+=1
    elif name == "Rat Pack":
        times=dead.get_calculated_attack()
        i = 0
        while i < times and alive_num(lst1)<7:
            temp=len(lst1)
            summon("Rat", dead.get_move(), pos, lst1, "deathrattle", dead.get_golden())
            pos += len(lst1) - temp
            i+=1
    elif name=="Harvest Golem":
        summon("Damaged Golem",dead.get_move(),pos,lst1,"deathrattle",dead.get_golden())
    elif name == "Imprisoner":
        summon("Imp", dead.get_move(), pos, lst1, "deathrattle", dead.get_golden())
    elif  name == "The Beast":
        summon("Finkle Einhorn",0, len(lst2), lst2, "deathrattle", False)
    elif name == "Infested Wolf":
        temp = len(lst1)
        summon("Spider", dead.get_move(), pos, lst1, "deathrattle", dead.get_golden())
        pos += len(lst1) - temp
        summon("Spider", dead.get_move(), pos, lst1, "deathrattle", dead.get_golden())
    elif name=="Piloted Shredder":
        times = 2 if dead.get_golden() else 1
        i = 0
        while i < times and alive_num(lst1)<7:
            temp = len(lst1)
            name = random.choice(database.get_minions_by_cost(2))["name"]
            summon(name, dead.get_move(), pos, lst1, "deathrattle", False)
            pos += len(lst1) - temp
            i += 1
    elif name=="Piloted Sky Golem":
        times = 2 if dead.get_golden() else 1
        i = 0
        while i < times and alive_num(lst1)<7:
            temp = len(lst1)
            name = random.choice(database.get_minions_by_cost(4))["name"]
            summon(name, dead.get_move(), pos, lst1, "deathrattle", False)
            pos += len(lst1) - temp
            i += 1
    elif name == "Replicating Menace":
        times = 3
        i = 0
        while i < times and alive_num(lst1)<7:
            temp = len(lst1)
            summon("Microbot", dead.get_move(), pos, lst1, "deathrattle", False)
            pos += len(lst1) - temp
            i += 1
    elif name == "Replicating Menace golden":
        times = 3
        i = 0
        while i < times and alive_num(lst1)<7:
            temp = len(lst1)
            summon("Microbot", dead.get_move(), pos, lst1, "deathrattle", True)
            pos += len(lst1) - temp
            i += 1
    elif name == "Mechano-Egg":
        summon("Robosaur", dead.get_move(), pos, lst1, "deathrattle", dead.get_golden())
    elif name == "Savannah Highmane":
        times = 2
        i = 0
        while i < times and alive_num(lst1)<7:
            temp = len(lst1)
            summon("Hyena", dead.get_move(), pos, lst1, "deathrattle", dead.get_golden())
            pos += len(lst1) - temp
            i += 1
    elif name == "Sated Threshadon":
        times = 3
        i = 0
        while i < times and alive_num(lst1)<7:
            temp = len(lst1)
            summon("Primalfin", dead.get_move(), pos, lst1, "deathrattle", dead.get_golden())
            pos += len(lst1) - temp
            i += 1
    elif name == "Voidlord":
        times = 3
        i = 0
        while i < times and alive_num(lst1)<7:
            temp = len(lst1)
            summon("Voidwalker", dead.get_move(), pos, lst1, "deathrattle", dead.get_golden())
            pos += len(lst1) - temp
            i += 1
    elif name == "Sneed's Old Shredder":
        times = 2 if dead.get_golden() else 1
        i = 0
        while i < times and alive_num(lst1)<7:
            temp = len(lst1)
            name = random.choice(database.get_legendary_minions())["name"]
            summon(name, dead.get_move(), pos, lst1, "deathrattle", False)
            pos += len(lst1) - temp
            i += 1
    elif name=="Ghastcoiler":
        times = 4 if dead.get_golden() else 2
        i = 0
        while i < times and alive_num(lst1)<7:
            temp = len(lst1)
            name = random.choice(database.get_deathrattle_minions())["name"]
            summon(name, dead.get_move(), pos, lst1, "deathrattle", False)
            pos += len(lst1) - temp
            i += 1
    elif name=="Gentle Megasaur":#亡语植物
        times = 2
        i = 0
        while i < times and alive_num(lst1) < 7:
            temp = len(lst1)
            summon("Plant", dead.get_move(), pos, lst1, "deathrattle", False)
            pos += len(lst1) - temp
            i += 1
    else:
        pass
def alive_num(lst):
    num=0
    for i in lst:
        if (not i.get_death()):
            num+=1
    return num

def check_zero(lst):
    Flag=True
    for i in lst:
        if i.get_calculated_attack():
            Flag=False
            break
    return Flag

def summon(name,attack_state,pos,lst,source,gold):#记得马上renew_buff
    if alive_num(lst)<7:
        dic=database.get_minions_by_name(name)
        if dic:
            minion1=set_minion(dic[0],attack_state,gold)
            minion1.set_source(source)
            charater=minion1.get_character()
            summon_buff(minion1,lst)
            lst.insert(pos,minion1.copy())
            after_summon(lst,charater)
            copies=minion1.copy()
            summon_buff(copies,lst)
            times=duplicate(lst)
            n=0
            while (n<times and alive_num(lst)<7):
                n+=1
                lst.insert(pos+n,copies.copy())
                after_summon(lst, charater)

def after_summon(lst,ch):
    if ch=="Mech":
        for i in lst:
            if i.get_special()=="Cobalt Guardian":
                i.set_shield(True)
    elif ch=="Murloc":
        for i in lst:
            if i.get_special() == "Murloc Tidecaller":
                if i.get_golden():
                    i.set_attack(2)
                else:
                    i.set_attack(1)


class battlefeild:
    def __init__(self, up=[], down=[]):
        self.up = up #记录上方
        self.down = down #记录下方
        self.begin=None #True 表示上面先动,主玩家设置
        self.now =None  #表示运行到第几个,第一表示该第几个，第二表示示该上方或下方,True 表示上方
        self.history = []
        self.atkHistory = []
        self.log = ""
        self.attack_time=1
        self.already_attack=0
        self.dead_minion=False
        self.attack_flag=False
        self.result=""
        self.mech_up=[]
        self.mech_down=[]

    def calc_tier(self):
        if self.result=="up win":
            num=0
            for i in self.up:
                num+=i.get_tier()
            return num
        elif self.result=="down win":
            num = 0
            for i in self.down:
                num += i.get_tier()
            return num
        else:
            return 0

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
                    "id": minion.id,
                    "attack": minion.get_calculated_attack(),
                    "health": minion.get_calculated_health(),
                    "shield": minion.get_shield(),
                    "taunt": minion.get_taunt(),
                    "poisonous": minion.get_poison(),
                    "golden": minion.get_golden(),
                    "death": minion.get_rattle(),
                    "name": minion.get_name(),
                    "source": minion.get_source()
                })
        self.history.append(current)
    def set_log(self,lo):
        self.log +=lo

    def set_dead_minion(self,de):
       if str(de) !="True" and str(de) !="False":
            print ("error: wrong set dead minion")
       else:
        self.dead_minion=de
    def get_dead_minion(self):
        return self.dead_minion

    def set_now(self,num,side):
        if num>6 or num<-1:
            print ("error: wrong position")
        elif str(side) !="True" and str(side) !="False":
            print ("error: wrong side")
        else:
            self.now=[num,side]

    def set_attack_time(self):
        if self.now[1]:
            self.attack_time=self.up[self.now[0]].get_wind()
        else:
            self.attack_time=self.down[self.now[0]].get_wind()
    def get_attack_time(self):
        return self.attack_time

    def reset_already_attack(self):
        self.already_attack=0
    def add_already_attack(self):
        self.already_attack+=1
    def get_already_attack(self):
        return self.already_attack
    def attack_over(self):
        self.already_attack=self.attack_time

    def get_result(self):
        return self.result

    def add_minion(self,mi,side,pos):
        if side=="up":
            if pos>=0 and len(self.up) < 7:
                self.up.insert(pos,mi)  #这里注意如果列表只有4个minion，直接插入第六个会使其变成第五而不是第六
            else:
                print ("error: wrong position to add a minion1")
        elif side=="down":
            if pos>=0 and len(self.down) < 7:
                self.down.insert(pos,mi)  #这里注意如果列表只有4个minion，直接插入第六个会使其变成第五而不是第六
            else:
                print ("error: wrong position to add a minion2")
        else:
            print ("error:wrong side to add a minion")

    def up_minion(self):
        return len(self.up)
    def down_minion(self):
        return  len(self.down)
    def get_up(self):
        return self.up
    def get_down(self):
        return self.down

    def battle_begin(self):  #确定开始方和处理minion_buff
        minionup=len(self.up)
        miniondown=len(self.down)
        if minionup> miniondown:
            self.set_now(0,True)
        elif minionup< miniondown:
            self.set_now(0, False)
        else:
            a=random.random()
            if a>=0.5:
                self.set_now(0, True)
            else:
                self.set_now(0,False)
        main_player = random.random()
        if main_player >= 0.5:
             self.begin = True
        else:
             self.begin =False
        origin_minion_buff(self.up)
        origin_minion_buff(self.down)#Old Murk-Eye比较特殊，考虑对面,专门处理
        Murloc_num=0
        for i in self.up:
            if i.get_character()in ["Murloc","All"]:
                Murloc_num+=1
        for i in self.down:
            if i.get_character()in ["Murloc","All"]:
                Murloc_num+=1
        for i in self.up:
            if i.get_special() == "Old Murk-Eye" :
                if i.get_golden():
                    i.set_attack(-2*(Murloc_num-1))
                    i.set_buff([2*(Murloc_num-1), 0])
                else:
                    i.set_attack(-(Murloc_num-1))
                    i.set_buff([Murloc_num-1, 0])
        for i in self.down:
            if i.get_special() == "Old Murk-Eye":
                if i.get_golden():
                    i.set_attack(-2*(Murloc_num-1))
                    i.set_buff([2*(Murloc_num-1), 0])
                else:
                    i.set_attack(-(Murloc_num-1))
                    i.set_buff([Murloc_num-1, 0])

    def minion_battle(self):
        side = self.now[1]
        pos=self.now[0]
        attack_state=[]
        if self.up and self.down:
            if  str(side) !="True" and str(side) !="False":
                print ("error: which side to attack")
            elif side:
                if (not self.dead_minion):
                    Flag=self.up[pos].get_shield()
                    damage1=self.up[pos].get_damage()
                    temp = single_minion_battle(self.up[pos], self.down)
                    damage2=self.up[pos].get_damage()
                    if Flag and (not self.up[pos].get_shield()):
                        lose_shield(self.up,1)
                    attack_state.append(self.up[pos].id)
                    attack_state.append(temp[1])
                    self.set_attack_time()
                    self.add_already_attack()
                    self.attack_flag=True
                    if temp[0]:
                        summon("Ironhide Runt", 0, pos + 1, self.up, "overkill", self.up[pos].get_golden())
                    if damage2-damage1>0:
                        after_injury(self.up,pos)
                    self.detect_death()
                    after_attack(self.up)
                if pos !=-1:
                    if self.up[pos].get_death():
                        self.attack_over()
            else:
                if (not self.dead_minion) and self.down:
                    Flag = self.down[pos].get_shield()
                    damage1 = self.down[pos].get_damage()
                    temp=single_minion_battle(self.down[pos], self.up)
                    damage2 = self.down[pos].get_damage()
                    if Flag and (not self.down[pos].get_shield()):
                        lose_shield(self.down,1)
                    attack_state.append(self.down[pos].id)
                    attack_state.append(temp[1])
                    self.set_attack_time()
                    self.add_already_attack()
                    self.attack_flag = True
                    if temp[0]:
                        summon("Ironhide Runt", 0, pos + 1, self.down, "overkill", self.down[pos].get_golden())
                    if damage2-damage1>0:
                        after_injury(self.down,pos)
                    self.detect_death()
                    after_attack(self.down)
                if pos!=-1:
                    if self.down[pos].get_death():
                        self.attack_over()
        self.atkHistory.append(attack_state)

    def do_deathrattle(self):
        if not self.attack_flag:
            pos_up,pos_down=0,0
            dead_up=[]
            dead_down=[]
            for i in range(len(self.up)):
                if self.up[i].get_death():
                    self.up[i].set_rattle(True)
                    dead_up.append(i)
                    if self.up[i].get_character() == "Mech" and len(self.mech_up) < 2:
                        self.mech_up.append(self.up[i].get_name())
            for i in range(len(self.down)):
                if self.down[i].get_death():
                    self.down[i].set_rattle(True)
                    dead_down.append(i)
                    if self.down[i].get_character() == "Mech" and len(self.mech_down) < 2:
                        self.mech_down.append(self.down[i].get_name())
            if self.begin:
                times = deathrattle_time(self.up)
                for i in dead_up:
                    deathrattle_lst = self.up[i+pos_up].get_deathrattle().split("+")
                    if deathrattle_lst[0]:
                        for j in deathrattle_lst:
                            for k in range(times):
                                if j == "Kangor's Apprentice" and alive_num(self.up)<7:
                                    for l in self.mech_up:
                                        temp = len(self.up)
                                        summon(l,self.up[i+pos_up].get_move(),i+pos_up+1,self.up,"deathrattle",self.up[i+pos_up].get_golden())
                                        pos_up += len(self.up) - temp
                                else:
                                    temp=len(self.up)
                                    single_deathrattle(j,self.up[i+pos_up],self.up,self.down,i+pos_up+1)
                                    pos_up+=len(self.up)-temp
                                    self.renew_buff()
                    after_death(self.up[i+pos_up].get_character(),self.up,self.down)
                times=deathrattle_time(self.down)
                for i in dead_down:
                    deathrattle_lst = self.down[i+pos_down].get_deathrattle().split("+")
                    if deathrattle_lst[0]:
                        for j in deathrattle_lst:
                            for k in range(times):
                                if j == "Kangor's Apprentice" and alive_num(self.down)<7:
                                    for l in self.mech_down:
                                        temp = len(self.down)
                                        summon(l,self.down[i+pos_down].get_move(),i+pos_down+1,self.down,"deathrattle",self.down[i+pos_down].get_golden())
                                        pos_down += len(self.down) - temp
                                else:
                                    temp = len(self.down)
                                    single_deathrattle(j, self.down[i+pos_down], self.down, self.up,i+pos_down+1)
                                    pos_down += len(self.down) - temp
                                    self.renew_buff()
                    after_death(self.down[i+pos_down].get_character(), self.down, self.up)
            else:
                times = deathrattle_time(self.down)
                for i in dead_down:
                    deathrattle_lst = self.down[i + pos_down].get_deathrattle().split("+")
                    if deathrattle_lst[0]:
                        for j in deathrattle_lst:
                            for k in range(times):
                                if j == "Kangor's Apprentice" and alive_num(self.down) < 7:
                                    for l in self.mech_down:
                                        temp = len(self.down)
                                        summon(l, self.down[i + pos_down].get_move(), i + pos_down+1, self.down,
                                               "deathrattle", self.down[i + pos_down].get_golden())
                                        pos_down += len(self.down) - temp
                                else:
                                    temp = len(self.down)
                                    single_deathrattle(j, self.down[i + pos_down], self.down, self.up, i + pos_down+1)
                                    pos_down += len(self.down) - temp
                                    self.renew_buff()
                    after_death(self.down[i + pos_down].get_character(), self.down, self.up)
                times = deathrattle_time(self.up)
                for i in dead_up:
                    deathrattle_lst = self.up[i + pos_up].get_deathrattle().split("+")
                    if deathrattle_lst[0]:
                        for j in deathrattle_lst:
                            for k in range(times):
                                if j == "Kangor's Apprentice" and alive_num(self.up) < 7:
                                    for l in self.mech_up:
                                        temp = len(self.up)
                                        summon(l, self.up[i + pos_up].get_move(), i + pos_up+1, self.up, "deathrattle",
                                               self.up[i + pos_up].get_golden())
                                        pos_up += len(self.up) - temp
                                else:
                                    temp = len(self.up)
                                    single_deathrattle(j, self.up[i + pos_up], self.up, self.down, i + pos_up+1)
                                    pos_up += len(self.up) - temp
                                    self.renew_buff()
                    after_death(self.up[i + pos_up].get_character(), self.up, self.down)

    def detect_death(self):
        Flag=True
        for i in self.up:
            if i.get_damage()>= (i.get_health()+i.get_buff_health()):
                i.set_death(True)
                self.set_dead_minion(True)
                Flag=False

        for j in self.down:
            if j.get_damage()>= (j.get_health()+j.get_buff_health()):
                j.set_death(True)
                self.set_dead_minion(True)
                Flag=False
        if Flag:
            self.set_dead_minion(False)

    def remove_death(self):
        self.up=list(filter(lambda x: not x.get_rattle(), self.up))
        self.down=list(filter(lambda x: not x.get_rattle(), self.down))

    def renew_begin_attack(self,lst,side):
        self.reset_already_attack()
        if lst:
            pos=-1
            for i in lst:
                if i.get_move() == 2:
                    i.set_move(1)
            for i in range(len(lst)):
                if lst[i].get_move() == 0:
                    pos = i
                    break
            if pos == -1:
                pos = 0
                for i in lst:
                    i.set_move(0)
            self.set_now(pos, side)

    def renew_attack(self):
        side = self.now[1]
        pos=self.now[0]
        if pos==-1:
            if self.attack_time > self.already_attack:  #未到行动数
                if not self.get_dead_minion():
                    if side:
                        self.renew_begin_attack(self.up,side)
                    else:
                        self.renew_begin_attack(self.down, side)
            else:
                print("error: wrong renew set")
        else:
            if self.attack_time > self.already_attack:  # 未到行动数
                if side:
                    num = -1
                    for i in range(len(self.up)):
                        if self.up[i].get_move() == 2:
                            num = i
                            break
                    if num == -1:
                        print("error: no one attack")
                    else:
                        self.set_now(num, side)
                else:
                    num = -1
                    for i in range(len(self.down)):
                        if self.down[i].get_move() == 2:
                            num = i
                            break
                    if num == -1:
                        print("error: no one attack")
                    else:
                        self.set_now(num, side)
            else:
                if self.get_dead_minion():
                    self.reset_already_attack()
                    self.set_now(-1,(not side))
                else:
                    if side:
                        self.renew_begin_attack(self.down,False)
                    else:
                        self.renew_begin_attack(self.up,True)
        self.attack_flag=False
        self.check_state()

    def renew_buff(self):
        temp_up=[]
        temp_down=[]
        Murloc_num = 0
        for i in self.up:
            temp_up.append(i.get_buff_health())
            i.remove_buff()
            if (i.get_character()in ["Murloc","All"]) and (not i.get_death()):
                Murloc_num += 1
        for i in self.down:
            temp_down.append(i.get_buff_health())
            i.remove_buff()
            if (i.get_character() in ["Murloc","All"])  and (not i.get_death()):
                Murloc_num += 1
        add_minion_buff(self.up)
        add_minion_buff(self.down)
        for i in range(len(self.up)):
            if self.up[i].get_special() == "Old Murk-Eye":
                if self.up[i].get_death():
                    if self.up[i].get_golden():
                        self.up[i].set_buff([2 * Murloc_num, 0])
                    else:
                        self.up[i].set_buff([Murloc_num, 0])
                else:
                    if self.up[i].get_golden():
                        self.up[i].set_buff([2 * (Murloc_num-1) , 0])
                    else:
                        self.up[i].set_buff([Murloc_num - 1, 0])
            if temp_up[i]- self.up[i].get_buff_health()>self.up[i].get_damage():
                self.up[i].remove_damage()
            elif temp_up[i]- self.up[i].get_buff_health()>0:
                self.up[i].set_damage(self.up[i].get_buff_health()-temp_up[i])
            else:
                pass
        for i in range(len(self.down)):
            if self.down[i].get_special() == "Old Murk-Eye":
                if self.down[i].get_death():
                    if self.down[i].get_golden():
                        self.down[i].set_buff([2 * Murloc_num, 0])
                    else:
                        self.down[i].set_buff([Murloc_num , 0])
                else:
                    if self.down[i].get_golden():
                        self.down[i].set_buff([2 * (Murloc_num - 1), 0])
                    else:
                        self.down[i].set_buff([Murloc_num - 1, 0])
            if temp_down[i]- self.down[i].get_buff_health()>self.down[i].get_damage():
                self.down[i].remove_damage()
            elif temp_down[i]- self.down[i].get_buff_health()>0:
                self.down[i].set_damage(self.down[i].get_buff_health()-temp_down[i])
            else:
                pass

    def deal_zero_attack(self):#选择的行动者是zero attack
        side=self.now[1]
        pos=self.now[0]
        if check_zero(self.up) and check_zero(self.down):
            self.result = "a tie"
            self.log += self.result
        else:
            if side:
                if check_zero(self.up):
                    for i in self.up:
                        i.set_move(1)
                    self.attack_over()
                    self.renew_attack()
                else:
                    self.up[pos].set_move(1)
                    self.set_now(-1,side)
                    self.renew_attack()
            else:
                if check_zero(self.down):
                    for i in self.down:
                        i.set_move(1)
                    self.attack_over()
                    self.renew_attack()
                else:
                    self.down[pos].set_move(1)
                    self.set_now(-1,side)
                    self.renew_attack()

    def check_state(self):
        if not self.get_dead_minion():
            if self.up and self.down:
                if self.now[0]<0 or self.now[0]>6:
                    print ("error: wrong state",self.now)
                else:
                    if self.now[1]:
                        if not self.up[self.now[0]].get_calculated_attack():
                            self.deal_zero_attack()
                    else:
                        if not self.down[self.now[0]].get_calculated_attack():
                            self.deal_zero_attack()
            elif (not self.up) and (not self.down):
                self.result = "a tie"
                self.log += self.result
            elif self.down :
                self.result="down win"
                self.log+=self.result
            else:
                self.result="up win"
                self.log += self.result

    def __str__(self):
        str1="up:\n"
        for i in self.up:
            str1+=str(i)+"\n"
        str1+="down:\n"
        for i in self.down:
            str1+=str(i)+"\n"
        str1+="now:"+str(self.now)
        return str1

    def quick_add_up(self,name,attack=0,health=0,taunt=False,shield=False,poison=False,wind=1,golden=False,deathrattle="",times=0):
        dic = database.get_minions_by_name(name)
        if dic:
            temp=dic[0]
            num=2 if golden else 1
            a = minion(na=name, at=max(temp["atk"]*num ,attack) , he=max(temp["health"] * num,health), ch=temp["tribe"],\
                       t=temp["taunt"] if temp["taunt"] else taunt, sh=temp["divineShield"] if temp["divineShield"] else shield,\
                       p=temp["poisonous"] if temp["poisonous"] else poison,g=golden, tie=temp["tier"])
            if name in special_list:
                a.set_special(name)
            if name=="Zapp Slywick" and golden:
                a.set_wind(4)
            else:
                a.set_wind(2 if temp["windfury"] else wind)
            if temp["deathrattle"]:
                a.set_deathrattle((temp["name"]))
            if deathrattle:
                for i in range(times):
                    a.set_deathrattle(deathrattle)
            if len(self.up)<7:
                self.up.insert(len(self.up),a)

    def quick_add_down(self, name, attack=0, health=0, taunt=False, shield=False, poison=False, wind=1,
                     golden=False, deathrattle="", times=0):
        dic = database.get_minions_by_name(name)
        if dic:
            temp = dic[0]
            num = 2 if golden else 1
            a = minion(na=name, at=max(temp["atk"] * num, attack), he=max(temp["health"] * num, health),
                       ch=temp["tribe"], \
                       t=temp["taunt"] if temp["taunt"] else taunt,
                       sh=temp["divineShield"] if temp["divineShield"] else shield, \
                       p=temp["poisonous"] if temp["poisonous"] else poison, g=golden, tie=temp["tier"])
            if name in special_list:
                a.set_special(name)
            if name == "Zapp Slywick" and golden:
                a.set_wind(4)
            else:
                a.set_wind(2 if temp["windfury"] else wind)
            if temp["deathrattle"]:
                a.set_deathrattle((temp["name"]))
            if deathrattle:
                for i in range(times):
                    a.set_deathrattle(deathrattle)
            if len(self.down)<7:
                self.down.insert(len(self.down),a)

def battle(field):
    field.battle_begin()
    field.dump()
    field.check_state()
   # print (field,"\n")
    while not field.get_result():
        field.minion_battle()
        field.renew_buff()
        field.do_deathrattle()
       # field.renew_buff()
        field.dump()
       # print (field,"\n")
        field.remove_death()
        field.detect_death()
        field.renew_buff()
        #field.dump()
        field.renew_attack()
       # print ("a")
       # print (field,"c\n")
        #print (field.get_already_attack()," ",field.get_attack_time())
    print (field.log)

def simulate(field1,time):
    i=0
    up,down,tie=0,0,0
    up1,down1=0,0
    while i<time:
        field=copy.deepcopy(field1)
        field.battle_begin()
        field.check_state()
        while not field.get_result():
            field.minion_battle()
            field.renew_buff()
            field.do_deathrattle()
            field.remove_death()
            field.detect_death()
            field.renew_buff()
            field.renew_attack()
        if field.get_result()=="up win":
            up+=1
            up1+=field.calc_tier()
        elif field.get_result()=="down win":
            down+=1
            down1+=field.calc_tier()
        elif field.get_result()=="a tie":
            tie+=1
        else:
            print ("error: no result")
        i+=1
    print ("test time: ",time)
    print ("up win: ",up," average damage: ",up1/up if up!=0 else 0)
    print ("down win: ",down," average damage: ",down1/down if down!=0 else 0)
    print ("a tie: ",tie)


#'''
ba = battlefeild()
ba.quick_add_up("Kaboom Bot",15, 4,golden=True)
ba.quick_add_up("Cobalt Guardian", 25, 10,shield=True,deathrattle="Replicating Menace",times=1)
ba.quick_add_up("Security Rover", 7, 10,shield=True,taunt=True)
ba.quick_add_up("Shielded Minibot", 9, 2)
ba.quick_add_up("Screwjank Clunker", 3, 5)
ba.quick_add_up("Metaltooth Leaper", 13, 6)
ba.quick_add_up("Baron Rivendare")
ba.quick_add_down("Cobalt Guardian", 8, 3,shield=True)
ba.quick_add_down("Harvest Golem", 6, 6,golden=True)
ba.quick_add_down("Mechano-Egg")
ba.quick_add_down("Shielded Minibot", 4, 2)
ba.quick_add_down("Annoy-o-Tron",golden=True)
ba.quick_add_down("Bolvar, Fireblood")
ba.quick_add_down("Junkbot")
print (ba)
import time
start_time = time.time()
simulate(ba,1000)
end_time = time.time()
print (end_time-start_time)
#'''

