# Tela Inicial
    # Título: Hashzap
    # Botão: Iniciar Chat
        # quando clicar no botão:
        # abrir um popup/alerta/modal
            # Título: Bem vindo ao hashzap
            # Caixa de texto: Escreva seu nome no chat
            # Botão: Entrar no chat
                # quando clicar no botão
                # sumir com o título
                # sumir com o popup
                # sumir com o botão de iniciar chat
                    # carregar o chat
                    # carregar o campo de enviar mensagem "Digite sua mensagem"
                    # botão enviar
                        # quando clicar no botão enviar
                        # enviar mensagem
                        # limpar a caixa de mensagem

# 3 passos para usar o flet: importar o flet, função principal para o app e executar essa função com flet

import flet as ft

def main(pagina):
    # titulo
    titulo = ft.Text("Hashzap")
    
    def enviar_mensagem(evento):
        texto = ft.Text(campo_enviar_mensagem.value)
        chat.controls.append(texto)
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()

    # function para entrar no chat
    def entrar_chat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)
        pagina.add(chat)
        pagina.add(linha_enviar)
        pagina.update()
        
    # criar popup
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome,actions=[botao_popup])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print("Clicou no botão")

    # botao inicial
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    
    # adicionar elementos na página
    pagina.add(titulo)
    pagina.add(botao)


ft.app(main)