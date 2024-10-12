from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados
Base = declarative_base()
engine = create_engine('sqlite:///solicitacoes.db')
Session = sessionmaker(bind=engine)

# Modelo para a tabela de solicitações
class Solicitation(Base):
    __tablename__ = 'solicitations'
    id = Column(Integer, primary_key=True)
    matricula = Column(String)
    nome_solicitante = Column(String)
    data_viagem = Column(String)
    origem = Column(String)
    destino = Column(String)
    hora_saida = Column(String)
    previsao_retorno = Column(String)
    quantidade_passageiros = Column(Integer)
    observacoes = Column(String)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

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
        session = Session()
        viagem = {field: input_field.text for field, input_field in self.inputs.items()}
        matricula = self.manager.matricula
        
        # Criação da solicitação e adição ao banco de dados
        nova_solicitacao = Solicitation(
            matricula=matricula,
            nome_solicitante=viagem['Nome do solicitante'],
            data_viagem=viagem['Data da viagem'],
            origem=viagem['Origem'],
            destino=viagem['Destino'],
            hora_saida=viagem['Hora de saída'],
            previsao_retorno=viagem['Previsão de retorno'],
            quantidade_passageiros=int(viagem['Quantidade de passageiros']),
            observacoes=viagem['Observações (opcional)']
        )
        
        session.add(nova_solicitacao)
        session.commit()
        session.close()
        
        print(f"Solicitação adicionada ao banco de dados: {viagem}")

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
        session = Session()
        matricula = self.manager.matricula
        solicitacoes = session.query(Solicitation).filter_by(matricula=matricula).all()
        session.close()
        
        # Limpa os pedidos anteriores ao entrar na tela
        self.content.clear_widgets()
        self.content.add_widget(self.label)

        if solicitacoes:
            for s in solicitacoes:
                pedido_label = Label(
                    text=f"Solicitação {s.id}:\n"
                          f"Nome: {s.nome_solicitante}\n"
                          f"Data: {s.data_viagem}\n"
                          f"Origem: {s.origem}\n"
                          f"Destino: {s.destino}\n"
                          f"Hora de saída: {s.hora_saida}\n"
                          f"Previsão de retorno: {s.previsao_retorno}\n"
                          f"Quantidade de passageiros: {s.quantidade_passageiros}\n"
                          f"Observações: {s.observacoes}\n"
                          f"-----------------------------------",
                    size_hint_y=None,
                    height=200,
                    halign='left',
                    valign='top'
                )
                pedido_label.bind(size=pedido_label.setter('text_size'))
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
