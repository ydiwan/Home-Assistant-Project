from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class Home(Widget):
    pass

class V1App(App):
    def build(self):
        return Home()

if __name__ == '__main__':
    V1App().run()