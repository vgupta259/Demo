import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class StudentDetails(GridLayout):
    def __init__(self,**kwargs):  # **kwargs mean this method can accept multiple paramter
        super(StudentDetails, self).__init__()
        self.cols = 2
        self.add_widget(Label(text = "Student Name:"))
        self.s_name = TextInput(multiline=False)
        self.add_widget(self.s_name)

        self.add_widget(Label(text = "Student Class:"))
        self.s_Class = TextInput(multiline=False)
        self.add_widget(self.s_Class)

        self.add_widget(Label(text = "Student Gender:"))
        self.s_gender = TextInput(multiline=False)
        self.add_widget(self.s_gender)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.submit_event)
        self.add_widget(self.submit)
    
    def submit_event(self,instance):
        print("Done")

class MyApp(App):
    def build(self):
        return StudentDetails()


if __name__ == '__main__':
    MyApp().run()