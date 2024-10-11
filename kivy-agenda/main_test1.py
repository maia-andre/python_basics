from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Patrimonio(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        self.label = Label(text='1', font_size=30)
        button = Button(text='Buscar placa', font_size=30, on_release=self.incrementar)
        box.add_widget(self.label)
        box.add_widget(button)
        return box
    
    def incrementar(self,button):
        button.text = "Soltei"
        self.label.text = str(int(self.label.text)+1)

Patrimonio().run()
