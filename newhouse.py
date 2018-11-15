#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 08:06:14 2018
@author: mihailkrengauz
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 07:42:05 2018
@author: Михаил
"""

import graphics as gr

window = gr.GraphWin("Misha's project", 800, 400)

sky = gr.Line(gr.Point(0, 0), gr.Point(800, 0))
sky.setFill('blue')
sky.setWidth(600)

sun = gr.Circle(gr.Point(600, 40), 30)
sun.setFill('yellow')

grass = gr.Line(gr.Point(0, 400), gr.Point(800, 400))
grass.setFill('green')
grass.setWidth(200)


def cloud1():
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


def cloud2():
    cloudpiece1 = gr.Circle(gr.Point(250, 40), 20)
    cloudpiece1.setFill('white')
    cloudpiece2 = gr.Circle(gr.Point(277, 43), 20)
    cloudpiece2.setFill('white')
    cloudpiece3 = gr.Circle(gr.Point(265, 50), 20)
    cloudpiece3.setFill('white')
    cloudpiece4 = gr.Circle(gr.Point(275, 54), 20)
    cloudpiece4.setFill('white')
    cloudpiece5 = gr.Circle(gr.Point(290, 49), 20)
    cloudpiece5.setFill('white')

    cloudpiece1.draw(window)
    cloudpiece2.draw(window)
    cloudpiece3.draw(window)
    cloudpiece4.draw(window)
    cloudpiece5.draw(window)


def cloud3():
    cloudpiece1 = gr.Circle(gr.Point(650, 60), 20)
    cloudpiece1.setFill('white')
    cloudpiece2 = gr.Circle(gr.Point(677, 63), 20)
    cloudpiece2.setFill('white')
    cloudpiece3 = gr.Circle(gr.Point(665, 70), 20)
    cloudpiece3.setFill('white')
    cloudpiece4 = gr.Circle(gr.Point(675, 74), 20)
    cloudpiece4.setFill('white')
    cloudpiece5 = gr.Circle(gr.Point(690, 79), 20)
    cloudpiece5.setFill('white')

    cloudpiece1.draw(window)
    cloudpiece2.draw(window)
    cloudpiece3.draw(window)
    cloudpiece4.draw(window)
    cloudpiece5.draw(window)


chimney = gr.Line(gr.Point(375, 200), gr.Point(375, 210))
chimney.setWidth(7)

house = gr.Rectangle(gr.Point(300, 210), gr.Point(450, 300))
house.setFill('grey')

window1 = gr.Rectangle(gr.Point(310, 220), gr.Point(340, 250))
window1.setFill('yellow')

window2 = gr.Rectangle(gr.Point(440, 220), gr.Point(410, 250))
window2.setFill('yellow')

sky.draw(window)
sun.draw(window)
grass.draw(window)
cloud1()
cloud2()
cloud3()
chimney.draw(window)
house.draw(window)
window1.draw(window)
window2.draw(window)

window.getMouse()
window.close()