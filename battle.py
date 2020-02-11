import random
import database
ch_list=("Beast","Murloc","Mech","Demon","All")
special_list=("Dire Wolf Alpha","Murloc Warleader","Phalanx Commander","Siegebreaker","Mal'Ganis","Old Murk-Eye",\
              "Zapp Slywick","Foe Reaper 4000","Cave Hydra","Ironhide Direhorn","The Boogeymonster",\
              "Festeroot Hulk","Scavenging Hyena","Junkbot", "Soul Juggler","Kaboom Bot")
#m_b_list=("Dire Wolf Alpha","Murloc Warleader","Phalanx Commander","Siegebreaker","Mal'Ganis","Old Murk-Eye")
#d_s_list=("Mecharoo","")

##"Ironhide Direhorn" no summon,"Soul Juggler",

class minion:
    def __init__(self,na="",at=0,he=0,ch="",t=False,sh=False,p=False,w=1,d=0,m=0,dea=False,g=False,spe="",ra=""):
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
    def get_poison(self):
        return self.poison

    def set_wind(self,w):
        if w != 1 and w != 2 and w != 4:
            print ("error: wrong wind set")
        else:
            self.wind = w
    def get_wind(self):
        return self.wind

    def set_rattle(self,ra):
        if str(ra)== "True" or str(ra)=="False":
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
        if str(dea)== "True" or str(dea)=="False":
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

    def get_calculated_health(self):
        return self.health+self.buff[1]-self.damage
    def get_calculated_attack(self):
        return self.attack + self.buff[0]

    def __str__(self):
        return "name "+self.name+" attack "+str(self.attack)+"+"+str(self.buff[0])+" health "+str(self.health)+"+"+str(self.buff[1])+" damage "+str(self.damage)+" shield "+str(self.shield)+" "+self.special

    def minion_attack(self,other):
          if self.shield:
              self.set_shield(False)
          elif other.poison:
              self.set_damage(other.attack + other.buff[0])
              self.set_death(True)
          else:
              self.set_damage(other.attack+other.buff[0])
             # print (self.damage)

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
                    if lst[j].get_character()==("Murloc" or "All"):
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
                    if lst[j].get_character() == ("Demon" or  "All"):
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
                    if lst[j].get_character() == ("Demon" or  "All"):
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
                    if lst[j].get_character()==("Murloc" or "All"):
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
                    if lst[j].get_character() == ("Demon" or  "All"):
                        if lst[i].get_golden():
                            lst[j].set_buff([2, 0])
                        else:
                            lst[j].set_buff([1, 0])
        elif lst[i].get_special() == "Mal'Ganis" and (not lst[i].get_death()):
            for j in range(minionlist):
                if j == i:
                    pass
                else:
                    if lst[j].get_character() == ("Demon" or  "All"):
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
    be_attack=[]
    aim=-2
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
        be_attack.append(aim)
        usual_minion_battle(m,m_lst[aim])
    elif m.get_special() == ("Foe Reaper 4000" or "Cave Hydra"):
        aim =select_minion(m_lst)
        minionlist = len(m_lst)
   #     if aim !=-1:
        if minionlist == 1:
            m.minion_attack(m_lst[aim])
            m_lst[aim].minion_attack(m)
            be_attack.append( aim)
        elif aim == 0:
            m.minion_attack(m_lst[aim])
            m_lst[aim].minion_attack(m)
            m_lst[aim + 1].minion_attack(m)
            be_attack.append(aim)
            be_attack.append(aim+1)
        elif aim == minionlist - 1:
            m.minion_attack(m_lst[aim])
            m_lst[aim].minion_attack(m)
            m_lst[aim - 1].minion_attack(m)
            be_attack.append(aim)
            be_attack.append(aim-1)
        else:
            m.minion_attack(m_lst[aim])
            m_lst[aim].minion_attack(m)
            m_lst[aim + 1].minion_attack(m)
            m_lst[aim - 1].minion_attack(m)
            be_attack.append(aim)
            be_attack.append(aim-1)
            be_attack.append(aim+1)
        m.set_move(2)
    elif m.get_special() == "The Boogeymonster":
        aim = select_minion(m_lst)
       # if aim!=-1:
        usual_minion_battle(m, m_lst[aim])
        be_attack.append(aim)
        if m_lst[aim].get_damage() >= (m_lst[aim].get_health() + m_lst[aim].get_buff_health()) and m.get_damage() < (m.get_health() + m.get_buff_health()):
            if m.get_golden():
                m.set_health(4)
                m.set_attack(4)
            else:
                m.set_health(2)
                m.set_attack(2)
    elif m.get_special() == "Ironhide Direhorn":
        aim = select_minion(m_lst)
      #  if aim!=-1:
        usual_minion_battle(m, m_lst[aim])
        be_attack.append(aim)
        if m_lst[aim].get_damage() > (m_lst[aim].get_health() + m_lst[aim].get_buff_health()):
            pass #还没有写summon函数
    else:
        aim = select_minion(m_lst)
       # if aim!=-1:
        usual_minion_battle(m, m_lst[aim])
        be_attack.append(aim)
    return [be_attack,id(m_lst[aim])]

