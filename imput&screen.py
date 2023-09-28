from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDRaisedButton
from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.properties import Clock
from kivy.core.window import Window

class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

### ======= App goes here ======= ###
        
        self.change_x = 0
        self.change_y = 0

        self._keyboard = Window.request_keyboard(self.keyboard_closed,self)
        self._keyboard.bind(on_key_down = self.on_keyboard_down)

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
        self.rect.pos = (self.rect.pos[0] + self.change_x, self.rect.pos[1] - +self.change_y)
        self.cir.pos = (self.cir.pos[0] - self.change_x, self.cir.pos[1] + +self.change_y)
 
    def on_touch_up(self, touch):
        dx = touch.x - touch.opos[0]
        dy = touch.y - touch.opos[1]

        if dx == 0 and dy == 0:
            self.change_x = 0
            self.change_x = 0
        
        else:
            if abs(dx) > abs(dy):
                if dx > 0:
                    self.change_x = 2
                    self.change_y = 0
                else:
                    self.change_x = -2
                    self.change_y = 0
            else:
                if dy > 0:
                    self.change_y = 2
                    self.change_x = 0
                else:
                    self.change_y = -2
                    self.change_x = 0


    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down =self.on_keyboard_down)

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'a':
            self.change_x = -2
            self.change_y = 0

        elif keycode[1] == 'd':
            self.change_x = 2
            self.change_y = 0

        elif keycode[1] == 'w':
            self.change_x = 0
            self.change_y = 2

        elif keycode[1] == 's':
            self.change_x = 0
            self.change_y = -2

        elif keycode[1] == 'p':
            self.change_x = 0
            self.change_y = 0



### ======= App goes here ======= ###
  
class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main(name = 'Main_Page'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        return(SC)

wt_app().run()