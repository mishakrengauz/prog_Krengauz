import graphics as gr
import random
window = gr.GraphWin("Misha's project", 800, 400)


def draw_nature():
    sky = gr.Line(gr.Point(0, 0), gr.Point(800, 0))
    sky.setFill('blue')
    sky.setWidth(600)

    sun = gr.Circle(gr.Point(600, 40), 30)
    sun.setFill('yellow')

    grass = gr.Line(gr.Point(0, 400), gr.Point(800, 400))
    grass.setFill('green')
    grass.setWidth(200)

    sky.draw(window)
    sun.draw(window)
    grass.draw(window)


def draw_cloud():
    for x, y in (40, 70), (55, 75), (150, 60), (167, 65), (410, 100), (440, 95), (460, 115), (520, 250), (530, 240),\
                (620, 150), (630, 170), (650, 150):
        draw_small_cloud(x, y)


def draw_small_cloud(x, y):
    cloud = gr.Circle(gr.Point(x, y), random.randint(10, 30))
    cloud.setFill('white')
    cloud.draw(window)


def draw_house():
    chimney = gr.Line(gr.Point(375, 200), gr.Point(375, 210))
    chimney.setWidth(7)

    house = gr.Rectangle(gr.Point(300, 210), gr.Point(450, 320))
    house.setFill('grey')

    window1 = gr.Rectangle(gr.Point(310, 220), gr.Point(340, 250))
    window1.setFill('yellow')

    window2 = gr.Rectangle(gr.Point(440, 220), gr.Point(410, 250))
    window2.setFill('yellow')

    chimney.draw(window)
    house.draw(window)
    window1.draw(window)
    window2.draw(window)


def main():
    draw_nature()
    draw_cloud()
    draw_house()
    window.getMouse()
    window.close()


if __name__ == "__main__":
    main()
