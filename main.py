import kivy

kivy.require('2.1.0') # replace with your current kivy version !
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class Rotot(BoxLayout):
    def __init__(self, **args):
        super(Rotot, self).__init__(**args)

        minus = Button(text="lewo")
        minus.bind(on_press=self.mniej)
        self.numer = 0
        self.add_widget(minus)
        self.label = Label(text=str(self.numer))
        self.add_widget(self.label)
        plus = Button(text="prawo")
        plus.bind(on_press=self.wiecej)
        self.add_widget(plus)



    def wiecej(self, x):
        self.numer += 1

        if self.numer == -1:
            self.numer = 359

        if self.numer == 360:
            self.numer = 0

        self.label.text = str(self.numer)

    def mniej(self, x):
        self.numer -= 1

        if self.numer == -1:
            self.numer = 359

        if self.numer == 360:
            self.numer = 0

        self.label.text = str(self.numer)






class MyApp(App):
    def build(self):
        self.root = root = Rotot()
        return root

if __name__ == '__main__':
    MyApp().run()

