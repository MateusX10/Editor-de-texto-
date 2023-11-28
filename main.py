# importa o módulo tkinter, o apelidando como "tk" para facilitar o uso
import tkinter as tk
from editor import *

# verifica se o usuário está executando  o meu programa a partir do arquivo principal
if __name__ == "__main__":
    # define a janela de interface
    janela = tk.Tk()

    # cria uma instância da classe "editorDeTexto", passando a janela como argumento
    editor_de_texto = EditorDeTexto(janela)

    # executa a aplicação
    janela.mainloop()
