from battle import minion, battlefeild, battle

def simple_test0():#啥都没有，基础检测
    ba = battlefeild()
    return ba
def simple_test1():#只有上面，基础检测
    a = minion("Zapp Slywick", 6, 16, spe="Zapp Slywick", g=True)
    ba = battlefeild()
    ba.add_minion(a, "up", 0)
    return ba
def simple_test2():#只有下面，基础检测
    a = minion("Zapp Slywick", 6, 16, spe="Zapp Slywick", g=True)
    ba = battlefeild()
    ba.add_minion(a, "down", 0)
    return ba
def simple_test3():#简单对撞
    a = minion("Zapp Slywick", 6, 16, spe="Zapp Slywick", g=True)
    b = minion("Zapp Slywick", 6, 16, spe="Zapp Slywick")
    ba = battlefeild()
    ba.add_minion(a, "down", 0)
    ba.add_minion(b, "up", 0)
    return ba

def test1():#检测狂战，腐树，爆爆，老瞎眼
    a = minion("Foe Reaper 4000", 6, 16, spe="Foe Reaper 4000", g=True, ch="Mech")
    b = minion("Kaboom Bot", 6, 10, ch="Mech", ra="Kaboom Bot")
    c = minion("Kaboom Bot", 10, 11, ch="Mech", ra="Kaboom Bot")
    d = minion("Kaboom Bot", 6, 11, ch="Mech", ra="Kaboom Bot")
    e = minion("Kaboom Bot", 6, 16, ch="Mech", ra="Kaboom Bot")
    f = minion("Kaboom Bot", 7, 15, ch="Mech", ra="Kaboom Bot")
    g = minion("Kaboom Bot", 5, 12, sh=True, t=True, ch="Mech", ra="Kaboom Bot")
    h = minion("Old Murk-Eye", 22, 6, sh=True, g=True, ch="Murloc", spe="Old Murk-Eye")
    i = minion("Murloc Tidehunter", 12, 12, sh=True, ch="Murloc")
    j = minion("Murloc Tidehunter", 5, 12, sh=True, ch="Murloc")
    k = minion("Murloc Tidehunter", 6, 12, sh=True, ch="Murloc")
    l = minion("Festeroot Hulk", 8, 12, sh=True, spe="Festeroot Hulk")
    m = minion("Brann Bronzebeard", 4, 6, t=True)
    n = minion("Murloc Warleader", 5, 12, sh=True, ch="Murloc", spe="Murloc Warleader")
    ba = battlefeild()
    ba.add_minion(b, "up", 0)
    ba.add_minion(a, "up", 1)
    ba.add_minion(c, "up", 2)
    ba.add_minion(d, "up", 3)
    ba.add_minion(e, "up", 4)
    ba.add_minion(f, "up", 5)
    ba.add_minion(g, "up", 6)
    ba.add_minion(h, "down", 0)
    ba.add_minion(i, "down", 1)
    ba.add_minion(j, "down", 2)
    ba.add_minion(k, "down", 3)
    ba.add_minion(l, "down", 4)
    ba.add_minion(m, "down", 5)
    ba.add_minion(n, "down", 6)
    return ba

def test2():
    a = minion("Foe Reaper 4000", 6, 16, spe="Foe Reaper 4000", g=True, ch="Mech")
    n = minion("Murloc Warleader", 12, 112,  ch="Murloc", spe="Murloc Warleader")
    ba = battlefeild()
    ba.add_minion(a, "up", 1)
    ba.add_minion(n, "down", 6)
    return ba

def test3():#检测生命buff刷新
    a = minion("Mal'Ganis", 16, 6, spe="Mal'Ganis",g=True, ch="Demon")
    b= minion("Nathrezim Overseer", 6, 16, t=True, ch="Demon")
    c=minion("Nathrezim Overseer", 3, 4, ch="Demon")
    d=minion("Nathrezim Overseer", 6, 16, ch="Demon")
    e = minion("Murloc Warleader", 12, 112, t=True, ch="Murloc", spe="Murloc Warleader")
    ba = battlefeild()
    ba.add_minion(a, "up", 0)
    ba.add_minion(b, "up", 1)
    ba.add_minion(c, "down", 0)
    ba.add_minion(d, "down", 1)
    ba.add_minion(e, "down", 2)
    return ba

