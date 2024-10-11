from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

# Classe para a tela de boas-vindas
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.matricula_input = TextInput(hint_text='Digite sua matrícula', multiline=False)
        button = Button(text='Entrar')
        button.bind(on_press=self.go_to_home)
        layout.add_widget(Label(text='Bem-vindo ao App!'))
        layout.add_widget(self.matricula_input)
        layout.add_widget(button)
        self.add_widget(layout)

    def go_to_home(self, instance):
        matricula = self.matricula_input.text
        if matricula:
            self.manager.current = 'home'
            self.manager.matricula = matricula

# Classe para a página inicial
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Agenda do Transporte'))
        agendar_btn = Button(text='Agendar Veículo')
        consultar_btn = Button(text='Consultar Meus Pedidos')
        agendar_btn.bind(on_press=self.go_to_agendar)
        consultar_btn.bind(on_press=self.go_to_consultar)
        layout.add_widget(agendar_btn)
        layout.add_widget(consultar_btn)
        self.add_widget(layout)

    def go_to_agendar(self, instance):
        self.manager.current = 'agendar'

    def go_to_consultar(self, instance):
        self.manager.current = 'consultar'

# Classe para agendar veículo
class AgendarScreen(Screen):
    solicitacoes = []  # Lista para armazenar as solicitações
    contador = 1  # Contador para o número da solicitação

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.inputs = {}
        fields = ['Nome do solicitante', 'Data da viagem', 'Origem', 'Destino', 'Hora de saída',
                  'Previsão de retorno', 'Quantidade de passageiros', 'Observações (opcional)']

        for field in fields:
            input_field = TextInput(hint_text=field, multiline=False)
            layout.add_widget(input_field)
            self.inputs[field] = input_field

        button = Button(text='Solicitar')
        button.bind(on_press=self.solicitar)
        layout.add_widget(button)
        self.add_widget(layout)

    def solicitar(self, instance):
        viagem = {field: input_field.text for field, input_field in self.inputs.items()}
        matricula = self.manager.matricula
        viagem['matricula'] = matricula
        viagem['numero_solicitacao'] = AgendarScreen.contador
        
        print(f"Solicitação {AgendarScreen.contador}: {viagem}")  # Imprime a solicitação no console
        AgendarScreen.solicitacoes.append(viagem)  # Armazena a solicitação
        AgendarScreen.contador += 1  # Incrementa o contador

        # Limpa os campos após a solicitação
        for input_field in self.inputs.values():
            input_field.text = ''

        self.manager.current = 'home'

# Classe para consultar pedidos
class ConsultarScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Criação do ScrollView
        self.scroll_view = ScrollView()
        self.content = BoxLayout(orientation='vertical', size_hint_y=None)
        self.content.bind(minimum_height=self.content.setter('height'))

        self.label = Label(text='Seus Pedidos:', size_hint_y=None, height=40)  # Altura fixa para o label
        self.content.add_widget(self.label)
        self.scroll_view.add_widget(self.content)

        button = Button(text='Voltar', size_hint_y=None, height=50)
        button.bind(on_press=self.go_to_home)
        
        layout.add_widget(self.scroll_view)
        layout.add_widget(button)
        self.add_widget(layout)

    def on_enter(self):
        matricula = self.manager.matricula
        solicitacoes = [s for s in AgendarScreen.solicitacoes if s['matricula'] == matricula]
        
        # Limpa os pedidos anteriores ao entrar na tela
        self.content.clear_widgets()
        self.content.add_widget(self.label)  # Adiciona o label de volta

        if solicitacoes:
            for s in solicitacoes:
                pedido_label = Label(
                    text=f"Solicitação {s['numero_solicitacao']}:\n"
                          f"Nome: {s['Nome do solicitante']}\n"
                          f"Data: {s['Data da viagem']}\n"
                          f"Origem: {s['Origem']}\n"
                          f"Destino: {s['Destino']}\n"
                          f"Hora de saída: {s['Hora de saída']}\n"
                          f"Previsão de retorno: {s['Previsão de retorno']}\n"
                          f"Quantidade de passageiros: {s['Quantidade de passageiros']}\n"
                          f"Observações: {s['Observações (opcional)']}\n"
                          f"-----------------------------------",
                    size_hint_y=None,
                    height=200,
                    halign='left',  # Alinhamento à esquerda
                    valign='top'  # Alinhamento vertical no topo
                )
                pedido_label.bind(size=pedido_label.setter('text_size'))  # Permite quebra de linha
                self.content.add_widget(pedido_label)
        else:
            self.content.add_widget(Label(text=f'Sem pedidos para matrícula {matricula}.', size_hint_y=None, height=40))

    def go_to_home(self, instance):
        self.manager.current = 'home'

# Gerenciador de telas
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AgendarScreen(name='agendar'))
        sm.add_widget(ConsultarScreen(name='consultar'))
        sm.matricula = ''
        return sm

if __name__ == '__main__':
    MyApp().run()
