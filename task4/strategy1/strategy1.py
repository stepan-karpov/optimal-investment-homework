
from freqtrade.strategy import IStrategy
from pandas import DataFrame

class Strategy1(IStrategy):
    INTERFACE_VERSION = 3
    timeframe = '1d'
    can_short = True

    minimal_roi = {"0": 0.0}
    stoploss = -1.0
    trailing_stop = False
    use_exit_signal = True
    exit_profit_only = False

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['enter_long'] = 0
        dataframe['enter_short'] = (
            (dataframe['close'] < dataframe['open']) &                  # красная свеча
            (dataframe['close'].shift(1) < dataframe['open'].shift(1)) & # предыдущая красная
            (dataframe['close'].shift(2) < dataframe['open'].shift(2))   # третья красная подряд
        ).astype(int)
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['exit_long'] = 0
        dataframe['exit_short'] = dataframe['enter_short'].shift(2).fillna(0).astype(int)
        return dataframe