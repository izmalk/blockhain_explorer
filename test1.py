from pycoingecko import CoinGeckoAPI
import json

# Create an instance of the CoinGeckoAPI
cg = CoinGeckoAPI()

# Get Bitcoin transaction data
bitcoin_data = cg.get_coin_by_id('bitcoin', localization=False, tickers=False, market_data=True, community_data=False,
                                 developer_data=False)

# Access the transaction data
transaction_data = bitcoin_data
# ['public_interest_stats']
# ['transactions']
print(json.dumps(transaction_data, indent=4))
