import math
import emoji
import random
import time
import os
import threading
import tkinter as tk
BG_COR = "#222831"
FG_COR = "#FFD369"
BTN_BG = "#393E46"
BTN_FG = "#FFD369"
BTN_ACTIVE_BG = "#FFD369"
BTN_ACTIVE_FG = "#222831"
FONTE_TITULO = ("Arial", 16, "bold")
FONTE_PADRAO = ("Arial", 12) 

def abrir_calculadora():
    principal = tk.Toplevel(janela)
    principal.title =('Calculadora')
    principal.geometry('350x400')
    principal.configure(bg=BG_COR)

    tk.Label(principal,text='Escolha a operação:',font=(FONTE_PADRAO),bg=BG_COR,fg=FG_COR).pack(pady=5)
    valores = tk.StringVar(value='soma')
    ops = [("Soma","soma"),
           ("Subtração","sub"),
           ("Multiplicação","multi"),
           ("Divisão","div")
    ]
    for texto, valor in ops:
        tk.Radiobutton(principal,text=texto,variable=valores,value=valor,font=FONTE_PADRAO,bg=BG_COR,fg=FG_COR,selectcolor=BTN_BG,activebackground=BTN_ACTIVE_BG,activeforeground=BTN_ACTIVE_FG).pack(anchor='w',padx=10)
    tk.Label(principal,text="Primeiro número:",font=FONTE_PADRAO,bg=BG_COR,fg=FG_COR).pack()
    num1_entry = tk.Entry(principal,font=FONTE_PADRAO,bg="#FFF",fg="#000")
    num1_entry.pack(pady=5)
    tk.Label(principal,text="Segundo número:",font=FONTE_PADRAO,bg=BG_COR,fg=FG_COR).pack()
    num2_entry = tk.Entry(principal,font=FONTE_PADRAO,bg="#FFF",fg="#000")
    num2_entry.pack(pady=5)
    resultado_label = tk.Label(principal, text="", font=FONTE_PADRAO,bg=BG_COR,fg=FG_COR)
    resultado_label.pack(pady=10)

    def calcular():
        try:
            op = valores.get()
            n1 = float(num1_entry.get())
            n2 = float(num2_entry.get())
            if op == 'soma':
                resultado = n1 + n2
                resultado_label.config(text=f'soma: {resultado:.2f}')
            elif op == 'sub':
                resultado = n1 - n2
                resultado_label.config(text=f'subtração: {resultado:.2f}')
            elif op == 'multi':
                resultado = n1 * n2
                resultado_label.config(text=f'multiplicação: {resultado:.2f}')
            elif op == 'div':
                resultado = n1 / n2
                resultado_label.config(text=f'divisão: {resultado:.2f}')
        except ValueError:
            resultado_label.config(text='Digite números válidos!')

    tk.Button(principal, text='Calcular', command=calcular,font=FONTE_PADRAO,bg=BTN_BG,fg=BTN_FG,activebackground=BTN_ACTIVE_BG,activeforeground=BTN_ACTIVE_FG,width=15,bd=0,cursor="hand2").pack(pady=10)  

def abrir_imc():
        principal = tk.Toplevel(janela)
        principal.title('IMC')
        principal.geometry('350x400')
        principal.configure(bg=BG_COR)
        tk.Label(principal, text='Peso (kg):',font=FONTE_PADRAO,bg=BG_COR,fg=FG_COR).pack()
        peso_entry = tk.Entry(principal)
        peso_entry.pack()
        tk.Label(principal, text='Altura (m):',font=FONTE_PADRAO,bg=BG_COR,fg=FG_COR).pack()
        altura_entry = tk.Entry(principal)
        altura_entry.pack()
        resultado_label = tk.Label(principal ,text='',font=FONTE_PADRAO,bg=BG_COR,fg=FG_COR)
        resultado_label.pack(pady=10)
        def calcular_imc():
            try:
                peso = float(peso_entry.get())
                altura = float(altura_entry.get())
                imc = peso / (altura **2)
                resultado_label.config(text=f'IMC: {imc:.2f}',)
                if imc < 18.5:
                    resultado_label.config(text='Abaixo do peso')
                elif 18.5 <= imc < 24.9:
                    resultado_label.config(text='Peso normal')
                elif 25 <= imc < 29.9:
                    resultado_label.config(text='Sobrepeso')
                else:
                    resultado_label.config(text='Obesidade')
            except ValueError:
                resultado_label.config(text='Digite números válidos!')
        tk.Button(principal, text='Calcular IMC', command= calcular_imc,font=FONTE_PADRAO,bg=BTN_BG,fg=BTN_FG,activebackground=BTN_ACTIVE_BG,activeforeground=BTN_ACTIVE_FG,cursor="hand2").pack(pady=10) 

def abrir_cacaniquel():
    principal = tk.Toplevel(janela)
    principal.title('Caça-níquel')
    principal.geometry('350x400')
    principal.configure(bg=BG_COR)
    simbolos = ["🍒","🔔","💎","⭐","🍊","🍇"]
    resultado_label = tk.Label(principal, text='| ? | ? | ? |', font=('arial', 38,'bold'),bg=BG_COR,fg=FG_COR)
    resultado_label.pack(pady=30)
    status_label = tk.Label(principal, text='', font=('arial',16,'bold'), bg=BG_COR, fg=FG_COR)
    status_label.pack(pady=10)
        
    def animar():
        for _ in range(15):
            a, b, c = random.choices(simbolos, k=3)
            resultado_label.config(text=f'| {a} | {b} | {c} |')
            principal.update()
            time.sleep(0.2)
        if a == b == c:
            status_label.config(text="🏆 Parábens!! Quanta Sorte!")
        elif a == b or a == c or b == c:
            status_label.config(text="✨ boa! Dois símbolos iguais!")
        else:
            status_label.config(text="😢 que pena! Tente novamente")
    def girar():
        status_label.config(text='',fg=FG_COR)
        threading.Thread(target=animar).start()

    tk.Button(principal, text='Girar', command=girar, font=FONTE_PADRAO,bg=BTN_BG,fg=BTN_FG,activebackground=BTN_ACTIVE_BG,activeforeground=BTN_ACTIVE_FG,cursor='hand2').pack(pady=20)
janela = tk.Tk()
janela.title('Menu Principal')
janela.geometry('350x400')
janela.configure(bg=BG_COR)


tk.Label(janela, text='Bem-vindo ao Menu Principal', font=FONTE_TITULO, bg=BG_COR,fg=FG_COR).pack(pady=10)
tk.Button(janela, text='Calculadora', width=20, command=abrir_calculadora, font=FONTE_TITULO,bg=BG_COR,fg=FG_COR).pack(pady=10)
tk.Button(janela,text='IMC', width=20, command=abrir_imc,font=FONTE_TITULO,bg=BG_COR,fg=FG_COR).pack(pady=5)
tk.Button(janela, text='Caça-níquel', width=20, command=abrir_cacaniquel,font=FONTE_TITULO,bg=BG_COR,fg=FG_COR).pack(pady=5)
tk.Button(janela, text='Sair', width=20 , command=janela.quit,bg=BG_COR,fg=FG_COR).pack(pady=20)
janela.mainloop()