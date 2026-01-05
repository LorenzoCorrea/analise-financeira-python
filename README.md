# 📊 Dashboard Financeiro - Lorenzo Corrêa

> Uma solução de **Data Analysis** automatizada para substituir planilhas manuais e gerar insights financeiros visuais.

## 📸 Preview
![Dashboard Preview](dashboard_preview.png)
*(Certifique-se de salvar um print do gráfico gerado na pasta do projeto com o nome dashboard_preview.png para ele aparecer aqui)*

---

## 🚀 Sobre o Projeto

Este projeto marca minha transição prática para a área de **Dados e Backend**. O objetivo foi desenvolver um script em Python que atua como um motor de ETL (Extract, Transform, Load) para finanças pessoais.

Diferente de uma planilha estática, este software:
* **Lê** dados brutos de extratos bancários (CSV).
* **Processa** e tipa as informações automaticamente.
* **Agrega** valores por categorias dinâmicas.
* **Renderiza** um dashboard executivo para tomada de decisão.

## 🛠 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Data_Viz-11557c?style=for-the-badge)
![CSV](https://img.shields.io/badge/CSV-Data_Handling-239120?style=for-the-badge)
![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)

## 📂 Estrutura do Projeto

A arquitetura foi pensada para ser simples e modular:

* `app.py`: Script principal contendo a lógica de processamento e visualização.
* `financeiro.csv`: Base de dados (simulando um export bancário).
* `ETL Logic`: O código converte strings para floats e agrupa dicionários para análise.

## 🏃‍♂️ Como Rodar Localmente

Siga os passos abaixo para executar o dashboard na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/LorenzoCorrea/analise-financeira-python.git](https://github.com/LorenzoCorrea/analise-financeira-python.git)