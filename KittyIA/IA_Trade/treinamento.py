import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam
import joblib

# Carregar os dados processados
df = pd.read_csv("dados_processados.csv")

# Separar recursos (X) e alvo (y)
X = df[['open', 'high', 'low', 'close']].values
y = df['close'].values

# Corrigir tamanho de X para coincidir com y
X = X[:len(y)]

# Verificar tamanhos
print("Tamanho de X:", X.shape)
print("Tamanho de y:", y.shape)

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Criar o modelo de rede neural
model = Sequential([
    layers.Dense(64, activation='relu', input_dim=X_train.shape[1]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])

# Compilar o modelo
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

# Treinar o modelo
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))

# Salvar o modelo treinado
model.save("modelo_trade.h5")
joblib.dump(X, "scaler_X.pkl")
joblib.dump(y, "scaler_y.pkl")

print("Treinamento concluído e modelo salvo!")

import joblib

# Salvar o modelo treinado
joblib.dump(model, 'modelo_treinado.pkl')