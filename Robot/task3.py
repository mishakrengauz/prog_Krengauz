import robot
r = robot.rmap()
r.lm('task3')

def task():
    for i in range(4):
        r.rt()
        r.rt()
        r.dn()
        r.up()

task()