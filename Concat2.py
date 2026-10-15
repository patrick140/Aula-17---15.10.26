import pandas as pd

df1 = pd.read_csv(r"C:\Users\patrick.araujo\Documents\Aulas\Analista de dados\funcionarios (1).csv")

df2 = pd.read_csv(r"C:\Users\patrick.araujo\Documents\Aulas\Analista de dados\funcionarios_v2.csv")

print(df1)

print("\n") 

print(df2)

print("\n")

resultado_vertical = pd.concat([df1, df2])

print(resultado_vertical)


print("\n")

df1_lucroLiquido = (df1["lucro"] - df1["salario"]).rename("lucroLiquido")
df2_lucroLiquido = (df2["lucro"] - df2["salario"]).rename("lucroLiquido")

resultado_horizontal1 = pd.concat([df1, df1_lucroLiquido], axis=1)

resultado_horizontal2 = pd.concat([df2, df2_lucroLiquido], axis=1)

print(resultado_horizontal1)
print("\n")

print(resultado_horizontal2)
print("\n")




