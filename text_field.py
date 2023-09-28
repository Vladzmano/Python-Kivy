from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import *
from kivymd.uix.slider import MDSlider


class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

### ======= App goes here ======= ###


        self.text = MDTextField(hint_text = 'Sound', helper_text = 'Please set volume/sound level', helper_text_mode = 'on_focus',
        on_text_validate = lambda x: self.check_text())
        self.text.pos_hint = {'center_x' : 0.5, 'center_y' : 0.5}
        self.text.size_hint =(0.4, None)
        self.add_widget(self.text)

        self.sl = MDSlider(pos_hint = {'center_y' : 0.3})
        self.add_widget(self.sl)

    def check_text(self):
        self.sl.value = float(self.text.text)



### ======= App goes here ======= ###
  
class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main(name = 'Main_Page'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        return(SC)

wt_app().run()