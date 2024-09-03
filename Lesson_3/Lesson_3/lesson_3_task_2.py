from smartphone import Smartphone
catalog = []
phone1 = Smartphone("Apple", "iPhone 11", "+795767879898")
phone2 = Smartphone("Xiaomi", "Mi 11", "+79876543210")
phone3 = Smartphone("Samsung", "Galaxy S", "+79011234567")
phone4 = Smartphone("Motorolla", "Raz V3", "+79745689977")
phone5 = Smartphone("Huawei", "P40", "+79648964265")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
