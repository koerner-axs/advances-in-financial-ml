import pandas as pd


def get_sp_future_ticks(base_dir: str = 'datasets/', abbreviated: bool = False) -> pd.DataFrame:
    filename = f'{base_dir}SP.csv' if not abbreviated else f'{base_dir}SP_abbreviated.csv'
    with open(filename, 'r') as fd:
        df = pd.read_csv(fd)
        df['timestamp'] = pd.to_datetime(df['date'] + ' ' + df['time'])
        return df


if __name__ == '__main__':
    sp_future_ticks = get_sp_future_ticks(base_dir='')
    print(f'Found {len(sp_future_ticks)} future ticks.')
    print(sp_future_ticks[:5])
    print('...')
    print(sp_future_ticks[-5:])
