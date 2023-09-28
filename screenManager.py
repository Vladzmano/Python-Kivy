from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDRaisedButton

### 1st button

class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.button_1 = MDRaisedButton(
            text = 'Go to page 2', 
            pos_hint = {'center_x' : 0.5, 'center_y' : 0.7}, 
            md_bg_color = (1, 0, 0, 1), 
            on_press = lambda x: self.go_to_page_2())

        self.add_widget(self.button_1)
        
    def go_to_page_2(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'secondary'


### 2nd button

class secondary(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.button_2 = MDRaisedButton(
            text = 'Go to page 1', 
            pos_hint = {'center_x' : 0.5, 'center_y' : 0.2 }, 
            md_bg_color = (0, 0, 1, 1), 
            on_press = lambda x: self.go_to_page_1())
        
        self.add_widget(self.button_2)

    def go_to_page_1(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main'



### ======= App goes here ======= ###
  
class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main(name = 'main'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        SC.add_widget(secondary(name = "secondary"))
        return(SC)

wt_app().run()