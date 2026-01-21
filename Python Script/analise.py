import pandas as pd
import matplotlib.pyplot as plt


# Vamos começar criando os dados
data = {
    'Nome': ['Greatsword', 'Claymore', 'Uchigatana', 'Longsword', 'Reduvia'],
    'Dano_Base': [164,138,115,110,79],
    'Peso': [23.0, 9.0, 5.5, 3.5, 2.5],
    'Atributo': ['Strength', 'Strength', 'Dexterity', 'Strength', 'Dexterity']
}


df = pd.DataFrame(data)


# Agora Vamos criar a metrica de Eficiencia, dividindo dano base pelo peso
df['Eficiencia'] = df['Dano_Base'] / df['Peso']

# Com isso podemos gerar a média por atributo, mostrando qual vale mais a pena em relação de seu peso pelo seu dano base, assim, mostrando a possibilidade de dar mais dano
# usando menos pontos de atributo

media_atributo = df.groupby('Atributo')['Eficiencia'].mean()
print("Média de Eficiência por Atributo:")
print(media_atributo)

# Agora podemos criar um gráfico automático que vai nos mostrar esses valores
df.sort_values('Eficiencia', ascending=False).plot(x='Nome', y='Eficiencia', kind='bar', color='skyblue')
plt.title('Elden Ring: Efficiency By Weapon (Python)')
plt.ylabel('Damage/Weight Ratio')
plt.tight_layout()

# Agora Vamos Salvar o grafico como imagem 
plt.savefig('grafico_python.png')
print("\nGráfico gerado com sucesso!")