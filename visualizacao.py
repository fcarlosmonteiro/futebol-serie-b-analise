import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

# Carregar o dataset
df = pd.read_csv('dataset_novo_atributo.csv')

# Conversão de tipos
df['Aproveitamento'] = df['Aproveitamento'].astype(float)
df['Público'] = df['Público'].astype(float)
df['GP'] = df['GP'].astype(float)

# --------------------------------------
# Q1 – Distribuição do Aproveitamento
# --------------------------------------
plt.figure(figsize=(10, 6))

counts, bins, patches = plt.hist(df['Aproveitamento'], bins=10, color='skyblue', edgecolor='black')
for count, x in zip(counts, bins):
    if count > 0:
        plt.text(x + 0.5, count + 0.1, int(count), ha='center', fontsize=8)

media_ap = df['Aproveitamento'].mean()
mediana_ap = df['Aproveitamento'].median()
plt.axvline(media_ap, color='red', linestyle='--', label=f'Média: {media_ap:.2f}%')
plt.axvline(mediana_ap, color='green', linestyle='--', label=f'Mediana: {mediana_ap:.2f}%')
plt.title('Q1 – Distribuição do Aproveitamento dos Times')
plt.xlabel('Aproveitamento (%)')
plt.ylabel('Frequência')
plt.legend()
plt.tight_layout()
plt.savefig('grafico_q1_histograma_aproveitamento.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

# --------------------------------------
# Q2 – Maior e Menor Público e Aproveitamento
# --------------------------------------
plt.figure(figsize=(10, 6))

maior_pub = df.loc[df['Público'].idxmax()]
menor_pub = df.loc[df['Público'].idxmin()]
times = [maior_pub['Time'], menor_pub['Time']]
publicos = [maior_pub['Público'], menor_pub['Público']]
aproveitamentos = [maior_pub['Aproveitamento'], menor_pub['Aproveitamento']]

bars = plt.bar(times, publicos, color=['orange', 'purple'])
for i in range(2):
    plt.text(i, publicos[i] + 1000, f"Aprov: {aproveitamentos[i]:.1f}%", ha='center', fontsize=10)
    plt.text(i, 500, f"{int(publicos[i])} pessoas", ha='center', fontsize=9, color='white')
plt.title('Q2 – Maior e Menor Público Médio vs Aproveitamento')
plt.ylabel('Público Médio')
plt.xlabel('Time')
plt.tight_layout()
plt.savefig('grafico_q2_publico_aproveitamento.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

# --------------------------------------
# Q3 – Gols Marcados x Aproveitamento
# --------------------------------------
plt.figure(figsize=(12, 8))

scatter = plt.scatter(df['GP'], df['Aproveitamento'], c=df['Aproveitamento'], cmap='viridis', s=80, edgecolors='black')
m, b = np.polyfit(df['GP'], df['Aproveitamento'], 1)
plt.plot(df['GP'], m * df['GP'] + b, color='green', linestyle='--', label='Tendência linear')

r, _ = pearsonr(df['GP'], df['Aproveitamento'])
plt.text(min(df['GP']) + 0.5, max(df['Aproveitamento']) - 5, f"Correlação de Pearson: r = {r:.2f}", fontsize=12, color='darkgreen')

for i, row in df.iterrows():
    plt.text(row['GP'] + 0.1, row['Aproveitamento'], row['Time'], fontsize=8, alpha=0.7)

plt.title('Q3 – Relação entre Gols Marcados (GP) e Aproveitamento')
plt.xlabel('Gols Pró (GP)')
plt.ylabel('Aproveitamento (%)')
plt.colorbar(scatter, label='Aproveitamento (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('grafico_q3_gols_aproveitamento.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

print("Gráficos salvos com sucesso!")
print("- grafico_q1_histograma_aproveitamento.png")
print("- grafico_q2_publico_aproveitamento.png")
print("- grafico_q3_gols_aproveitamento.png")
