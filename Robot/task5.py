import robot
r = robot.rmap()
r.lm('task5')


for i in range(3):
    for j in range(4):
        r.pt()
        r.dn()
        r.rt()
        r.pt()
        r.rt()
        r.up()
        r.pt()

        if r.fr():
            r.rt()
            r.rt()
    r.dn(3)
    r.lt(14)