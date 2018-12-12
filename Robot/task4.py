import robot
r = robot.rmap()
r.lm('task4')


def task():
    while r.fl():
        r.lt()
    while r.fd():
        r.dn()
    for i in range(3):
        for j in range(5):
            r.up()
            r.rt()
            r.pt()
        r.lt(5)
        r.dn(3)


task()