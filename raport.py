from datetime import datetime
import os
import bryly

now = datetime.now()
now = now.strftime("%d/%m/%Y %H:%M:%S")

os.system('python plt.py')

file=open("raport.html", "w", encoding="utf-8")
html = ""
html += f"<!DOCTYPE html><html lang=\"pl\"><head><meta charset=\"utf-8\"><link rel=\"stylesheet\" href=\"style.css\"></head>"
html += f"<body><h1>Raport z dnia: {now}</h1>"
html += "<h2>Dane wejściowe: </h2>"
html += f"<table><tr><td><b>Funkcja: </b></td><td>{bryly.func}</td></tr>"
html += f"<td><b>Początek przedziału:</b></td><td>{bryly.a}</td></tr>"
html += f"<td><b>Koniec przedziału:</b></td><td>{bryly.b}</td></tr> "
html += f"<td><b>Ilość częsci na które będziemy dzielić przedział:</b></td><td>{bryly.n}</td></tr></table>"
html += "<h2>Dane wyjściowe: </h2>"
html += f"<table><tr><td><b>Przybliżone pole powierzchni bocznej bryły:</b></td> <td>{bryly.algorithm(bryly.func)}</td></tr></table>"
html += f"<img src=\"Plot.png\", alt=\"Graph\">"
html += "</body>"
html += "</html>"

file.write(html)
file.close()

file2 = open("outputdata.txt", "w")
file2.write(str(bryly.algorithm(bryly.func)))
file2.close()