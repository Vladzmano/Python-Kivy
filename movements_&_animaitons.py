from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDRaisedButton
from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.properties import Clock


class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

### ======= App goes here ======= ###

        with self.canvas:
            Color(1, 0, 0, 1)
            self.rect = Rectangle(pos = self.center)


            Color(0, 0, 1, 1)
            self.cir = Ellipse (pos =self.center)

        self.button_1 = MDRaisedButton(text = 'Move', on_press =lambda x: self.move())
        self.add_widget(self.button_1)
        Clock.schedule_interval(self.update, 1/10)

    def on_size(self, *args):
        self.rect.pos = (self.center_x-(self.rect.size[0]/2), self.center_y-(self.rect.size[1]/2))
        self.cir.pos = (self.center_x-(self.cir.size[0]/2), self.center_y-(self.cir.size[1]/2))

    def move(self):
        self.rect.pos = (self.rect.pos[0] + 10, self.rect.pos[1])
        self.cir.pos = (self.cir.pos[0] - 10, self.cir.pos[1])

    def update(self, dt):
        self.rect.pos = (self.rect.pos[0], self.rect.pos[1] - 2)
        self.cir.pos = (self.cir.pos[0], self.cir.pos[1] + 2)

### ======= App goes here ======= ###
  
class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main(name = 'Main_Page'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        return(SC)

wt_app().run()