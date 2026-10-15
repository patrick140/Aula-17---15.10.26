import pandas as pd

dados = {
    'categoria': ['Eletrônicos', 'Eletrônicos', 'Eletrônicos', 'Eletrônicos',
                  'Roupas', 'Roupas', 'Roupas', 'Roupas',
                  'Alimentos', 'Alimentos', 'Alimentos', 'Alimentos'],
    'ano':       [2022, 2022, 2023, 2023,
                  2022, 2022, 2023, 2023,
                  2022, 2022, 2023, 2023],
    'vendas':    [1000, 1500, 2000, 2500,
                  800,  900,  1100, 1300,
                  500,  600,  700,  850]
}

df = pd.DataFrame(dados)

print("DataFrame Original")
print(df)
print("\n")

# 2. Aplicando o pivot_table
tabela_pivot = df.pivot_table(
    index='categoria', #Define a coluna que será usada como linha da tabela
    columns='ano', #Define a coluna que será usada como coluna tabela
    values='vendas',  #Coluna cujos valores serão agregados
    aggfunc='sum' #Função de agregação
)

print("vendas somadas por categoria e ano")
print(tabela_pivot)
print("\n")
