import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#config do banco
connection =sqlite3.connect('carros.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS carros(
                  Chassi INTEGER PRIMARY KEY AUTOINCREMENT,
                  Nome_do_Proprietario TEXT NOT NULL,
                  CPF_do_Proprietario INTEGER NOT NULL,
                  Placa TEXT NOT NULL,
                  UF TEXT NOT NULL,
                  Cidade TEXT NOT NULL,
                  Marca TEXT NOT NULL,
                  Ano_de_Fabricacao INTEGER NOT NULL,
                  Cor TEXT NOT NULL,
                  Portas INTEGER NOT NULL,
                  Mala TEXT NOT NULL,
                  capacidade_da_Mala INTEGER NOT NULL,
                  ArCondicionado BOOLEAN NOT NULL,
                  Radio BOOLEAN NOT NULL,
                  Airbag BOOLEAN NOT NULL,
                  Defeitos TEXT NOT NULL)''')

connection.commit()
print("tabela criada")

#CRUD
#insert
def insert():
    Chassi = entry_chassi.get()
    Nome_do_proprietario = entry_nome.get()
    CPF_do_proprietario = entry_cpf.get()
    Placa = entry_placa.get()
    UF = combobox_uf.get()
    Cidade = entry_cidade.get()
    Marca = combobox_marca.get()
    Ano_de_fabricacao = combobox_ano.get()
    Cor = combobox_cor.get()
    Portas = qntportas_var.get()
    Mala = mala_var.get()
    capacidade_da_mala = scale_peso.get()
    ArCondicionado = checkbox_ar_var.get()
    Radio = checkbox_radio_var.get()
    Airbag = checkbox_airbag_var.get()
    Defeitos = entry_cidade.get()

    connection.execute("INSERT INTO carros (Chassi, Nome_do_proprietario, CPF_do_proprietario, Placa, UF, Cidade, Marca, Ano_de_fabricacao, Cor, Portas, Mala, capacidade_da_mala, ArCondicionado, Radio, Airbag, Defeitos) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", 
                      (Chassi, Nome_do_proprietario, CPF_do_proprietario, Placa, UF, Cidade, Marca, Ano_de_fabricacao, Cor, Portas, Mala, capacidade_da_mala, ArCondicionado, Radio, Airbag, Defeitos))
    connection.commit()
    messagebox.showinfo("Sucesso", "carro inserido com sucesso!")

#delete
def delete():
    try:
        Chassi = int(entry_chassi.get())
        connection.execute("DELETE FROM carros WHERE Chassi=?", (Chassi,))
        connection.commit()
        messagebox.showinfo("Sucesso", "carro deletado com sucesso!")
    except ValueError:
        messagebox.showwarning("Atenção", "Número de chassi inválido!")

#update
def update():
    try:
        Chassi = int(entry_chassi.get())
        Nome_do_proprietario = entry_nome.get()
        CPF_do_proprietario = entry_cpf.get()
        Placa = entry_placa.get()
        UF = combobox_uf.get()
        Cidade = entry_cidade.get()
        Marca = combobox_marca.get()
        Ano_de_fabricacao = combobox_ano.get()
        Cor = combobox_cor.get()
        Portas = qntportas_var.get()
        Mala = mala_var.get()
        capacidade_da_mala = scale_peso.get()
        ArCondicionado = checkbox_ar_var.get()
        Radio = checkbox_radio_var.get()
        Airbag = checkbox_airbag_var.get()
        Defeitos = entry_cidade.get()

        if Nome_do_proprietario and CPF_do_proprietario and Placa and UF and Cidade and Marca and Ano_de_fabricacao and Cor and Portas and Mala and capacidade_da_mala and Defeitos:
            cursor.execute('''UPDATE carros SET Nome_do_proprietario=?, CPF_do_proprietario=?, Placa=?, UF=?, Cidade=?, Marca=?, Ano_de_fabricacao=?, Cor=?, Portas=?, Mala=?, capacidade_da_mala=?, ArCondicionado=?, Radio=?, Airbag=?, Defeitos=?
                WHERE Chassi=?''',
                (Nome_do_proprietario, CPF_do_proprietario, Placa, UF, Cidade, Marca, Ano_de_fabricacao, Cor, Portas, Mala, capacidade_da_mala, ArCondicionado, Radio, Airbag, Defeitos, Chassi))
            connection.commit()
            messagebox.showinfo("Sucesso", "Cadastro atualizado com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
    except ValueError:
        messagebox.showwarning("Atenção", "chassi inválido!")

#Select
def select():
    listar_janela = tk.Toplevel(root)
    listar_janela.title("Listagem dos carros")

    listbox = tk.Listbox(listar_janela, width=320)
    listbox.pack()

    cursor.execute("SELECT * FROM carros")
    registros = cursor.fetchall()
    for registro in registros:
        listbox.insert(tk.END, f"Chassi: {registro[0]} - Nome do Proprietário: {registro[1]} - CPF: {registro[2]} - "
                               f"Placa: {registro[3]} - UF: {registro[4]} - Cidade: {registro[5]} - "
                               f"Marca: {registro[6]} - Ano: {registro[7]} - Cor: {registro[8]} - "
                               f"Portas: {registro[9]} - Mala: {'Sim' if registro[10] == 'Sim' else 'Não'} - "
                               f"Capacidade da Mala: {registro[11]}L - "
                               f"Ar-condicionado: {'Sim' if registro[12] else 'Não'} - "
                               f"Radio: {'Sim' if registro[13] else 'Não'} - "
                               f"Airbag: {'Sim' if registro[14] else 'Não'} - "
                               f"Problemas: {registro[15]}")

def selectchassi():
    try:
        Chassi = int(entry_chassi.get())
        listar_janela = tk.Toplevel(root)
        listar_janela.title("Carro")

        listbox = tk.Listbox(listar_janela, width=320)
        listbox.pack()

        cursor.execute("SELECT * FROM carros WHERE Chassi=?", (Chassi,))
        registro = cursor.fetchone()
        if registro:
            listbox.insert(tk.END, f"Chassi: {registro[0]} - Nome do Proprietário: {registro[1]} - CPF: {registro[2]} - "
                                   f"Placa: {registro[3]} - UF: {registro[4]} - Cidade: {registro[5]} - "
                                   f"Marca: {registro[6]} - Ano: {registro[7]} - Cor: {registro[8]} - "
                                   f"Portas: {registro[9]} - Mala: {'Sim' if registro[10] == 'Sim' else 'Não'} - "
                                   f"Capacidade da Mala: {registro[11]}L - "
                                   f"Ar-condicionado: {'Sim' if registro[12] else 'Não'} - "
                                   f"Radio: {'Sim' if registro[13] else 'Não'} - "
                                   f"Airbag: {'Sim' if registro[14] else 'Não'} - "
                                   f"Problemas: {registro[15]}")
        else:
            messagebox.showinfo("Informação", "Carro não encontrado!")
    except ValueError:
        messagebox.showwarning("Atenção", "Número de chassi inválido!")
        
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
tk.Label(root, text="CPF do proprietário").grid(row=4, column=0)
entry_cpf = tk.Entry(root)
entry_cpf.grid(row=5, column=0)

#Placa
tk.Label(root, text="Placa").grid(row=6, column=0)
entry_placa = tk.Entry(root)
entry_placa.grid(row=7, column=0)

#UF
tk.Label(root, text="UF:").grid(row=8, column=0)
combobox_uf = ttk.Combobox(root)
combobox_uf['values'] = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS",
    "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC",
    "SE", "SP", "TO"]
combobox_uf.grid(row=9, column=0)

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
combobox_ano['values'] = [str(year) for year in range(1980, 2025)]
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
mala_var = tk.StringVar()
radio_sim = tk.Radiobutton(root, text="Sim", variable=mala_var, value="Sim")
radio_nao = tk.Radiobutton(root, text="Não", variable=mala_var, value="Não")
radio_sim.grid(row=21, column=0, sticky='w')
radio_nao.grid(row=21, column=1, sticky='w')

#Slider capacidade da mala
tk.Label(root, text="Capacidade da mala(L):").grid(row=22, column=0)
scale_peso = tk.Scale(root, from_=0, to=600, orient=tk.HORIZONTAL,sliderlength=10, sliderrelief='raised')
scale_peso.grid(row=22, column=1)

#Recursos do carro
tk.Label(root, text="O carro possui:").grid(row=23, column=0)

#Ar-condiconado
checkbox_ar_var = tk.BooleanVar()
checkbox_ar = tk.Checkbutton(root, text="Ar-condicionado", variable=checkbox_ar_var)
checkbox_ar.grid(row=24, column=0, sticky='w')

#Radio
checkbox_radio_var = tk.BooleanVar()
checkbox_radio = tk.Checkbutton(root, text="Radio", variable=checkbox_radio_var)
checkbox_radio.grid(row=25, column=0, sticky='w')

#Airbag
checkbox_airbag_var = tk.BooleanVar()
checkbox_airbag = tk.Checkbutton(root, text="Airbag", variable=checkbox_airbag_var)
checkbox_airbag.grid(row=26, column=0, sticky='w')

#Defeitos
tk.Label(root, text="Problemas no carro:").grid(row=27, column=0)
entry_cidade = tk.Entry(root)
entry_cidade.grid(row=27, column=1)

#--------------------------------------------------------------------------------
#buttons
tk.Button(root, text="Confirmar cadastro", command=insert).grid(row=30, column=0)
tk.Button(root, text="Excluir cadastro", command=delete).grid(row=30, column=1)
tk.Button(root, text="Atualizar cadastro", command=update).grid(row=30, column=2)
tk.Button(root, text="Carros cadastrados", command=select).grid(row=30, column=3)
tk.Button(root, text="Procurar pelo chassi", command=selectchassi).grid(row=30, column=4)

root.mainloop()


