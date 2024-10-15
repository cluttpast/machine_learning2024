Nail_style=['Шеллак', 'Френч', 'Обычный лак', 'Гель-лак', 'Акрил']
Price=[2000, 1500, 1000, 3000, 3500]
Week=[4, 5, 4, 8, 6]
visits_avg=sum(Week)/len(Week)
visits_all=sum(Week)
n=0
income=0
for n in range(len(Week)):
    price_per_week=Price[n]*Week[n]
    income+=price_per_week
    n+=1
print("Среднне число посещений в месяц =",visits_avg)
print("Всего посещений =", visits_all)
print("Прибыль за неделю =", income)
m=0
for m in range(len(Week)):
    print(Nail_style[m], ": прибыль за неделю -", Price[m]*Week[m], "|||", "Средняя прибыль за день -", (Price[m]*Week[m])/7)
    m+=1
    