from address import Address
from mailing import Mailing

to_address = Address("620345", "Екатеринбург", "Татищева", "23", "5")
from_address = Address("456234", "Москва", "Мира", "123", "45")
mailing = Mailing(to_address, from_address, 300, "34545P")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.number} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.number}. Стоимость {mailing.cost} рублей.")