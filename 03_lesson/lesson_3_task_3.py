from adress import Adress
from mailing import Mailing


to_adress = Adress(129402, "Florida", "Nilson", 35, 531)
from_adress = Adress(298532, "Tokyo", "Vilniok", 92, 8)
cost = 3094
track = 870378024587

my_mailing = Mailing(to_adress, from_adress, cost, track)

print((f"Отправление: {track} из {from_adress} в {to_adress}. "
       f"Стоимость {cost} рублей."))
