import joblib
import MetaTrader5 as mt5
import pandas as pd

# Conectar ao MT5
mt5.initialize()

# Carregar o modelo treinado
modelo = joblib.load('modelo_treinado.pkl')

# Definir o ativo e timeframe
ativo = "BTCUSD"
timeframe = mt5.TIMEFRAME_M1  # 1 minuto

# Pegar os últimos 100 candles
dados = mt5.copy_rates_from_pos(ativo, timeframe, 0, 100)
df = pd.DataFrame(dados)

# Aplicar a rede neural para prever a próxima ação
previsao = modelo.predict(df.iloc[-1].values.reshape(1, -1))

# Decisão de compra/venda
if previsao == 1:
    print("Sinal de COMPRA")
elif previsao == -1:
    print("Sinal de VENDA")
else:
    print("Manter posição")

# Finalizar conexão
mt5.shutdown()
