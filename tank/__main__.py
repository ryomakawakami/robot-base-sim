import pyglet
import math
import random

robot_image = pyglet.image.load('sprite.png')
robot_image.anchor_x = 50
robot_image.anchor_y = 50
robot = pyglet.sprite.Sprite(robot_image, x=250, y=250)

window = pyglet.window.Window(height=500, width=500)

@window.event
def on_draw():
    window.clear()
    robot.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    robot.update(x=x, y=y, rotation=random.uniform(0, 360))

d_l = 1
d_r = 2

def update(dt):
    d_theta = (d_l - d_r) / 100 + 0.00001
    phi = (math.pi - d_theta) / 2 - robot.rotation * math.pi / 180
    a = (d_l + d_r) * math.sin(d_theta / 2) / d_theta

    robot.update(x=robot.x+a*math.cos(phi), y=robot.y+a*math.sin(phi), rotation=robot.rotation+d_theta*180/math.pi)

pyglet.clock.schedule_interval(update, 1/30.0)
pyglet.app.run()
