from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Patrimonio(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        label = Label(text='Patrimônio')
        button = Button(text='Buscar placa')
        box.add_widget(label)
        box.add_widget(button)
        return box
        
Patrimonio().run()
