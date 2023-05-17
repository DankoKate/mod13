# Запрашиваем количество билетов, добавляем к ней возраст каждого посетителя и определяем стоимость каждого билета
num_tickets = int(input("Введите количество билетов: "))
total_cost = 0
for i in range(num_tickets):
    age = int(input(f"Введите возраст посетителя {i+1}: "))
    if age < 18:
        ticket_cost = 0
    elif age >= 18 and age < 25:
        ticket_cost = 990
    else:
        ticket_cost = 1390
    total_cost += ticket_cost

# Применяем скидку, если кол-во билетов больше 3
if num_tickets > 3:
    total_cost *= 0.9

# Выводим итоговую стоимость
print(f"Сумма к оплате: {total_cost} руб.")