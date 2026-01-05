import csv
import matplotlib.pyplot as plt

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

for item in transacoes:
    valor = item['Valor']
    tipo = item['Tipo']
    categoria = item['Categoria']

    if tipo == 'Entrada':
        total_entradas += valor
    elif tipo == 'Saida':
        total_saidas += valor
        # Lógica de acumular gastos por categoria
        if categoria in gastos_por_categoria:
            gastos_por_categoria[categoria] += valor
        else:
            gastos_por_categoria[categoria] = valor

saldo_final = total_entradas - total_saidas

# --- AQUI COMEÇA A MÁGICA VISUAL ---
# Criando uma figura com 2 gráficos (subplots) lado a lado (1 linha, 2 colunas)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# GRÁFICO 1: Pizza (Gastos por Categoria)
categorias = list(gastos_por_categoria.keys())
valores = list(gastos_por_categoria.values())

ax1.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=90)
ax1.set_title('Onde estou gastando?')

# GRÁFICO 2: Barras (Entradas vs Saídas)
resumo = ['Entradas', 'Saídas']
valores_resumo = [total_entradas, total_saidas]
cores = ['green', 'red'] # Verde para dinheiro entrando, Vermelho para saindo

barras = ax2.bar(resumo, valores_resumo, color=cores)
ax2.set_title('Balanço do Mês')

# Adicionando o valor em cima da barra para facilitar a leitura
ax2.bar_label(barras, fmt='R$ %.2f')

# Ajuste final para não ficar tudo apertado
plt.tight_layout()

print(f"✅ Dashboard Gerado! Saldo Final: R$ {saldo_final:.2f}")
plt.show()