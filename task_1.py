total_minutes = 0
times_str = '1h 45m,360s,25m,30m 120s,2h 60s'

times_str = times_str.replace(' ',',' )
times_list = times_str.split(',')

for time_entry in times_list:
    if 'h' in time_entry:
        time_entry = time_entry.replace('h','')
        time_minutes = int(time_entry) * 60
        total_minutes += time_minutes
    elif 's' in time_entry:
        time_entry = time_entry.replace('s','')
        time_minutes = int(time_entry) // 60
        total_minutes += time_minutes
    else:
        time_entry = time_entry.replace('m','')
        time_minutes = int(time_entry)
        total_minutes += time_minutes

print(total_minutes)