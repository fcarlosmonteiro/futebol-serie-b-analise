import pandas as pd

# abrir a base de dados
df = pd.read_csv("dataset/dataset.csv")

# imprimir as primeiras linhas da base de dados
print(df.head())

# imprimir as colunas da base de dados
print("\nColunas da base de dados:")
print(df.columns.tolist())

# imprimir tipos de dados das colunas
print("\n Tipos de dados das colunas:")
print(df.dtypes)

#verificar dimensões da base de dados
print("\nDimensões da base de dados:")
print(df.shape)