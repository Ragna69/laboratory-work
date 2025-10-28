ip = input('Введите IP для проверки на корректность:\n')
ip = ip.strip()
ip = ip.split('.')
if len(ip) != 4:
    print('Неверный формат IP адреса!')
else:
    if not ip[0].isdigit() or  int(ip[0]) < 0 or int(ip[0]) > 255 or not\
            ip[1].isdigit() or int(ip[1]) < 0 or int(ip[1]) > 255 or not\
            ip[2].isdigit() or int(ip[2]) < 0 or int(ip[2]) > 255 or not\
            ip[3].isdigit() or int(ip[3]) < 0 or int(ip[3]) > 255:
        ip = '.'.join(ip)
        print('Ваш IP', ip, 'некорректный')
    else:
        ip = '.'.join(ip)
        print('Ваш IP', ip, 'корректный')