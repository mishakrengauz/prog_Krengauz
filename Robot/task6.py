import robot
r = robot.rmap()

r.lm('task6')


def task():

    width = int(input("Введите ширину: "))
    height = int(input("Введите высоту: "))


    for i in range(width):
        r.pt()
        r.rt()
    r.lt(int(width/2)+1)

    if  (width % 2):
        for i in range(height):
            r.pt()
            r.dn()

    else:
        for i in range(height):
            r.pt()
            r.rt()
            r.pt()
            r.dn()
            r.lt()

r.start(task)