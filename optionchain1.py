def request_option_chain(self, symbol='SPX', exchange='CBOE'):
        try:
            underlying = Index(symbol, exchange)
            print("********  OPTION CHAIN *********")
            print(f"Requesting option chain for {underlying.symbol}")

            contract_details = self.ib.reqContractDetails(underlying)
            if contract_details:
                conId = contract_details[0].contract.conId
                print(f"ConId for {symbol}: {conId}")

                option_chain = self.ib.reqSecDefOptParams(underlying.symbol, '', underlying.secType, conId)
                for chain in option_chain:
                    print(f"Exchange: {chain.exchange}")
                    print(f"Underlying ConId: {chain.underlyingConId}")
                    print(f"Trading Class: {chain.tradingClass}")
                    print(f"Multiplier: {chain.multiplier}")
                    print(f"Expirations: {chain.expirations}")
                    print(f"Strikes: {chain.strikes}")
                    print('-' * 50)
            print("********  END Here (Requesting option Chain) *********")
        except Exception as e:
            print(f"Failed to get option chain response: {e}")

        res = request_option_chain();  

        print(res);  