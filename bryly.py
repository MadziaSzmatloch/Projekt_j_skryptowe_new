import math
import matplotlib.pyplot as plt

file = open("inputdata.txt", "r")

lines = file.readlines()
data = []
for line in lines:
    data.append(line.strip("\n"))

func = data[0]
a = float(data[1])
b = float(data[2])
n = int(data[3])


def algorythm(function):
    Xaxis = []
    Yaxis = []
    l1 = (abs(a)+abs(b))/n
    pole = 0
    for i in range(n+1):
        Xaxis.append(a+l1*i)
        x = Xaxis[i]
        Yaxis.append(float(eval(function)))
    plt.plot(Xaxis, Yaxis) 
    plt.ylabel("Wartości y")
    plt.xlabel("Argumenty x")
    plt.title("Wykres fukncji f(x) = " + func)
    plt.grid(True)
    plt.savefig("Plot.png") 
    

    for i in range(n):
        l = math.sqrt((Xaxis[i+1]-Xaxis[i])*(Xaxis[i+1]-Xaxis[i])+(Yaxis[i+1]-Yaxis[i])*(Yaxis[i+1]-Yaxis[i]))
        pole += (abs(Yaxis[i])+abs(Yaxis[i+1]))*l*math.pi
    
    pole = '{:.4f}'.format(pole)
    return pole

algorythm(func)
file2 = open("outputdata.txt", "w")
file2.write(str(algorythm(func)))
file2.close()



