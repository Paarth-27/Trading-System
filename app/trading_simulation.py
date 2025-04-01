import pandas as pd

def moving_average_crossover_strategy(data: pd.DataFrame):
    data['50_SMA'] = data['price'].rolling(window=50).mean()
    data['200_SMA'] = data['price'].rolling(window=200).mean()

    buy_signals = []
    sell_signals = []
    position = None  # None means no position, 'buy' means holding a stock

    for i in range(200, len(data)):
        if data['50_SMA'][i] > data['200_SMA'][i] and position != 'buy':
            buy_signals.append(i)
            position = 'buy'
        elif data['50_SMA'][i] < data['200_SMA'][i] and position == 'buy':
            sell_signals.append(i)
            position = None

    return buy_signals, sell_signals

