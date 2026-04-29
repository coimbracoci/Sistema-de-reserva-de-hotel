class Reserva:
    def __init__(self, hospede, quarto, quant_dias):
        self.hospede = hospede
        self.quarto = quarto
        self.quantidade_dias = quant_dias
    def reservar(self):
        if self.quantidade_dias > 0:
            if self.quarto.disponivel:
                self.quarto.disponivel = False
                return f"Reserva realizada!"
            else:
                return f"Quarto indisponivel."
        else:
            return f"Número de dias inválido."
    def calcular_valor(self):
        vt = self.quarto.valor_diaria * self.quantidade_dias
        return f"Valor total: R${vt:.2f}"
    def cancelar_reserva(self):
        if self.quarto.disponivel == False:
            self.quarto.disponivel = True
            return f"Reserva cancelada."
        else:
            return f"Não há reserva ativa."
    def resumo(self):
        return f"Hóspede: {self.hospede.nome_hospede} \nCPF: {self.hospede.cpf_hospede} \nDias: {self.quantidade_dias} \n{self.calcular_valor()}"