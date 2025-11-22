import os
import pandas as pd

# Pastas 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW = os.path.join(BASE_DIR, "data_raw")
DATA_PROCESSED = os.path.join(BASE_DIR, "data_processed_small")
os.makedirs(DATA_PROCESSED, exist_ok=True)

df = pd.read_csv(os.path.join(DATA_RAW, "SuperMarketAnalysis.csv"))

df.columns = df.columns.str.strip()

df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)  
df['Sales'] = df['Sales'].astype(float).round(2)
df['Tax 5%'] = df['Tax 5%'].astype(float).round(2)
df['Unit price'] = df['Unit price'].astype(float)
df['Quantity'] = df['Quantity'].astype(int)

df['Month'] = df['Date'].dt.to_period('M')

print("Primeiras linhas das colunas numéricas:")
print(df[['Sales', 'Tax 5%', 'Unit price', 'Quantity']].head(10))

print("\nResumo das colunas numéricas:")
print(df[['Sales', 'Tax 5%', 'Unit price', 'Quantity']].describe())

# Vendas por mês 
vendas_mes = df.groupby('Month')['Sales'].sum().round(2).reset_index()
print("\nVendas por mês (amostra):")
print(vendas_mes.head())
vendas_mes.to_csv(os.path.join(DATA_PROCESSED, "vendas_mes.csv"), index=False, decimal=',')

# Ticket médio por cliente
ticket_medio = df.groupby('Customer type')['Sales'].mean().round(2).reset_index()
ticket_medio.rename(columns={'Sales':'avg_ticket'}, inplace=True)
print("\nTicket médio por cliente (amostra):")
print(ticket_medio.head())
ticket_medio.to_csv(os.path.join(DATA_PROCESSED, "ticket_medio.csv"), index=False, decimal=',')

# Vendas por categoria de produto
vendas_categoria = df.groupby('Product line')['Sales'].sum().round(2).reset_index()
print("\nVendas por categoria (amostra):")
print(vendas_categoria.head())
vendas_categoria.to_csv(os.path.join(DATA_PROCESSED, "vendas_categoria.csv"), index=False, decimal=',')

# Vendas por filial 
vendas_branch = df.groupby('Branch')['Sales'].sum().round(2).reset_index()
print("\nVendas por filial (amostra):")
print(vendas_branch.head())
vendas_branch.to_csv(os.path.join(DATA_PROCESSED, "vendas_branch.csv"), index=False, decimal=',')

# Vendas por tipo de pagamento
vendas_payment = df.groupby('Payment')['Sales'].sum().round(2).reset_index()
print("\nVendas por tipo de pagamento (amostra):")
print(vendas_payment.head())
vendas_payment.to_csv(os.path.join(DATA_PROCESSED, "vendas_payment.csv"), index=False, decimal=',')

print("Arquivos prontos!")
