from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager

class  main_screen(Screen):
    pass

class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main_screen(name = 'Main_Page'))

        return(SC)

wt_app().run()