import random
ch_list=("beast","murloc","mech","demon","all")
special_list=("dire_worf_alpha","murloc_warleader","phalanx_commander","siege_breaker","malganis","oldmurkeye",\
              "zapp_slywick","foe_reaper_4000","cave_hydra","ironhide_direhorn","the_boogeymonster","festeroot_hulk","scavenging_hyena","junkbot", "soul_juggler")
#m_b_list=("dire_worf_alpha","murloc_warleader","phalanx_commander","siege_breaker","malganis","oldmurkeye")
#d_s_list=("Mecharoo","")

##"ironhide_direhorn" no summon,"soul_juggler",

class minion:
    def __init__(self,na="",at=0,he=0,ch="",t=False,sh=False,p=False,w=1,d=0,m=0,dea=False,g=False,spe=""):
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

    def get_poison(self):
        return self.poison

    def set_wind(self,w):
        if w != 1 and w != 2 and w != 4:
            print ("error: wrong wind set")
        else:
            self.wind = w

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

    def set_death(self,dea):
        if str(dea)== "True" or str(dea)=="False":
            self.death = dea
        else:
            print ("error: wrong death set")

    def get_death(self):
        return self.death

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
              self.set_damage(10000) #poison is 10000 attack
          else:
              self.set_damage(other.attack+other.buff[0])
             # print (self.damage)

    def __eq__(self, other):
        if self.name==other.name:
            return True
        else:
            return False

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
        if lst[i].get_special()=="dire_worf_alpha" and (not lst[i].get_death()):
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
        elif lst[i].get_special()=="murloc_warleader" and (not lst[i].get_death()):
            for j in range(minionlist):
                if j==i:
                    pass
                else:
                    if lst[j].get_character()==("murloc" or "all"):
                        if lst[i].get_golden():
                            lst[j].set_buff([4, 0])
                        else:
                            lst[j].set_buff([2, 0])
        elif lst[i].get_special()=="phalanx_commander" and (not lst[i].get_death()):
            for j in range(minionlist):
                if lst[j].get_taunt():
                    if lst[i].get_golden():
                        lst[j].set_buff([4, 0])
                    else:
                        lst[j].set_buff([2, 0])
        elif lst[i].get_special()=="siege_breaker" and (not lst[i].get_death()):
            for j in range(minionlist):
                if j == i:
                    pass
                else:
                    if lst[j].get_character() == ("demon" or  "all"):
                        if lst[i].get_golden():
                            lst[j].set_buff([2, 0])
                        else:
                            lst[j].set_buff([1, 0])
        elif lst[i].get_special() == "malganis" and (not lst[i].get_death()):
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
def usual_minion_battle(minion1,minion2): #minion1是攻击方
    minion1.minion_attack(minion2)
    minion2.minion_attack(minion1)
    minion1.set_move(2)
def single_minion_battle(m,m_lst):
    be_attack=[]
    aim=-2
    if m.get_special() == "zapp_slywick":
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
    elif m.get_special() == ("foe_reaper_4000" or "cave_hydra"):
        aim =select_minion(m_lst)
        minionlist = len(m_lst)
        if aim !=-1:
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
    elif m.get_special() == "the_boogeymonster":
        aim = select_minion(m_lst)
        if aim!=-1:
            usual_minion_battle(m, m_lst[aim])
            be_attack.append(aim)
            if m_lst[aim].get_damage() >= (m_lst[aim].get_health() + m_lst[aim].get_buff_health()) and m.get_damage() < (m.get_health() + m.get_buff_health()):
                if m.get_golden():
                    m.set_health(4)
                    m.set_attack(4)
                else:
                    m.set_health(2)
                    m.set_attack(2)
    elif m.get_special() == "ironhide_direhorn":
        aim = select_minion(m_lst)
        if aim!=-1:
            usual_minion_battle(m, m_lst[aim])
            be_attack.append(aim)
            if m_lst[aim].get_damage() > (m_lst[aim].get_health() + m_lst[aim].get_buff_health()):
                pass #还没有写summon函数
    else:
        aim = select_minion(m_lst)
        if aim!=-1:
            usual_minion_battle(m, m_lst[aim])
            be_attack.append(aim)
    return [be_attack,id(m_lst[aim])]

def after_attack(lst):
    for i in lst:
        if i.get_special() == "festeroot_hulk":
            if i.get_golden():
                i.set_attack(2)
            else:
                i.set_attack(1)
def after_death(lst,dea):#dea为二维list，dea[0]=beast,dea[1]=mech
    for i in lst:
        if i.get_special() == "scavenging_hyena":
            if i.get_golden():
                i.set_health(2*dea[0])
                i.set_attack(4*dea[0])
            else:
                i.set_health(dea[0])
                i.set_attack(2*dea[0])
        elif i.get_special() == "junkbot":
            if i.get_golden():
                i.set_health(4*dea[1])
                i.set_attack(4*dea[1])
            else:
                i.set_health(2*dea[1])
                i.set_attack(2*dea[1])
        else:
            pass
