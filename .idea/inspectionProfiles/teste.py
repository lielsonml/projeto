import tkinter as tk
import random
import time
import threading
import math

def abrir_calculadora():
    win = tk.Toplevel(janela)
    win.title("Calculadora")
    win.geometry("300x350")

    tk.Label(win, text="Escolha a operação:", font=("Arial", 12)).pack(pady=5)
    operacao = tk.StringVar(value="soma")
    ops = [("Soma", "soma"), ("Subtração", "sub"), ("Multiplicação", "mult"), ("Divisão", "div"), ("Raiz Quadrada", "raiz")]
    for texto, valor in ops:
        tk.Radiobutton(win, text=texto, variable=operacao, value=valor).pack(anchor="w")

    tk.Label(win, text="Primeiro número:").pack()
    num1_entry = tk.Entry(win)
    num1_entry.pack()
    tk.Label(win, text="Segundo número (ou deixe vazio para raiz):").pack()
    num2_entry = tk.Entry(win)
    num2_entry.pack()
    resultado_label = tk.Label(win, text="", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def calcular():
        try:
            op = operacao.get()
            n1 = float(num1_entry.get())
            if op == "raiz":
                resultado = math.sqrt(n1)
                resultado_label.config(text=f"Raiz quadrada: {resultado:.2f}")
                return
            n2 = float(num2_entry.get())
            if op == "soma":
                resultado = n1 + n2
                resultado_label.config(text=f"Soma: {resultado:.2f}")
            elif op == "sub":
                resultado = n1 - n2
                resultado_label.config(text=f"Subtração: {resultado:.2f}")
            elif op == "mult":
                resultado = n1 * n2
                resultado_label.config(text=f"Multiplicação: {resultado:.2f}")
            elif op == "div":
                if n2 == 0:
                    resultado_label.config(text="Erro: divisão por zero")
                else:
                    resultado = n1 / n2
                    resultado_label.config(text=f"Divisão: {resultado:.2f}")
        except ValueError:
            resultado_label.config(text="Digite números válidos!")

    tk.Button(win, text="Calcular", command=calcular).pack(pady=10)

def abrir_imc():
    win = tk.Toplevel(janela)
    win.title("IMC")
    win.geometry("300x250")
    tk.Label(win, text="Peso (kg):").pack()
    peso_entry = tk.Entry(win)
    peso_entry.pack()
    tk.Label(win, text="Altura (m):").pack()
    altura_entry = tk.Entry(win)
    altura_entry.pack()
    resultado_label = tk.Label(win, text="", font=("Arial", 12))
    resultado_label.pack(pady=10)

    def calcular_imc():
        try:
            peso = float(peso_entry.get())
            altura = float(altura_entry.get())
            imc = peso / (altura ** 2)
            if imc < 18.5:
                msg = f"IMC: {imc:.2f} - Abaixo do peso"
            elif imc < 24.9:
                msg = f"IMC: {imc:.2f} - Peso normal"
            else:
                msg = f"IMC: {imc:.2f} - Acima do peso"
            resultado_label.config(text=msg)
        except ValueError:
            resultado_label.config(text="Digite valores válidos!")

    tk.Button(win, text="Calcular IMC", command=calcular_imc).pack(pady=10)

def abrir_tabuada():
    win = tk.Toplevel(janela)
    win.title("Tabuada")
    win.geometry("300x350")
    tk.Label(win, text="Digite um número:").pack()
    num_entry = tk.Entry(win)
    num_entry.pack()
    resultado_text = tk.Text(win, height=12, width=20)
    resultado_text.pack(pady=10)

    def mostrar_tabuada():
        try:
            n = int(num_entry.get())
            resultado_text.delete("1.0", tk.END)
            for i in range(1, 11):
                resultado_text.insert(tk.END, f"{n} x {i} = {n*i}\n")
        except ValueError:
            resultado_text.delete("1.0", tk.END)
            resultado_text.insert(tk.END, "Digite um número inteiro!")

    tk.Button(win, text="Mostrar Tabuada", command=mostrar_tabuada).pack(pady=5)

def abrir_caca_niquel():
    win = tk.Toplevel(janela)
    win.title("Caça-níquel")
    win.geometry("350x250")
    simbolos = ["🍒","🔔","💎","⭐","🍊","🍇"]
    resultado_label = tk.Label(win, text="| ? | ? | ? |", font=("Arial", 32))
    resultado_label.pack(pady=20)
    status_label = tk.Label(win, text="", font=("Arial", 14))
    status_label.pack(pady=10)

    def animar():
        for _ in range(15):
            a, b, c = random.choices(simbolos, k=3)
            resultado_label.config(text=f"| {a} | {b} | {c} |")
            win.update()
            time.sleep(0.12)
        # Resultado final
        if a == b == c:
            status_label.config(text="🏆 Parabéns!! Quanta Sorte!")
        elif a == b or a == c or b == c:
            status_label.config(text="✨ Boa! Dois símbolos iguais!")
        else:
            status_label.config(text="😢 Que pena! Tente novamente")

    def girar():
        status_label.config(text="")
        threading.Thread(target=animar).start()

    tk.Button(win, text="Girar", command=girar, font=("Arial", 14)).pack(pady=10)

# Janela principal
janela = tk.Tk()
janela.title("Projeto Python")
janela.geometry("350x400")

tk.Label(janela, text="Bem-vindo ao nosso projeto! 😃", font=("Arial", 14)).pack(pady=10)
tk.Button(janela, text="Calculadora", width=20, command=abrir_calculadora).pack(pady=5)
tk.Button(janela, text="Calcular IMC", width=20, command=abrir_imc).pack(pady=5)
tk.Button(janela, text="Jogar Caça-níquel", width=20, command=abrir_caca_niquel).pack(pady=5)
tk.Button(janela, text="Tabuada", width=20, command=abrir_tabuada).pack(pady=5)
tk.Button(janela, text="Sair", width=20, command=janela.destroy).pack(pady=20)

janela.mainloop()