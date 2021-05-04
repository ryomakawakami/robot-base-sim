import pyglet
import math
import random

slew = 20
speed = 200

class RobotBase:
    def __init__(self):
        self.x = 250
        self.y = 250
        self.theta = 0
        self.v_l = 0
        self.v_r = 0

        # Target velocities
        self.target_l = 0
        self.target_r = 0

    def update_target(self, dv_l, dv_r):
        self.target_l += dv_l
        self.target_r += dv_r

    def update(self, dt):
        # Get wheel distances
        d_l = self.v_l * dt
        d_r = self.v_r * dt

        # Update positions
        d_theta = (d_l - d_r) / 100 + 0.00001
        phi = (math.pi - d_theta) / 2 - self.theta
        a = (d_l + d_r) * math.sin(d_theta / 2) / d_theta

        self.x += a * math.cos(phi)
        self.y += a * math.sin(phi)
        self.theta += d_theta

        # Update velocities
        if abs(self.v_l - self.target_l) < slew:
            self.v_l = self.target_l
        elif self.v_l < self.target_l:
            self.v_l += slew
        else:
            self.v_l -= slew

        if abs(self.v_r - self.target_r) < slew:
            self.v_r = self.target_r
        elif self.v_r < self.target_r:
            self.v_r += slew
        else:
            self.v_r -= slew

base = RobotBase()

robot_image = pyglet.image.load('sprite.png')
robot_image.anchor_x = 50
robot_image.anchor_y = 50
robot = pyglet.sprite.Sprite(robot_image, x=250, y=250)

window = pyglet.window.Window(height=500, width=500)

@window.event
def on_draw():
    window.clear()
    robot.draw()

# @window.event
# def on_mouse_press(x, y, button, modifiers):
#     robot.update(x=x, y=y, rotation=random.uniform(0, 360))

@window.event
def on_key_press(symbol, modifiers):
    if symbol == 119:
        base.update_target(speed, speed)
    elif symbol == 97:
        base.update_target(-speed, speed)
    elif symbol == 115:
        base.update_target(-speed, -speed)
    elif symbol == 100:
        base.update_target(speed, -speed)

@window.event
def on_key_release(symbol, modifiers):
    if symbol == 119:
        base.update_target(-speed, -speed)
    elif symbol == 97:
        base.update_target(speed, -speed)
    elif symbol == 115:
        base.update_target(speed, speed)
    elif symbol == 100:
        base.update_target(-speed, speed)

def update(dt):
    base.update(dt)
    robot.update(x=base.x, y=base.y, rotation=base.theta*180/math.pi)

pyglet.clock.schedule_interval(update, 1/30.0)
pyglet.app.run()