def test4():#检测伯瓦尔，金爆爆
    a = minion("Foe Reaper 4000", 6, 16, spe="Foe Reaper 4000", g=True, ch="Mech")
    b = minion("Kaboom Bot", 6, 10, ch="Mech", ra="Kaboom Bot")
    c = minion("Kaboom Bot", 10, 11, ch="Mech", ra="Kaboom Bot")
    d = minion("Kaboom Bot", 6, 11, ch="Mech", ra="Kaboom Bot")
    e = minion("Kaboom Bot", 6, 16, ch="Mech", ra="Kaboom Bot")
    f = minion("Kaboom Bot", 7, 15, ch="Mech", g=True,ra="Kaboom Bot")
    g = minion("Kaboom Bot", 5, 12, sh=True, t=True, ch="Mech", ra="Kaboom Bot")
    h = minion("Old Murk-Eye", 22, 6, sh=True, g=True, ch="Murloc", spe="Old Murk-Eye")
    i =minion("Bolvar, Fireblood", 8, 12, sh=True, spe="Bolvar, Fireblood")
    j = minion("Murloc Tidehunter", 5, 12, sh=True, ch="Murloc")
    k = minion("Murloc Tidehunter", 6, 12, sh=True, ch="Murloc")
    l = minion("Murloc Tidehunter", 12, 12, sh=True, ch="Murloc")
    m = minion("Brann Bronzebeard", 4, 6, t=True)
    n = minion("Murloc Warleader", 5, 12, sh=True, ch="Murloc", spe="Murloc Warleader")
    ba = battlefeild()
    ba.add_minion(b, "up", 0)
    ba.add_minion(a, "up", 1)
    ba.add_minion(c, "up", 2)
    ba.add_minion(d, "up", 3)
    ba.add_minion(e, "up", 4)
    ba.add_minion(f, "up", 5)
    ba.add_minion(g, "up", 6)
    ba.add_minion(h, "down", 0)
    ba.add_minion(i, "down", 1)
    ba.add_minion(j, "down", 2)
    ba.add_minion(k, "down", 3)
    ba.add_minion(l, "down", 4)
    ba.add_minion(m, "down", 5)
    ba.add_minion(n, "down", 6)
    return ba

def test5():#检测爆爆，伯瓦尔互动
    a=minion("Kaboom Bot", 6, 6, ch="Mech", g=True,ra="Kaboom Bot")
    b= minion("Murloc Tidehunter", 6, 6, ch="Murloc")
    c= minion("Murloc Tidehunter", 5, 4, sh=True, ch="Murloc")
    d =minion("Bolvar, Fireblood", 8, 12, sh=True, spe="Bolvar, Fireblood")
    ba = battlefeild()
    ba.add_minion(a, "up", 0)
    ba.add_minion(b, "down", 0)
    ba.add_minion(c, "down", 1)
    ba.add_minion(d, "down", 2)
    return ba

def test6():#检测零攻互动
    a=minion("Kaboom Bot", 4, 12, ch="Mech", g=True,ra="Kaboom Bot")
    b= minion("Murloc Tidehunter", 0, 6, ch="Murloc")
    c= minion("Murloc Tidehunter", 0, 6, ch="Murloc")
    d =minion("Bolvar, Fireblood", 0, 12, sh=True, spe="Bolvar, Fireblood")
    e =minion("Bolvar, Fireblood", 0, 12, sh=True, spe="Bolvar, Fireblood")
    f= minion("Murloc Tidehunter", 0, 6, ch="Murloc")
    g = minion("Festeroot Hulk", 0, 12,  spe="Festeroot Hulk")
    ba = battlefeild()
    ba.add_minion(a, "up", 0)
    ba.add_minion(b, "down", 0)
    ba.add_minion(c, "down", 1)
    ba.add_minion(d, "down", 1)
    ba.add_minion(e,"down",3)
    ba.add_minion(f,"down",4)
    ba.add_minion(g,"down",5)
    return ba

def test7():#检测恐狼，土狼，喷子
    a=minion("Kaboom Bot", 6, 6, ch="Mech", g=True,ra="Kaboom Bot")
    b= minion("Murloc Tidehunter", 6, 6, ch="Murloc")
    c= minion("Murloc Tidehunter", 5, 4, sh=True, ch="Murloc")
    d =minion("Bolvar, Fireblood", 8, 12, sh=True, spe="Bolvar, Fireblood")
    ba = battlefeild()
    ba.add_minion(a, "up", 0)
    ba.add_minion(b, "down", 0)
    ba.add_minion(c, "down", 1)
    ba.add_minion(d, "down", 2)
    return ba