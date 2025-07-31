import pandas as pd
import numpy as np

df = pd.read_csv("dataset_corrigido.csv")

#Etapa de agregação dos dados
def calcular_medias(df):
    print("MÉDIAS GERAIS DA RODADA")
    print("Média de pontos:", round(df['Pontos'].mean(), 2))
    print("Média de gols marcados:", round(df['GP'].mean(), 2))
    print("Média de gols sofridos:", round(df['GC'].mean(), 2))
    print("\n")

#Função para adicionar coluna de público
def adicionar_publico(df):
    df["Público"] = np.random.randint(1000, 50000, size=len(df))
    return df

#Função para reduzir os dados com os 4 melhores e 4 piores clubes
def reducao_dados(df):
    df_ordenado = df.sort_values(by='Pontos', ascending=False).reset_index(drop=True)

    g4 = df_ordenado.head(4).copy()
    z4 = df_ordenado.tail(4).copy()
    g4['Faixa'] = 'G4'
    z4['Faixa'] = 'Z4'

    df_reduzido = pd.concat([g4, z4], ignore_index=True)
    return df_reduzido

calcular_medias(df)
df = adicionar_publico(df)
df_reduzido = reducao_dados(df)

df.to_csv("dataset_novo_atributo.csv", index=False)
df_reduzido.to_csv("dataset_reduzido.csv", index=False)
