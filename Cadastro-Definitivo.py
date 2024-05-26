import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#abertura dejanela do tk
root = tk.Tk()
root.title("Cadastro de carro")

#Parte de preenchimento
#Chassi
tk.Label(root, text="Número de chassi:").grid(row=0, column=0)
entry_chassi = tk.Entry(root)
entry_chassi.grid(row=1, column=0)

#Nome do proprietário
tk.Label(root, text="Nome do proprietário").grid(row=2, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=3, column=0)

#CPF do proprietário
tk.Label(root, text="Nome do proprietário").grid(row=4, column=0)
entry_cpf = tk.Entry(root)
entry_cpf.grid(row=5, column=0)

#Placa
tk.Label(root, text="Placa").grid(row=6, column=0)
entry_placa = tk.Entry(root)
entry_placa.grid(row=7, column=0)

#UF
tk.Label(root, text="UF:").grid(row=8, column=0)
combobox_ano = ttk.Combobox(root)
combobox_ano['values'] = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS",
    "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC",
    "SE", "SP", "TO"]
combobox_ano.grid(row=9, column=0)

#Cidade
tk.Label(root, text="Cidade:").grid(row=10, column=0)
entry_cidade = tk.Entry(root)
entry_cidade.grid(row=11, column=0)

#Marca
tk.Label(root, text="Marca:").grid(row=12, column=0)
combobox_marca = ttk.Combobox(root)
combobox_marca['values'] = ["Chevrolet", "Fiat", "Ford", "Honda", "Hyundai", "Jeep",
    "Nissan", "Peugeot", "Renault", "Toyota", "Volkswagen"]
combobox_marca.grid(row=13, column=0)

#Ano de fabricação
tk.Label(root, text="Ano de fabricação:").grid(row=14, column=0)
combobox_ano = ttk.Combobox(root)
combobox_ano['values'] = [str(year) for year in range(1900, 2025)]
combobox_ano.grid(row=15, column=0)

#Cor
tk.Label(root, text="Cor:").grid(row=16, column=0)
combobox_cor = ttk.Combobox(root)
combobox_cor['values'] = ["Branco", "Cinza", "Prata", "Preto", "Vermelho", "Azul",
    "Marrom", "Verde", "Amarelo", "Laranja", "Roxo"]
combobox_cor.grid(row=17, column=0)

#Portas
tk.Label(root, text="Quantidade de portas:").grid(row=18, column=0)
qntportas_var = tk.StringVar()
radio_2portas = tk.Radiobutton(root, text="2 portas", variable=qntportas_var, value="2")
radio_4portas = tk.Radiobutton(root, text="4 portas", variable=qntportas_var, value="4")
radio_2portas.grid(row=19, column=0, sticky='w')
radio_4portas.grid(row=19, column=1, sticky='w')

#Mala
tk.Label(root, text="Possui mala:").grid(row=20, column=0)
qntportas_var = tk.StringVar()
radio_sim = tk.Radiobutton(root, text="Sim", variable=qntportas_var, value="Sim")
radio_nao = tk.Radiobutton(root, text="Não", variable=qntportas_var, value="Não")
radio_sim.grid(row=21, column=0, sticky='w')
radio_nao.grid(row=21, column=1, sticky='w')

#Recursos do carro
tk.Label(root, text="O carro possui:").grid(row=22, column=0)

#Ar-condiconado
checkbox_ar_var = tk.BooleanVar()
checkbox_ar = tk.Checkbutton(root, text="Ar-condicionado", variable=checkbox_ar_var)
checkbox_ar.grid(row=23, column=0, sticky='w')

#Radio
checkbox_radio_var = tk.BooleanVar()
checkbox_radio = tk.Checkbutton(root, text="Radio", variable=checkbox_radio_var)
checkbox_radio.grid(row=24, column=0, sticky='w')

#Airbag
checkbox_airbag_var = tk.BooleanVar()
checkbox_airbag = tk.Checkbutton(root, text="Airbag", variable=checkbox_airbag_var)
checkbox_airbag.grid(row=25, column=0, sticky='w')

#Defeitos
tk.Label(root, text="Problemas no carro:").grid(row=26, column=0)
entry_cidade = tk.Entry(root)
entry_cidade.grid(row=26, column=1)

#--------------------------------------------------------------------------------
#buttons
tk.Button(root, text="Confirmar cadastro").grid(row=30, column=0)
tk.Button(root, text="Excluir cadastro").grid(row=30, column=1)
tk.Button(root, text="Atualizar cadastro").grid(row=30, column=2)
tk.Button(root, text="Carros cadastrados").grid(row=30, column=3)

root.mainloop()



