import graphics as gr
import time
window = gr.GraphWin("Misha's project", 800, 400)

sky = gr.Line(gr.Point(0, 0), gr.Point(800, 0))
sky.setFill('blue')
sky.setWidth(600)

clouds = []


def sun():
    x = 600
    y = 40
    for i in range(5):

        sun = gr.Circle(gr.Point(600, 40), 30)
        sun.setFill('yellow')
        sun.draw(window)
        sun.move(x+1, y+1)
        i += 1


grass = gr.Line(gr.Point(0, 400), gr.Point(800, 400))
grass.setFill('green')
grass.setWidth(200)


def cloud1():
    global clouds
    cloudpiece1 = gr.Circle(gr.Point(80, 30), 10)
    cloudpiece1.setFill('white')
    cloudpiece2 = gr.Circle(gr.Point(87, 31), 10)
    cloudpiece2.setFill('white')
    cloudpiece3 = gr.Circle(gr.Point(76, 37), 10)
    cloudpiece3.setFill('white')
    cloudpiece4 = gr.Circle(gr.Point(82, 36), 10)
    cloudpiece4.setFill('white')
    cloudpiece5 = gr.Circle(gr.Point(87, 38), 10)
    cloudpiece5.setFill('white')

    cloudpiece1.draw(window)
    cloudpiece2.draw(window)
    cloudpiece3.draw(window)
    cloudpiece4.draw(window)
    cloudpiece5.draw(window)

    clouds.append(cloudpiece1)
    clouds.append(cloudpiece2)
    clouds.append(cloudpiece3)
    clouds.append(cloudpiece4)
    clouds.append(cloudpiece5)


def cloud2():

    cloudpiece6 = gr.Circle(gr.Point(250, 40), 20)
    cloudpiece6.setFill('white')
    cloudpiece7 = gr.Circle(gr.Point(277, 43), 20)
    cloudpiece7.setFill('white')
    cloudpiece8 = gr.Circle(gr.Point(265, 50), 20)
    cloudpiece8.setFill('white')
    cloudpiece9 = gr.Circle(gr.Point(275, 54), 20)
    cloudpiece9.setFill('white')
    cloudpiece10 = gr.Circle(gr.Point(290, 49), 20)
    cloudpiece10.setFill('white')

    cloudpiece6.draw(window)
    cloudpiece7.draw(window)
    cloudpiece8.draw(window)
    cloudpiece9.draw(window)
    cloudpiece10.draw(window)

    clouds.append(cloudpiece6)
    clouds.append(cloudpiece7)
    clouds.append(cloudpiece8)
    clouds.append(cloudpiece9)
    clouds.append(cloudpiece10)


def cloud3():
    cloudpiece11 = gr.Circle(gr.Point(650, 60), 20)
    cloudpiece11.setFill('white')
    cloudpiece12 = gr.Circle(gr.Point(677, 63), 20)
    cloudpiece12.setFill('white')
    cloudpiece13 = gr.Circle(gr.Point(665, 70), 20)
    cloudpiece13.setFill('white')
    cloudpiece14 = gr.Circle(gr.Point(675, 74), 20)
    cloudpiece14.setFill('white')
    cloudpiece15 = gr.Circle(gr.Point(690, 79), 20)
    cloudpiece15.setFill('white')

    cloudpiece11.draw(window)
    cloudpiece12.draw(window)
    cloudpiece13.draw(window)
    cloudpiece14.draw(window)
    cloudpiece15.draw(window)

    clouds.append(cloudpiece11)
    clouds.append(cloudpiece12)
    clouds.append(cloudpiece13)
    clouds.append(cloudpiece14)
    clouds.append(cloudpiece15)


chimney = gr.Line(gr.Point(375, 200), gr.Point(375, 210))
chimney.setWidth(7)

house = gr.Rectangle(gr.Point(300, 210), gr.Point(450, 300))
house.setFill('grey')

window1 = gr.Rectangle(gr.Point(310, 220), gr.Point(340, 250))
window1.setFill('yellow')

window2 = gr.Rectangle(gr.Point(440, 220), gr.Point(410, 250))
window2.setFill('yellow')

sky.draw(window)
sun()
grass.draw(window)
cloud1()
cloud2()
cloud3()
chimney.draw(window)
house.draw(window)
window1.draw(window)
window2.draw(window)

for i in range(100):
    time.sleep(0.00001)
    for cloud in clouds:
        cloud.move(1.5, 0)

window.getMouse()
window.close()
