# =========================================
# TRAILING STOP PARA O ROBÔ DE TRADING
# =========================================

class TrailingStop:
    def __init__(self, distance=0.01):
        """
        distance = distância do trailing (1% por padrão)
        Ex: 0.01 = 1%
        """
        self.distance = distance
        self.highest_price = None
        self.active = False

    def reset(self):
        """Reinicia o trailing stop após sair da operação"""
        self.highest_price = None
        self.active = False

    def update(self, current_price):
        """
        Atualiza o trailing stop conforme o preço se movimenta.
        Retorna: 
            None → não aciona
            preço_stop → para acionar venda
        """
        # Primeiro valor
        if not self.active:
            self.highest_price = current_price
            self.active = True
            return None

        # Atualiza topo
        if current_price > self.highest_price:
            self.highest_price = current_price

        # Calcula o stop atual
        stop_price = self.highest_price * (1 - self.distance)

        # Se caiu e tocou o stop → sinaliza saída
        if current_price <= stop_price:
            return stop_price

        return None
