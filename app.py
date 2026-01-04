import csv
import matplotlib.pyplot as plt # ### NOVO: Importando a ferramenta de gráficos

transacoes = []

try:
    with open('financeiro.csv', mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            linha['Valor'] = float(linha['Valor'])
            transacoes.append(linha)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
    exit()

total_entradas = 0
total_saidas = 0
gastos_por_categoria = {}

print("-" * 30)
print("EXTRATO DETALHADO")
print("-" * 30)

for item in transacoes:
    valor = item['Valor']
    descricao = item['Descricao']
    tipo = item['Tipo']
    categoria = item['Categoria']

    if tipo == 'Entrada':
        total_entradas += valor
        print(f"[+] {descricao}: R$ {valor:.2f}")

    elif tipo == 'Saida':
        total_saidas += valor
        print(f"[-] {descricao}: R$ {valor:.2f}")

        if categoria in gastos_por_categoria:
            gastos_por_categoria[categoria] += valor
        else:
            gastos_por_categoria[categoria] = valor

saldo_final = total_entradas - total_saidas

# ### NOVO: Criando o Gráfico
# O Matplotlib precisa de duas listas: uma com os nomes e outra com os valores
categorias = list(gastos_por_categoria.keys())
valores = list(gastos_por_categoria.values())

print("\n📊 Gerando gráfico...")

# Criando o gráfico de pizza
plt.figure(figsize=(6, 6)) # Tamanho da figura
plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição dos Meus Gastos')

# Exibindo na tela
plt.show()