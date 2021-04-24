from kivy.app import App
from kivy.uix.label import Label

class Test(App):
    def build(self):
        return Label(text='This is me')


if __name__ == '__main__':
    Test().run()