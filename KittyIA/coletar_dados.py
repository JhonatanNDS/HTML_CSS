import MetaTrader5 as mt5
import pandas as pd

# Inicializa o MT5
mt5.initialize()

# Definir o par e timeframe
ativo = "BTCUSD"
timeframe = mt5.TIMEFRAME_M1  # 1 Minuto

# Coletar 1000 candles
dados = mt5.copy_rates_from_pos(ativo, timeframe, 0, 1000)

# Encerrar conexão com MT5
mt5.shutdown()

# Criar DataFrame
df = pd.DataFrame(dados)

# Verificar as colunas e dados
print(df.head())

# Salvar CSV
df.to_csv("dados_btc.csv", index=False)
print("✅ Dados salvos com sucesso!")
