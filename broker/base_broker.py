class BaseBroker:
    """
    Classe base para qualquer corretora.
    Todas as corretoras reais ou simuladas devem seguir esse modelo.
    """

    def get_klines(self, symbol: str, interval: str, limit: int = 100):
        raise NotImplementedError("Método get_klines() não implementado.")

    def buy_market(self, symbol: str, quantity: float):
        raise NotImplementedError("Método buy_market() não implementado.")

    def sell_market(self, symbol: str, quantity: float):
        raise NotImplementedError("Método sell_market() não implementado.")

    def get_balance(self, asset: str = "USDT"):
        raise NotImplementedError("Método get_balance() não implementado.")
