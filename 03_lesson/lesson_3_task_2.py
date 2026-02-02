from smartphone import Smartphone


catalog = [
    Smartphone("Samsung", "A33", "+79573867206"),
    Smartphone("Poco", "d023", "+79759375955"),
    Smartphone("IPhone", "18 Pro", "+79205993756"),
    Smartphone("Xiomi", "zet648", "+79096320365"),
    Smartphone("Lenovo", "B52", "+79208703701")]


for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model}. {smartphone.number}")
