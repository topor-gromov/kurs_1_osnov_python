duration = int(input('Введите продолжительность времени (в секундах): '))

duration_second = duration % 60
duration_minute = (duration - duration_second) // 60
text_result = str(duration_second) + ' сек'
duration_hour = 0
duration_day = 0
if duration_minute != 0:
   if duration_minute > 59:
        duration_hour = duration_minute // 60
        duration_minute = duration_minute % 60
        text_result = str(duration_minute) + ' мин ' + text_result
        if duration_hour > 23:
            duration_day = duration_hour // 24
            duration_hour = duration_hour % 24
        text_result = str(duration_hour) + ' час ' + text_result
        if duration_day != 0:
            text_result = str(duration_day) + ' дн ' + text_result
   else:
       text_result = str(duration_minute) + ' мин ' + text_result

print(text_result)
