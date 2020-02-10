from battle import minion, battlefeild, battle

def simple_test0():
    ba = battlefeild()
    return ba
def simple_test1():
    a = minion("a", 6, 16, spe="foe_reaper_4000", g=True, ch="mech")
    ba = battlefeild()
    ba.add_minion(a, "up", 0)
    return ba
def simple_test2():
    a = minion("a", 6, 16, spe="zapp_slywick", g=True, ch="mech")
    ba = battlefeild()
    ba.add_minion(a, "down", 0)
    return ba

def mimi_test():
    a=minion("b", 2, 6, ch="mech", spe="D+kaboom_bot")
    b=minion("b", 6, 10, ch="mech", spe="D+kaboom_bot")
    ba = battlefeild()
    ba.add_minion(b, "up", 0)
    ba.add_minion(a, "down", 0)
    return ba

def test1():
    a = minion("a", 6, 16, spe="foe_reaper_4000", g=True, ch="mech")
    b = minion("b", 6, 10, ch="mech", spe="D+kaboom_bot")
    c = minion("c", 10, 11, ch="mech", spe="D+kaboom_bot")
    d = minion("d", 6, 11, ch="mech", spe="D+kaboom_bot")
    e = minion("e", 6, 16, ch="mech", spe="D+kaboom_bot")
    f = minion("f", 7, 15, ch="mech", spe="D+kaboom_bot")
    g = minion("g", 5, 12, sh=True, t=True, ch="mech", spe="D+kaboom_bot")
    h = minion("h", 22, 6, sh=True, g=True, ch="murloc", spe="oldmurkeye")
    i = minion("i", 12, 12, sh=True, ch="murloc")
    j = minion("j", 5, 12, sh=True, ch="murloc")
    k = minion("k", 6, 12, sh=True, ch="murloc")
    l = minion("l", 8, 12, sh=True, ch="murloc")
    m = minion("m", 4, 6, t=True)
    n = minion("n", 5, 12, sh=True, ch="murloc", spe="murloc_warleader")
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
