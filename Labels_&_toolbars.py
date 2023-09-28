from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel


class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

### ======= App goes here ======= ###

        self.toolbar = MDTopAppBar(title = 'The App is up and running', 
                                   anchor_title = "center", 
                                   pos_hint = {'top': 1})
                                   #material_style = 'M3'
        
        self.label1 = MDLabel(text = "Nice app", 
                              halign = "center", 
                              theme_text_color = "Custom", 
                              text_color = "white", 
                              font_style = 'H6', 
                              pos_hint = {'center_x' : 0.5, 'center_y' : 0.15})

        self.add_widget(self.toolbar) 
        self.add_widget(self.label1)

### ======= App goes here ======= ###

class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main(name = 'Main_Page'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        return(SC)

wt_app().run()