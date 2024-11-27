from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)

stock = Stock('AAPL', 'SMART', 'USD')
ib.qualifyContracts(stock)

ib.sleep(1)

#chains = ib.reqSecDefOptParams(stock.symbol, '', stock.secType, stock.conId)

symbol='AAPL'
exchange='CBOE'
underlying = Index(symbol, exchange)
contract_details = ib.reqContractDetails(underlying)

conId = contract_details[5].contract.conId
print(f"ConId for {symbol}: {conId}")

option_chain = ib.reqSecDefOptParams(underlying.symbol, '', underlying.secType, conId)
for chain in option_chain:
                    print(f"Exchange: {chain.exchange}")
                    print(f"Underlying ConId: {chain.underlyingConId}")
                    print(f"Trading Class: {chain.tradingClass}")
                    print(f"Multiplier: {chain.multiplier}")
                    print(f"Expirations: {chain.expirations}")
                    print(f"Strikes: {chain.strikes}")
                    print('-' * 50)
print("********  END Here (Requesting option Chain) *********")

# print(util.df(chains))