import kivy

kivy.require('2.1.0') # replace with your current kivy version !
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

numer = 0

def wiecej():
    global numer
    numer += 1

def mniej():
    global numer
    numer -= 1

if numer == -1:
    numer = 359

if numer == 360:
    numer = 0




class Rotot(BoxLayout):
    def __init__(self, **args):
        super(Rotot, self).__init__(**args)
        minus = Button(text="po")
        minus.bind(on_press=mniej)
        self.add_widget(minus)
        label = Label(text=str(numer))
        self.add_widget(label)
        plus = Button(text="pis")
        plus.bind(on_press=wiecej)
        self.add_widget(plus)




class MyApp(App):
    def build(self):
        self.root = root = Rotot()
        return root

if __name__ == '__main__':
    MyApp().run()

