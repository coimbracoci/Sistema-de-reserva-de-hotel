from hospede import Hospede
from quarto import Quarto
from reserva import Reserva

cadastro = Hospede('Matheus', '457.282.383-1', '94838-2822')
cadastro1 = Quarto(43, 'Duas camas', 350)
cadastro2 = Reserva(cadastro, cadastro1, 4)

print(cadastro2.reservar())
print(cadastro2.calcular_valor())
print(cadastro2.resumo())
print(cadastro2.cancelar_reserva())
print(cadastro2.cancelar_reserva())
