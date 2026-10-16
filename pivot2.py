import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.loureiro\Documents\Aulas\funcionarios.csv")


print(df)


tabela_pivot = df.pivot_table(
    index='departamento', #Define a coluna que será usada como linha da tabela
    columns='ativo', #Define a coluna que será usada como coluna
    values='salario', #Coluna cujos valores serão agregados
    aggfunc='sum' #Função de agregação
)

print(tabela_pivot)