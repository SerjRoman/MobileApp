from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
import kivy
from kivy.lang import Builder
import os 
# from kivy.core.window import Window
Kv = Builder.load_file(os.path.join(os.path.abspath(__file__+'/..'),'Castomize.kv'))
class WeatherButtonStart(Widget):
    def buttonPress(self):
        print('fkdsdlfksldf')

class WeatherTextInput(Widget):
    def InputText(self):
        print('Text')
       
class RootWidget(Widget):
    pass
class WeatherApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    WeatherApp().run()