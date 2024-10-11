import os
from tkinter import Tk, messagebox
from tkinter.filedialog import askdirectory
import shutil
import datetime

# Função para criar backup
def criar_backup():
    # Inicializar o tkinter
    root = Tk()
    root.withdraw()  # Oculta a janela principal

    # Janela para selecionar a pasta de origem (onde estão os arquivos)
    pasta_origem = askdirectory(title="Selecione a pasta de origem para backup")
    if not pasta_origem:
        print("Nenhuma pasta de origem selecionada.")
        return

    # Janela para selecionar a pasta de destino (onde o backup será armazenado)
    pasta_destino = askdirectory(title="Selecione a pasta de destino para o backup")
    if not pasta_destino:
        print("Nenhuma pasta de destino selecionada.")
        return

    # Listar arquivos e diretórios na pasta de origem
    lista_arquivos = os.listdir(pasta_origem)

    # Preparar pasta de backup
    nome_pasta_backup = "backup"
    pasta_backup = os.path.join(pasta_destino, nome_pasta_backup)

    if not os.path.exists(pasta_backup):
        os.mkdir(pasta_backup)

    data_atual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pasta_data_backup = os.path.join(pasta_backup, data_atual)

    os.mkdir(pasta_data_backup)

    # Mostrar mensagem de "Backup em andamento"
    messagebox.showinfo("Backup", "Backup em andamento...")

    for item in lista_arquivos:
        caminho_item = os.path.join(pasta_origem, item)
        destino_item = os.path.join(pasta_data_backup, item)

        try:
            if os.path.isfile(caminho_item):
                shutil.copy2(caminho_item, destino_item)
                print(f"Arquivo copiado: {caminho_item} -> {destino_item}")
            elif os.path.isdir(caminho_item) and item != nome_pasta_backup:
                shutil.copytree(caminho_item, destino_item)
                print(f"Pasta copiada: {caminho_item} -> {destino_item}")
        except Exception as e:
            print(f"Erro ao copiar {item}: {e}")

    # Mostrar mensagem de "Backup completo"
    messagebox.showinfo("Backup", "Backup completo!")

# Executar a função de backup
if __name__ == "__main__":
    criar_backup()
