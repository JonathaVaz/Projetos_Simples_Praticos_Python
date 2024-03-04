import tkinter as tk 
from tkinter import messagebox

janela = tk.Tk()
janela.title("Lombada Virtual")

tk.Label(janela, text='Velocidade do Carro (km/h)').pack()
velocidade_entry = tk.Entry(janela)
velocidade_entry.pack()

def verificador_de_multa():
    
    try:
        velocidade = float(velocidade_entry.get())
        
        if velocidade > 80:
            excesso = velocidade - 80
            multinha = excesso * 5
            mensagem = f"HAHAHA SE FUDEU!!! KKKKKKKK \n Voce foi multado otário! \n Excesso de velocidade de: {excesso}km/h \n Agora Paga essa Porra. \n Valor da Multa: R${multinha:.2f}"
    
            messagebox.showinfo("Multinha", mensagem)
            
        else:
             messagebox.showinfo("DEU SORTE OTÁRIO", "Sem Multa, por enquanto...")
        
    except ValueError:
       messagebox.showerror("Estúpido!!!", "Pelo Amor, insira uma velocidade válida.")
        

verificador_botao = tk.Button(janela, text="Verificando Possível Multa", command=verificador_de_multa)
verificador_botao.pack()

janela.mainloop()