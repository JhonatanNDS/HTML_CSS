import pandas as pd
from sklearn.preprocessing import StandardScaler

# Carregar os dados
df = pd.read_csv('dados_btcusd.csv')  # Substitua 'dados_btc.csv' pelo nome correto do arquivo com os dados

# Verifique se os dados foram carregados corretamente
print(df.head())

# Selecione as colunas que você quer usar no modelo (exemplo: time, open, high, low, close)
df = df[['time', 'open', 'high', 'low', 'close']]

# Pré-processamento: escalonando os dados
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['open', 'high', 'low', 'close']])

# Adiciona as características escalonadas de volta ao DataFrame
df[['open', 'high', 'low', 'close']] = scaled_features

# Salve os dados pré-processados
df.to_csv('dados_processados.csv', index=False)

print("Dados pré-processados e salvos com sucesso!")
