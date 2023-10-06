import numpy as np

vector = np.zeros(20,int)
i = 0
x = 20
tamaño = 20 
for i in range (tamaño):
    vector[i]= x
    x = x - 1 
    i = i + 1

print("Vector")
print(vector)
