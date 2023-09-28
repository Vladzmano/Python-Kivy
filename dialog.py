from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix. button import MDRaisedButton

class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

### ======= App goes here ======= ###

        self.button_1 = MDRaisedButton(text = 'Exit', on_press = lambda x: self.exit())
        self.add_widget(self.button_1)

    def exit(self):
        self.day = MDDialog(text = 'Are you sure you want to exit?', 
        buttons = [MDRaisedButton(text= 'Yes', on_press = lambda x: quit()), MDRaisedButton(text = 'No', on_press = lambda x : self.day.dismiss())])
        self.day.open()



### ======= App goes here ======= ###
  
class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main(name = 'Main_Page'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        return(SC)

wt_app().run()