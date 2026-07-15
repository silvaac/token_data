from token_data.kucoin  import kucoin_to_file
from token_data.kraken  import kraken_to_file
from token_data.coinbase import coinbase_to_file


if __name__ == "__main__":
    kucoin_to_file(
        token_list=['LIT-USDT'],
        timeframe='1h',
        first_date='2025-01-01T00:00:00Z',
        all_tokens=False,
        verbose=True,
    )
    #kraken_to_file(folder_path="../data/kraken",
    #           token_list=['XMR/USD'],
    #           type="parquet", timeframe='1h')
    #coinbase_to_file(
    #    token_list=['LIT-USD'],
    #    all_tokens=False,
    #    type="parquet"
    #)
