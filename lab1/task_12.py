tarif_minutes = 60
tarif_sms = 30
tarif_internet = 1024
tarif_price = 24.99

minute_over = 0.89
sms_over = 0.59
mb_over = 0.79

nalog = 0.02

used_minutes = int(input("Введите количество вами израсходованных минут за месяц:\n"))
used_sms = int(input("Введите количество вами отправленных SMS за месяц:\n"))
used_internet = int(input("Введите объем вами использованного интернет-трафика за месяц (в МБ):\n"))

plus_minutes = used_minutes - tarif_minutes
plus_sms = used_sms - tarif_sms
plus_internet = used_internet - tarif_internet

if plus_minutes < 0:
    plus_minutes = 0
if plus_sms < 0:
    plus_sms = 0
if plus_internet < 0:
    plus_internet = 0

prise_minutes = plus_minutes * minute_over
prise_sms = plus_sms * sms_over
prise_internet = plus_internet * mb_over

no_nalog = tarif_price + prise_minutes + prise_sms + prise_internet
summ_nalog = no_nalog * nalog
total = no_nalog + summ_nalog

print("Тариф:", tarif_price, "руб.")
if plus_minutes > 0:
    print("Минут сверх тарифа: " + str(plus_minutes) + " шт, доплата " + str(round(prise_minutes, 2)) + " руб.")
if plus_sms > 0:
    print("SMS сверх тарифа: " + str(plus_sms) + " шт, доплата " + str(round(prise_sms, 2)) + " руб.")
if plus_internet > 0:
    print("Интернет сверх тарифа: " + str(plus_internet) + " МБ, доплата " + str(round(prise_internet, 2)) + " руб.")
print("Налог: " + str(round(summ_nalog, 2)) + " руб.")
print("Всего к оплате: " + str(round(total, 2)) + " руб.")