from token_data.binance import binance_to_file


if __name__ == "__main__":
    binance_to_file(
        token_list=['ZRO/USDT'],
        timeframe='1h',
        first_date='2010-01-01T00:00:00Z',
        all_tokens=False,
        verbose=True,
    )
