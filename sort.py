import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.araujo\Documents\Aulas\Analista de dados\funcionarios (1).csv")

df = df.sort_values('salario')

df = df.sort_values('salario', ascending=False)

print(df)