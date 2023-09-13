import tkinter as tk
import automacao

#função que chama a automação
def chamar_automacao():
    automacao.inicia_automacao()


#criando a janela principal
tela_principal = tk.Tk()

#muda o titulo da janela
tela_principal.title("Minha Automação")

#dimensão da area de tela
tela_principal.geometry("300x128")

#criando o primeiro texto da janela
texto_1 = tk.Label(tela_principal, text="Clique em 'Iniciar' para iniciar a Automação")
#definido a poição do texto
texto_1.grid(column=0, row=0, padx=30, pady=20)

#criando o botão da janela
botao_1 = tk.Button(tela_principal, text="Iniciar", command=chamar_automacao)
#definindo posição do botão
botao_1.grid(column=0, row=1, padx=30, pady=15)

#quando exibir a janela deixa ela aberta/ smp é a ultima linha
tela_principal.mainloop()
