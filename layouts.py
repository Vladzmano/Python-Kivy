from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDRaisedButton


class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

### ======= App goes here ======= ###

        self.list = StackLayout(size_hint = (1, None), spacing = '5dp', padding = '10dp')

        for i in range(101):
            self.list.add_widget(MDRaisedButton(text = str(i), height = 200, size_hint_y = None))

        self.list.bind(minimum_height = self.list.setter('height'))

        self.scroll = ScrollView()
        self.scroll.add_widget(self.list)

        self.add_widget(self.scroll)

### ======= App goes here ======= ###

class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main(name = 'Main_Page'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        return(SC)

wt_app().run()