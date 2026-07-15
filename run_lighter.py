from token_data.lighter import lighter_to_file


if __name__ == "__main__":
    lighter_to_file(
        token_list=['LIT/USDC'],
        timeframe='1h',
        first_date='2025-01-01T00:00:00Z',
        all_tokens=False,
        verbose=True,
    )
