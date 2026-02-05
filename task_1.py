string = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0
tims = string.split(',')

for time_part in tims:
    time_part = time_part.replace(' ', '')  # убираем пробелы
    
    # ЧАСЫ: удаляем всё кроме цифр перед h
    if 'h' in time_part:
        hours_str = time_part.replace('m', '').replace('s', '').split('h')[0]
        total_minutes += int(hours_str) * 60
    
    # МИНУТЫ: удаляем всё кроме цифр перед m  
    if 'm' in time_part:
        minutes_str = time_part.replace('h', '').replace('s', '').split('m')[0]
        total_minutes += int(minutes_str)
    
    # СЕКУНДЫ: удаляем всё кроме цифр перед s
    if 's' in time_part:
        seconds_str = time_part.replace('h', '').replace('m', '').split('s')[0]
        total_minutes += int(seconds_str) // 60

print(total_minutes)  # 115