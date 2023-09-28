from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Ellipse, Line


class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

### ======= App goes here ======= ###

        with self.canvas:
            Color(1, 0, 0, 0.8)
            self.rect = Rectangle(pos = self.center, size = (200, 100))

            Color(0, 0, 1, 1)
            self.ellipse = Ellipse(pos = (200, 200), size = (50, 100))

            Color(1, 1, 1, 1)
            self.line_1 = Line(points = (0, 0, self.width/2, self.height, self.width, 0), width =2)

            Color(0, 1, 0, 1)
            self.line_2 = Line(circle = (200, 300, 50), width = 3)

            Color(1, 1, 1, 1)
            self.line_3 = Line(rectangle = (500, 300, 100, 50), width =2.5)

    def on_size(self, *args):
        self.rect.pos = (self.center_x-(self.rect.size[0]/2),self.center_y-(self.rect.size[1]/2))
        self.line_1.points = (0, 0, self.width/2, self.height, self.width, 0)

### ======= App goes here ======= ###
  
class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main(name = 'Main_Page'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        return(SC)

wt_app().run()