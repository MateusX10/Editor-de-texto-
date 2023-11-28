import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog

class EditorDeTexto:
    '''-> Classe que representa um editor de texto.
    '''


    def __init__(self, janela):
        '''-> Construtor da classe "editorDeTexto"
            Parâmetros:

                janela(tk.Tk): janela do editor de texto
        '''
        self.janela = janela
        self.janela.title("Bloco de notas")

        # o tk.WORD garante que se uma palavra muito longa estiver no finalzinho do comprimento da largura da janela, que ela não seja quebrada ao meio ao pular de linha por ser grande demais, mas sim que se ela for grande demais, que ela como um tudo será jogada para a linha posterior
        # a classe "ScrolledText" do módulo "scrolledtext" cria uma área de texto que permite a rolagem. qdHeight e width são a altura e largura da janela, respectivamente.Undo com valor igual a "True" permite que seja possível desfazer as ações feitas, isto é, permite que usar o "undo".
        self.areaDeTexto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, height=28, width=75, font=("Arial", 12), insertwidth=1, selectbackground="blue",undo=True) 
        
        # empacota a área de texto no bloco de notas.O argumento "expand=True" permite que a área de texto seja expandida, caso necessário.Se a altura de 10 e largura de 40 anteriormente definidos forem ultrapassados, não haverá necessidade de preocupação, visto que ele automaticamente se expandirá conforme o necessário.O argumento "fill=both" permitirá que tanto a horizontal quanto a vertical sejam expandidas e sejam preenchidas.
        self.areaDeTexto.pack(expand=True, fill="both")

        # o caminho do arquivo aberto ou salvo
        self.caminho_do_arquivo_atual = ''

        # cria uma barra de menu onde é instanciado a classe "Menu" onde é associado a nossa janela da aplicação
        menu_bar = tk.Menu(self.janela)

        # configura a janela do bloco de notas como o menu sendo o menu definido acima
        self.janela.config(menu=menu_bar)

        # define um menu arquivo, associando-o a barra de menus.O argumento "tearoff" define se o menu será destacado ou não."0" é para "não destacar", já "1" é para "destacar"
        menu_arquivo = tk.Menu(menu_bar, tearoff=0)

        # cria um item de menu na barra de menus, o apelidando como "arquivo".
        menu_bar.add_cascade(label="arquivo", menu=menu_arquivo)


        # adiciona um item de menu apelidado como "abrir" que realiza a ação de abrir um arquivo já existente.Assim que clicado, o método "abrir_arquivo" é chamado.
        menu_arquivo.add_command(label="abrir", command=self.abrir_arquivo)

        menu_arquivo.add_command(label="salvar", command=self.salvar_arquivo)

        # adiciona um item de menu chamado "salvar como..." que salva um arquivo de texto no computador do usuário.Assim que clicado, o método "salvar_arquivo" é chamado
        menu_arquivo.add_command(label="salvar como...", command=self.salvar_arquivo_como)
        # adiciona um separador (uma linha separadora)
        menu_arquivo.add_separator()
        # adiciona um item de menu apelidado como "sair" na qual, quando pressionado, é executado o comando "janela.destroy" que fecha a janela da aplicação
        menu_arquivo.add_command(label="sair", command=self.janela.destroy)


        # define um menu de "editar" na barra de menu
        menu_edit = tk.Menu(menu_bar, tearoff=0)

        # adiciona o menu definido a barra de menus com a label/nome "editar"
        menu_bar.add_cascade(label="editar", menu=menu_edit)

        # adiciona o item de menu ao menu "editar" chamado "desfazer" que executa o método de desfazer uma operação
        menu_edit.add_command(label="desfazer", command=self.desfazer)

        # adiciona o item  de "refazer" ao menu "editar" que executa o método de refazer uma operação
        menu_edit.add_command(label="refazer", command=self.refazer)

        # adiciona um seperador dentro do menu "editar"
        menu_edit.add_separator()

        # adiciona a opção de "copiar" ao menu "editar", na qual executa o método "copiar()" que copia o texto selecionado
        menu_edit.add_command(label="copiar", command=self.copiar)

        # adiciona a opção de "colar" ao menu de "editar" onde o método "colar" é chamado, na qual o texto da área de tranferência é colado
        menu_edit.add_command(label="colar", command=self.colar)

        # adiciona a opção de recortar ao menu "editar" na qual o método "recortar" é chamado.
        menu_edit.add_command(label="recortar", command=self.recortar)


    def abrir_arquivo(self):
        
        # exibe uma janela de seleção de arquivo onde o usuário poderá selecionar um arquivo de texto a abrir.A função "askopenfilename()" retorna o caminho (path) escolhido  pelo usuário.Por padrão, filtrado arquivos .txt e todos os arquivos.
        caminho_arquivo = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Arquivo de texto", "*.txt"), ("Todos os arquivos", "*.*")])

        # armazena o caminho do arquivo abertp
        self.caminho_do_arquivo_atual = caminho_arquivo

        # Verifica se o usuário escolheu um caminho
        if caminho_arquivo:
            
            # abre o caminho escolhido pelo usuário como leitura para assim visualizarmos o conteúdo do arquivo que queremos visualizar
            with open(caminho_arquivo, "r") as arquivo:

                # pega o arquivo e transforma cada linha do arquivo em um item de lista
                conteudo_arquivo = arquivo.read()

                # limpa a área de texto do início ao fim
                self.areaDeTexto.delete(1.0, tk.END)

                # insere o conteúdo do arquivo aberto na área de texto
                self.areaDeTexto.insert(tk.END, conteudo_arquivo)


    def salvar_arquivo(self):
        '''-> Salva arquivo já existente

            Parâmetros:

                return: sem retorno
        '''

        if self.caminho_do_arquivo_atual:

            caminho_arquivo = self.caminho_do_arquivo_atual

            with open(caminho_arquivo, "w", encoding="utf8") as arquivo:

                conteudo_do_arquivo = self.areaDeTexto.get(1.0, tk.END).encode("utf8")

                arquivo.write(conteudo_do_arquivo)

        else:

            self.salvar_arquivo_como()



    def salvar_arquivo_como(self):
        
        # abre uma janela onde possibilita o usuário escolher onde ele quer salvar  o arquivo de texto.
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")])

        self.caminho_do_arquivo_atual = caminho_arquivo
        
        # verifica se o usuário selecionou um local para salvar o arquivo
        if caminho_arquivo:

            # abre o caminho escolhido em modo de escrita.O parâmetro "encoding" com o valor "utf8" garante que o arquivo seja lido de acordo com a tabela de caracteres utf8
            with open(caminho_arquivo, "w", encoding="utf8") as arquivo:
                
                # obtém o conteúdo contido na área de texto do bloco de notas, do início ao fim
                conteudo = self.areaDeTexto.get(1.0, tk.END).encode("utf8")

                # escreve/coloca no caminho o nome do arquivo
                arquivo.write(conteudo)

    
    def desfazer(self):
        '''-> Desfaz uma ação feita na área de texto do bloco de notas

            Parâmetros:

                return: sem retorno
        '''

        # chama o método "edit_undo()" que desfaz a última operação/ação feita na área de texto
        self.areaDeTexto.edit_undo()


    def refazer(self):

        self.areaDeTexto.edit_redo()

    def copiar(self):
        '''-> Método que copia o texto seleciondo dentro da área de texto do bloco de notas

            Parâmetros:

                return: sem retorno
        '''

        # Chama o método "event_generate()" que gera um evento de cópia.Ao chamar esse método, o tkinter entende que deve copiar o conteúdo atualmente selecionado para a área de tranferência
        self.areaDeTexto.event_generate("<<Copy>>")

    def colar(self):
        '''-> Cola o conteúdo atual da área de tranferência na área de texto do bloco de notas

            Parâmetros:

                return: sem retorno
        '''

        # gera um evento de colagem ao chamar o método "event_generate".Esse método diz ao tkinter que ele deve colar na área de texto do bloco de notas o conteúdo atual da área de transferência
        self.areaDeTexto.event_generate("<<Paste>>")


    def recortar(self):
        '''-> Recorta o conteúdo selecionado, o armanzenando na área de tranferência

            Parâmetros:

                return: sem retorno
        '''                    

        # dispara a ação de recortar o texto selecionado para a área de tranferência
        self.areaDeTexto.event_generate("<<Cut>>")



            
