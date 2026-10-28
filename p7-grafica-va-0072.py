import matplotlib.pyplot as plt
import numpy as np 
#catherine eileen huerta rascon NC = 0072
#datos
no_lista =[1,2,3,17,48]
califa_ml=[20,30,80,100,90]
califa_va=[70,90,60,90,100]

plt.plot(no_lista,califa_ml, label="califa ML")
plt.plot(no_lista,califa_va, label="califa VA")

plt.title("calificaciones materias---- 0072")
plt.xlabel("numero de lista----- 0072")
plt.ylabel("calificaciones---- 0072")
plt.legend()
plt.show()
print("catherine eileen huerta rascon ")