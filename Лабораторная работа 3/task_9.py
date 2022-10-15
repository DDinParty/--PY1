salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
while months != 0:
    need_money += spend
    need_money -= salary
    months -= 1
    spend *= (increase+1)

print(round(need_money))
