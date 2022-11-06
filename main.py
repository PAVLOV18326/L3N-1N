import kivy

kivy.require('2.1.0') # replace with your current kivy version !
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

numer = 0

def mniej():
    global numer
    numer -= 1

def wiecej():
    global numer
    numer += 1

if numer == -1:
    numer = 359

if numer == 360:
    numer = 0




class Rotot(BoxLayout):
    def __init__(self, **args):
        super(Rotot, self).__init__(**args)
        label = Label(text=str(numer))
        self.add_widget(label)




class MyApp(App):
    def build(self):
        self.root = root = Rotot()
        return root

if __name__ == '__main__':
    MyApp().run()

if __name__ == '__main__':
    MyApp().run()