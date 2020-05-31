# this is needed for supporting Windows 10 with OpenGL < v2.0
# Example: VirtualBox w/ OpenGL v1.1
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import kivy
#kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

# these next two lines aren't necessary; I'm just testing something for the
# Windows build
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Point, GraphicException

class MyApp(App):

    def build(self):
        return Label(text='Hello world!')


if __name__ == '__main__':
    MyApp().run()


