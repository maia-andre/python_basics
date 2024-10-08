from kivy.app import App
from kivy.uix.button import Button

class Patrimonio(App):
    def build(self):
        return Button(text='Olá Mundo!')
    
Patrimonio().run()
