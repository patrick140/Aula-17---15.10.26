import pandas as pd

df = pd.read_csv(r"C:\Users\patrick.loureiro\Documents\Aulas\funcionarios.csv")

print(df)

#print(df.groupby('departamento').agg(Media_salarios= ("salario", "mean")).round(2))


# Agrupar por departamento e situação do funcionário
resultado = df.groupby(["departamento", "ativo"]).size()

print(resultado)


# Agrupar por departamento e agregação de varias colunas
resultado = df.groupby("departamento").agg(
    quantidade_funcionarios=("id", "count"),
    salario_medio=("salario", "mean"),
    maior_salario=("salario", "max"),
    lucro_total=("lucro", "sum")
)

print(resultado.round(2)) #.round(2) retorna os valores float com somente duas casas decimais




