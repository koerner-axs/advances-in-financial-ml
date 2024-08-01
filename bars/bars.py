import pandas as pd

from datasets.load_dataset import get_sp_future_ticks


def make_trade_bars(tickdata: pd.DataFrame, trades_per_bar: int) -> pd.DataFrame:
    grouped = tickdata.reset_index().groupby(tickdata.index // trades_per_bar)
    # TODO: force end of bar at end of day
    return grouped.agg(
        {
            'price': 'ohlc',
            'volume': 'sum'
        }
    )


if __name__ == '__main__':
    sp_future_ticks = get_sp_future_ticks(abbreviated=False)
    print(f'Found {len(sp_future_ticks)} future ticks.')
    bars = make_trade_bars(sp_future_ticks, 100)
    print(bars)

    import plotly.graph_objects as go

    fig = go.Figure(data=[go.Candlestick(x=bars.index,
                                         open=bars['price']['open'],
                                         high=bars['price']['high'],
                                         low=bars['price']['low'],
                                         close=bars['price']['close'])])
    fig.show()
