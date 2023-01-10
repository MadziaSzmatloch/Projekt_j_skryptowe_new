from raport import now 

time = now
for i in time:
    time = time.replace('/', '-')
    time = time.replace(' ', '-')
    time = time.replace(':', '-')
    
file = open("time.txt", "w")
file.write(time)
file.close()