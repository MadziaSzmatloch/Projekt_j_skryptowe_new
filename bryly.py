import math

file = open("inputdata.txt", "r")
lines = file.readlines()
data = []
for line in lines:
    data.append(line.strip("\n"))

func = data[0]
a = float(data[1])
b = float(data[2])
n = int(data[3])

Xaxis = []
Yaxis = []

def algorithm(function):
    
    l1 = (abs(a)+abs(b))/n
    pole = 0
    for i in range(n+1):
        Xaxis.append(a+l1*i)
        x = Xaxis[i]
        Yaxis.append(eval(function))

    for i in range(n):
        l = math.sqrt((Xaxis[i+1]-Xaxis[i])*(Xaxis[i+1]-Xaxis[i])+(Yaxis[i+1]-Yaxis[i])*(Yaxis[i+1]-Yaxis[i]))
        pole += (abs(Yaxis[i])+abs(Yaxis[i+1]))*l*math.pi
    
    pole = '{:.4f}'.format(pole)
    return pole