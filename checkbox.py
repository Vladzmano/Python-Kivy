from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.checkbox import CheckBox
from kivymd.uix.label import MDLabel

class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

### ======= App goes here ======= ###
        self.cb = CheckBox()
        self.cb.bind(active = self.active)
        self.add_widget(self.cb)

        self.label1 = MDLabel(text ='Disagree', halign = 'center', pos_hint = {'center_y' : 0.2})
        self.add_widget(self.label1)

    def active(self,checkbox, value):
        if value:
            self.label1.text = 'Agree'
        else:
            self.label1.text = 'Disagree'


### ======= App goes here ======= ###
  
class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main(name = 'main'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        return(SC)

wt_app().run()