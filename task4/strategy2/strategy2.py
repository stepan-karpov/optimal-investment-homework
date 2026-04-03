from freqtrade.strategy import IStrategy
from pandas import DataFrame
import pandas as pd

class Strategy2(IStrategy):
    INTERFACE_VERSION = 3
    timeframe = '1d'
    can_short = True

    minimal_roi = {"0": 0.0}
    stoploss = -1.0
    trailing_stop = False
    use_exit_signal = True
    exit_profit_only = False

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['rsi'] = pd.TaLib.RSI(dataframe['close'], timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['enter_long'] = (dataframe['rsi'] < 30).astype(int)
        dataframe['enter_short'] = (dataframe['rsi'] > 70).astype(int)
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Выход ровно через 48 часов (2 свечи)
        dataframe['exit_long'] = dataframe['enter_long'].shift(2).fillna(0).astype(int)
        dataframe['exit_short'] = dataframe['enter_short'].shift(2).fillna(0).astype(int)
        return dataframe