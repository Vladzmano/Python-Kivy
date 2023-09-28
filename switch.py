from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.switch import Switch


class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

### ======= App goes here ======= ###

        self.sw = Switch()
        self.sw.bind(active = self.trigger)
        self.add_widget(self.sw)
    
    def trigger(self, switch, value):
        if value:
            print('I love sushi')
        else:
            print('Dont like sushi')





### ======= App goes here ======= ###
  
class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main(name = 'Main_Page'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        return(SC)

wt_app().run()