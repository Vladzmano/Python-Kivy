from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.slider import MDSlider
from kivymd.uix.button import MDRaisedButton

class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

### ======= App goes here ======= ###

        self.slider_1 = MDSlider()
        self.slider_1.size_hint = (0.5, 0.5)
        self.slider_1.pos_hint = {'center_x' : 0.5, 'center_y' : 0.5}
        self.slider_1.color = 'red'
        self.slider_1.orientation = 'horizontal'
        self.slider_1.value = 80
        self.add_widget(self.slider_1)

        self.button_1 = MDRaisedButton(text = "Press here", on_press = lambda x: self.value())
        self.add_widget(self.button_1)


    def value(self):
        print(self.slider_1.value)

### ======= App goes here ======= ###
  
class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main(name = 'Main_Page'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        return(SC)

wt_app().run()