import flet as ft

def main(pagina):

# título + botão pequeno de admin no canto direito
    # "Secretaria da Educação - Agenda do Transporte"
    titulo = ft.Text("Secretaria da Educação - Agenda do Transporte", size=30)
    pagina.add(titulo)
    
 # Criar solicitação
    # definindo os itens do popup de solicitação
    titulo_popup = ft.Text("Solicite sua viagem!")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    caixa_data = ft.TextField(label="Digite o seu nome")
    caixa_origem = ft.TextField(label="Digite o seu nome")
    caixa_destino = ft.TextField(label="Digite o seu nome")
    caixa_saida = ft.TextField(label="Digite o seu nome")
    caixa_retorno = ft.TextField(label="Digite o seu nome")
    caixa_qtde = ft.TextField(label="Digite o seu nome")
    caixa_obs = ft.TextField(label="Digite o seu nome")
    botao_solicitar = ft.ElevatedButton("Solicitar viagem!")

    # criando o popup
    popup = ft.AlertDialog(
        title=titulo_popup,
        content=ft.Column([
            caixa_nome,
            caixa_data,
            caixa_origem,
            caixa_destino,
            caixa_saida,
            caixa_retorno,
            caixa_qtde,
            caixa_obs
        ]),
        actions=[botao_solicitar]
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print("Clicou no botão")

# 2 botões na mesma linha 
    botao_criar = ft.ElevatedButton("Criar Solicitação", on_click=abrir_popup)
    botao_admin = ft.ElevatedButton("Modo Administrador")
    linha_botoes = ft.Row([botao_criar,botao_admin])
    pagina.add(linha_botoes)
    

        # botão confirmar
            # insere as 8 informações na tabela
 # Botão Admin 
    # irá abrir um modal que irá solicitar um código
    # a inserção do código irá permitir o admin alterar ou excluir viagens na última coluna
    
#tabela - cabeçalho com 11 colunas
 # status
 # motorista
 # veículo
 # solicitante
 # data da viagem
 # origem
 # destino
 # hora de saída
 # retorno previsto
 # quantidade de passageiros
 # observações
 # 2 ícones - alterar e excluir
    # os ícones vão ser "clicáveis" apenas para o administrador

    

ft.app(main)