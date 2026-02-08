from address import Address
from mailing import Mailing


to_address = Address(129402, "Florida", "Nilson", 35, 531)
from_address = Address(298532, "Tokyo", "Vilniok", 92, 8)
cost = 3094
track = 870378024587

my_mailing = Mailing(to_address, from_address, cost, track)

print((f"Отправление: {track} из {from_address} в {to_address}. "
       f"Стоимость {cost} рублей."))