class battlefeild:
    def __init__(self, up=[], down=[],upa=[],downa=[]):
        self.up = up #记录上方
        self.down = down #记录下方
        self.up_after_attack=upa
        self.down_after_attack=downa
        #self.begin=None #True 表示上面先动
        self.now =None  #表示运行到第几个,第一表示该第几个，第二表示示该上方或下方,True 表示上方
        self.history = []
        self.atkHistory = []
        self.log = ""
        self.attack_time=1
        self.already_attack=1

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
                    "golden": minion.get_golden()
                })
        self.history.append(current)

    def set_now(self,num,side):
        if num>6 or num<0:
            print ("error: wrong position")
        elif str(side) !="True" and str(side) !="False":
            print ("error: wrong side")
        else:
            self.now=[num,side]

    def set_attack_time(self):
        if self.now[1]:
            print (self.now)
            self.attack_time=self.up[self.now[0]].get_wind()
        else:
            self.attack_time=self.down[self.now[0]].get_wind()
    def get_attack_time(self):
        return self.attack_time

    def reset_already_attack(self):
        self.already_attack=1
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
            self.set_attack_time()
        elif minionup< miniondown:
            #self.begin=False
            self.set_now(0, False)
            self.set_attack_time()
        else:
            a=random.random()
            if a>=0.5:
               # self.begin = True
                self.set_now(0, True)
                self.set_attack_time()
            else:
                #self.begin =False
                self.set_now(0,False)
                self.set_attack_time()
        origin_minion_buff(self.up)
        origin_minion_buff(self.down)#oldmurkeye比较特殊，考虑对面,专门处理
        murloc_num=0
        for i in self.up:
            if i.get_character()==("murloc" or "all") :
                murloc_num+=1
        for i in self.down:
            if i.get_character()==("murloc" or "all") :
                murloc_num+=1
        for i in self.up:
            if i.get_special() == "oldmurkeye" :
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

    #self.up_after_attack = copy(self.up)
    #self.down_after_attack = copy(self.down)

    def minion_battle(self):
        side = self.now[1]
        pos=self.now[0]
        attack_state=[]
        if  str(side) !="True" and str(side) !="False":
            print ("error: which side to attack")
        elif side:
            attack_state.append(id(self.up[pos]))
            temp=single_minion_battle(self.up[pos],self.down)
            attack_state.append(temp[1])
            self.detect_death()
            after_attack(self.up)
            attack_state.append(self.up[pos].get_death())
        else:
            attack_state.append(id(self.down[pos]))
            temp=single_minion_battle(self.down[pos], self.up)
            attack_state.append(temp[1])
            self.detect_death()
            after_attack(self.down)
            attack_state.append(self.down[pos].get_death())
        return attack_state


    def detect_death(self):
        for i in self.up:
            if i.get_damage()>= (i.get_health()+i.get_buff_health()):
                #print (i.get_damage(),i.get_health()+i.get_buff_health(),"up")
                i.set_death(True)
        for j in self.down:
            if j.get_damage()>= (j.get_health()+j.get_buff_health()):
                #print (j.get_damage(),j.get_health()+j.get_buff_health(),"down")
                j.set_death(True)

    def remove_death(self):
        self.up=list(filter(lambda x: not x.get_death(), self.up))
        self.down=list(filter(lambda x: not x.get_death(), self.down))

    def summon(self,lst):
        pass

    def renew_attack(self):
        if self.attack_time>self.already_attack:#未到行动数
            side=self.now[1]
            if side:  #找到该谁行动，更新序号
                num=-1
                for i in range(len(self.up)):
                    if self.up[i].get_move()==2:
                        num=i
                        break
                if num==-1:
                    print("error: no one attack")
                else:
                    self.set_now(num,side)
                    self.add_already_attack()
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
                    self.add_already_attack()
        else:
            self.reset_already_attack()
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
                if len(self.up)!=0:
                    for i in range(len(self.up)):
                        if self.up[i].get_move()==0:
                            uppos=i
                            break
                    if uppos==-1:
                        uppos=0
                        for i in self.up:
                            i.set_move(0)
                    self.set_now(uppos,side)
                    self.set_attack_time()
                else:
                    pass
            else:
                if len(self.down)!=0:
                    for j in range(len(self.down)):
                        if self.down[j].get_move()==0:
                            downpos=j
                            break
                    if downpos==-1:
                        downpos=0
                        for i in self.down:
                            i.set_move(0)
                    self.set_now(downpos, side)
                    self.set_attack_time()
                else:
                    pass

    def renew_buff(self):
        temp_up=[]
        temp_down=[]
        murloc_num = 0
        for i in self.up:
            temp_up.append(i.get_buff_health())
            i.remove_buff()
            if i.get_character() == ("murloc" or "all") and (not i.get_death()):
                murloc_num += 1
        for i in self.down:
            temp_down.append(i.get_buff_health())
            i.remove_buff()
            if i.get_character() == ("murloc" or "all")  and (not i.get_death()):
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
    field.dump()
    print (field,"\n")
    while field.up_minion()>0 and field.down_minion()>0:
        attack_list=field.minion_battle()
        field.atkHistory.append(attack_list[0:2])
        if attack_list[2]:
            field.attack_over()
        #print (attack_list)
        #field.detect_death()
        #field.dump()
        field.renew_buff()
        field.remove_death()
        field.renew_attack()
        field.dump()
        print (field,"\n")
        #print (field.get_already_attack()," ",field.get_attack_time())
    print (field.log)

'''
if __name__=="__main__":
    a=minion("cat",10,11,spe="zapp_slywick",g=True,ch="murloc")
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


lst=[0,2,3]
lst.insert(6,'x')
print (lst,len(lst))
'''
