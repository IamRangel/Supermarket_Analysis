📌 **Objetivo do Projeto**

Este projeto foi desenvolvido para transformar um dataset de vendas de supermercado em **insights reais para o negócio**, passando por todo o fluxo de análise de dados:

Limpeza e padronização do dataset (ETL)
Criação de métricas e agregações
Análise exploratória dos dados
Construção de dashboards no Power BI
Preparação final para portfólio (GitHub + LinkedIn)

🧹 **ETL — Limpeza e Processamento dos Dados**

Criei um script em Python responsável por:

Ler o arquivo original com segurança
Padronizar valores numéricos e corrigir formatações inconsistentes
Tratar datas e gerar a coluna de mês
Garantir a integridade dos valores de vendas e impostos
Exportar arquivos organizados para facilitar a análise no Power BI

**Arquivos gerados no processo:**

supermarket_clean.csv
vendas_mes.csv
vendas_categoria.csv
vendas_branch.csv
vendas_payment.csv
ticket_medio.csv

📊 **Dashboards no Power BI**

Com os dados tratados, construí um dashboard que apresenta os principais indicadores do negócio, como:

Evolução mensal das vendas
Vendas por categoria de produto
Comparação entre filiais
Participação dos métodos de pagamento
Total de vendas e outros KPIs essenciais

O arquivo .pbix está disponível no repositório.

🛠 **Tecnologias Utilizadas**

Python 3.10+
Pandas
OS (manipulação de diretórios)
Power BI
GitHub Desktop

▶️ **Como Rodar o Projeto**

1.Clone este repositório:
git clone https://github.com/IamRangel/Supermarket_Analysis.git

2.Acesse o diretório do projeto:
cd Supermarket_Analysis

3.Instale as dependências necessárias:
pip install pandas

4.Coloque o arquivo **SuperMarketAnalysis.csv** na pasta data_raw.

5.Execute o script ETL:
python scripts/etl_supermarket.py

Os arquivos processados serão gerados na pasta data_processed_small e poderão ser importados no Power BI.

---

📸 **Captura do Dashboard**

![Dashboard do Projeto](ecommerce_supermarket_project/visuals/Captura%20de%20Tela.png)
