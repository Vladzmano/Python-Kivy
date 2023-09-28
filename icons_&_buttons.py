from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDFillRoundFlatIconButton

class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.button_1 = MDFillRoundFlatIconButton(
            
            text = 'Next ', 
            icon = 'check', 
            pos_hint = {'center_x' : 0.5, 'center_y' : 0.2},
            size_hint = (0.5, 0.2),
            on_press = lambda x: self.press())
                                                
        self.add_widget(self.button_1)

    #def on_size(seld, *args):
     #   self.button_1.size_hint = (0.5, 0.2)

    def press(self):
        print("Osa")


class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main(name = 'Main_Page'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        return(SC)

wt_app().run()