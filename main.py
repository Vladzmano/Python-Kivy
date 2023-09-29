from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

### ======= App goes here ======= ###

        self.ecuation = ''

        with self.canvas:
            Color(0.6, 0.6, 0.6, 0.9)
            self.rect = Rectangle(size = (self.size[0], 0.15*self.size[1]), pos = (0, 0.85*self.height))

        self.show = MDLabel(text = 'Math Expression', bold = True, halign = 'center', pos_hint = {'center_y' : 0.925})
        self.add_widget(self.show)

        self.buttons = GridLayout(cols = 4, size_hint = (1, 0.7), spacing = 5, padding =10, pos_hint = {'center_x' : 0.5, 'top' : 0.82})
       
        self.buttons.add_widget(Button(text = '7', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('7')))
        self.buttons.add_widget(Button(text = '8', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('8')))
        self.buttons.add_widget(Button(text = '9', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('9')))
        self.buttons.add_widget(Button(text = '+', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('+')))
        self.buttons.add_widget(Button(text = '4', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('4')))
        self.buttons.add_widget(Button(text = '5', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('5')))
        self.buttons.add_widget(Button(text = '6', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('6')))
        self.buttons.add_widget(Button(text = '-', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('-')))
        self.buttons.add_widget(Button(text = '1', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('1')))
        self.buttons.add_widget(Button(text = '2', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('2')))
        self.buttons.add_widget(Button(text = '3', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('3')))
        self.buttons.add_widget(Button(text = '*', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('*')))
        self.buttons.add_widget(Button(text = '.', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('.')))
        self.buttons.add_widget(Button(text = '0', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('0')))
        self.buttons.add_widget(Button(text = '=', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.results()))
        self.buttons.add_widget(Button(text = '/', bold = True, size_hint = (0.25, 0.18), background_color = 'lightblue', on_press = lambda x: self.press('/')))

        self.add_widget(self.buttons)

        self.add_widget(Button(text = 'Delete', 
                               bold = True, 
                               size_hint = (0.25, 0.12), 
                               background_color = 'red', 
                               on_press = lambda x: self.delete(), 
                               pos_hint = {'center_x' : 0.5}))


    def on_size(self, *args):
        self.rect.size = (self.size[0], 0.15*self.size[1])
        self.rect.pos = (0, 0.85*self.height)

    def press(self, value):
        self.ecuation = self.ecuation + value
        self.show.text = self.ecuation

    def results(self):
        try:
            self.ecuation = str(eval(self.ecuation))
            self.show.text = self.ecuation
        
        except:
            self.ecuation = ''
            self.show.text = 'Error'

    def delete(self):
        self.ecuation = ''
        self.show.text = self.ecuation


### ======= App goes here ======= ###
  
class wt_app(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(main(name = 'main'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'

        return(SC)

wt_app().run()