def after_attack(lst):
    for i in lst:
        if i.get_special() == "Festeroot Hulk":
            if i.get_golden():
                i.set_attack(2)
            else:
                i.set_attack(1)
def after_death(lst):#dea为二维list，dea[0]=Beast,dea[1]=Mech
    for i in lst:
        if i.get_special() == "Scavenging Hyena":
            if i.get_golden():
                i.set_health(2*dea[0])
                i.set_attack(4*dea[0])
            else:
                i.set_health(dea[0])
                i.set_attack(2*dea[0])
        elif i.get_special() == "Junkbot":
            if i.get_golden():
                i.set_health(4*dea[1])
                i.set_attack(4*dea[1])
            else:
                i.set_health(2*dea[1])
                i.set_attack(2*dea[1])
        else:
            pass

def set_minion(temp,attack_state):#从database的dictionary形式变成minion类
    a=minion(na=temp["name"],at=temp["atk"],he=temp["heath"],ch=temp["tribe"],t=temp["taunt"],sh=temp["divineShield"],p=temp["poisonous"],w=2 if temp["windfury"] else 1)
    if temp["name"] in special_list:
        a.set_special(temp["name"])
    if attack_state==1:
        a.set_move(1)
    if temp["deathrattle"]:
        a.set_deathrattle((temp["name"]))
    return a

