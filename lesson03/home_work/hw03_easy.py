# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, nd):
    lnum = str(number).split('.')
    if len(lnum[1]) > nd:
        dr = int(lnum[1][0:nd])
        ld = int(lnum[1][nd])
        if ld >= 5:
            dr += 1
            snewdr = str(dr)
        else:
            snewdr = str(dr)

        if len(snewdr) > nd:
            sdi = str(int(lnum[0]) + 1)
            snewdr = snewdr[1:]
        else:
            sdi = str(int(lnum[0]))

        my_round = '{}.{}'.format(sdi, snewdr)
    else:
        my_round = str(number)
    return my_round


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ltn = str(ticket_number)
    if len(ltn) == 6:
        ls = 0
        rs = 0
        for li in ltn[0:3]:
            ls = ls + int(li)
        for li in ltn[3:6]:
            rs = rs + int(li)
        if ls == rs:
            lucky_ticket = 'Lucky ticket! {} == {}'.format(ls, rs)
        else:
            lucky_ticket = 'Unlucky ticket! {} != {}'.format(ls, rs)
    else:
        lucky_ticket = 'Strange ticket! Not 6 digits!'
    return lucky_ticket



print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
