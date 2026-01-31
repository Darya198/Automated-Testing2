def month_to_season(mon):
    if 1 <= mon <= 2 or mon == 12:
        return "Зима"
    if 2 <= mon <= 6:
        return "Весна"
    if 6 <= mon <= 9:
        return "Лето"
    if 9 <= mon <= 12:
        return "Осень"
    else:
        return "Введен неверный номр месяца"


mon = int(input("Введите номер месяца (1-12): "))


print(month_to_season(mon))