class battlefeild:
    def __init__(self, up=[], down=[]):
        self.up = up #记录上方
        self.down = down #记录下方
        #self.begin=None #True 表示上面先动
        self.now =None  #表示运行到第几个,第一表示该第几个，第二表示示该上方或下方,True 表示上方
        self.history = []
        self.atkHistory = []
        self.log = ""
        self.attack_time=1
        self.already_attack=0
        self.dead_minion=False
        self.deathrattle_up=[]
        self.deathrattle_down=[]
        self.attack_flag=False

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
                    "poison": minion.get_poison(),
                    "golden": minion.get_golden(),
                    "death": minion.get_rattle()
                })
        self.history.append(current)

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

    def add_minion(self,mi,side,pos):
        if side=="up":
            if pos>=0 and len(self.up)+1 <= 7:
                self.up.insert(pos,mi)  #这里注意如果列表只有4个minion，直接插入第六个会使其变成第五而不是第六
            else:
                print ("error: wrong position to add a minion1")
        elif side=="down":
            if pos>=0 and len(self.down)+1 <= 7:
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
        origin_minion_buff(self.down)#Old Murk-Eye比较特殊，考虑对面,专门处理
        Murloc_num=0
        for i in self.up:
            if i.get_character()==("Murloc" or "All") :
                Murloc_num+=1
        for i in self.down:
            if i.get_character()==("Murloc" or "All") :
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
                    temp = single_minion_battle(self.up[pos], self.down)
                    attack_state.append(id(self.up[pos]))
                    attack_state.append(temp[1])
                    self.set_attack_time()
                    self.add_already_attack()
                    self.detect_death()
                    self.attack_flag=True
                    after_attack(self.up)
                if pos !=-1:
                    if self.up[pos].get_death():
                        self.attack_over()
            else:
                if (not self.dead_minion) and self.down:
                    attack_state.append(id(self.down[pos]))
                    temp=single_minion_battle(self.down[pos], self.up)
                    attack_state.append(temp[1])
                    self.set_attack_time()
                    self.add_already_attack()
                    self.detect_death()
                    self.attack_flag = True
                    after_attack(self.down)
                if pos!=-1:
                    if self.down[pos].get_death():
                        self.attack_over()
        self.atkHistory.append(attack_state)

    def do_deathrattle(self):
        for i in self.deathrattle_up:
            if i=="Kaboom Bot":
                avail = []
                for i in range(len(self.down)):  # 不选择死亡随从为目标
                    if (not self.down[i].get_death()):
                        avail.append(i)
                if avail:  # 没死光
                    target=random.choice(avail)
                    if self.down[target].get_shield():
                        self.down[target].set_shield(False)
                    else:
                        self.down[target].set_damage(4)
        for i in self.deathrattle_down:
            if i == "Kaboom Bot":
                avail = []
                for i in range(len(self.up)):  # 不选择死亡随从为目标
                    if (not self.up[i].get_death()):
                        avail.append(i)
                if avail:  # 没死光
                    target = random.choice(avail)
                    if self.up[target].get_shield():
                        self.up[target].set_shield(False)
                    else:
                        self.up[target].set_damage(4)
        self.deathrattle_up=[]
        self.deathrattle_down=[]

    def find_deathrattle(self):
        if not self.attack_flag:
            for i in self.up:
                if i.get_death():
                    i.set_rattle(True)
                    lst = i.get_deathrattle().split("+")
                    if lst[0]:
                        for j in lst:
                            self.deathrattle_up.append(j)
            for i in self.down:
                if i.get_death():
                    i.set_rattle(True)
                    lst = i.get_deathrattle().split("+")
                    if lst[0] :
                        for j in lst:
                            self.deathrattle_down.append(j)

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

    def summon(self,lst):
        pass

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

    def renew_buff(self):
        temp_up=[]
        temp_down=[]
        Murloc_num = 0
        for i in self.up:
            temp_up.append(i.get_buff_health())
            i.remove_buff()
            if i.get_character() == ("Murloc" or "All") and (not i.get_death()):
                Murloc_num += 1
        for i in self.down:
            temp_down.append(i.get_buff_health())
            i.remove_buff()
            if i.get_character() == ("Murloc" or "All")  and (not i.get_death()):
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
    field.dump()
   # print (field,"\n")
    while True :
        field.minion_battle()
        field.find_deathrattle()
        field.do_deathrattle()
        field.renew_buff()
       # field.renew_buff()
        field.dump()
        field.remove_death()
        field.detect_death()
        #field.dump()
        field.renew_attack()
        if (field.up_minion()==0 or field.down_minion()==0) and (not field.get_dead_minion()):
            break
       # print ("a")
       # print (field,"\n")
        #print (field.get_already_attack()," ",field.get_attack_time())
   # print (field.log)

'''
if __name__=="__main__":
    a=minion("cat",10,11,spe="Zapp Slywick",g=True,ch="Murloc")
    b=minion("dog",3,12,p=True,ch="Murloc")
    c=minion("cat",10,11,ch="Murloc")
    d=minion("cat",10,11,ch="Murloc")
    e=minion("cat",10,11,ch="Murloc")
    f=minion("cat",10,11,ch="Murloc",spe="Old Murk-Eye")
    g=minion("test",1,3,sh=True,t=True,ch="Murloc")
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

'''
