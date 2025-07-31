import pandas as pd

df = pd.read_csv("dataset.csv")

# método para tratar valores ausentes
def tratar_valores_ausentes(df):
    print("Verificando valores ausentes")
    print(df.isnull().sum())

    # preencher valores ausentes com a mediana da coluna
    df_corrigido = df.fillna(df.median(numeric_only=True))
    return df_corrigido

# método para remover registros duplicados
def remover_duplicatas(df):
    print(f"\n Registros duplicados encontrados: {df.duplicated().sum()}")

    df_sem_duplicatas = df.drop_duplicates()
    return df_sem_duplicatas

#executando as funções de pré-processamento
print("Iniciando limpeza dos dados...")
df_new = tratar_valores_ausentes(df)
df_final = remover_duplicatas(df_new)

#salvar o DataFrame corrigido em um novo arquivo CSV
df_final.to_csv("dataset_corrigido.csv", index=False)  

