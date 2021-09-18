
import numpy as np
import matplotlib.pyplot as plt

oil_1p_terrestre_aguas_omeras = np.array([1730.09, 4389.64])
labels = ["Terrestre", "Aguas someras"]

fig, ax = plt.subplots(1, figsize=(10, 5))
myexplode = [0.1, 0.1]
mycolor = ['#ba9f85', '#94b8d7']

plt.pie(oil_1p_terrestre_aguas_omeras, labels = labels, explode = myexplode, autopct='%1.2f%%', shadow = True, colors = mycolor)
plt.legend()
#-------------------------------------------------------------------------------------------------
gas_1p_terrestre_aguas_omeras = np.array([6566.2, 3071.33, 343.43])
labels = ["Terrestre", "Aguas someras", "Aguas profundas"]

fig, ax = plt.subplots(1, figsize=(10, 5))
myexplode = [0.1, 0.1, 0.1]
mycolor = ['#ba9f85', '#94b8d7', '#557996']

plt.pie(gas_1p_terrestre_aguas_omeras, labels = labels, explode = myexplode, autopct='%1.2f%%', shadow = True, colors = mycolor)
plt.legend()
#-----------------------------------------RESERVAS 1P DE PETRÓLEO POR PROVINCIA--------------------------------------------------------
oil_provincias_p1 = np.array([281.26, 828.38, 4997.7, 13])
labels = [ "Veracruz", "Tampico-Misantla", "Cuenca del sureste", "Otros"]

fig, ax = plt.subplots(1, figsize=(10, 5))
myexplode = [0.1, 0.1, 0.1, 0.1]
mycolors = ['#2CA02C', '#1F77B4', '#FF7F0E', 'r']

plt.pie(oil_provincias_p1, labels = labels, explode = myexplode, autopct='%1.2f%%', colors = mycolors)
plt.legend()
#-----------------------------------------RESERVAS 1P DE PETRÓLEO POR CONTRATO--------------------------------------------------------
oil_contratos_p1 = np.array([912.21, 29.34, 5178.17])
labels = ["Contratos", "Sin asignar", "Asignaciones"]

fig, ax = plt.subplots(1, figsize=(10, 5))
myexplode = [0.1, 0.1, 0.1]
mycolors = ['#2CA02C', '#1F77B4', '#FF7F0E', 'r']

plt.pie(oil_contratos_p1, labels = labels, explode = myexplode, autopct='%1.2f%%', colors = mycolors)
plt.legend()
#-----------------------------------------RESERVAS 1P DE GAS POR PROVINCIA--------------------------------------------------------
gas_provincias_p1 = np.array([1158.48, 4795.51, 343.43,1313.18, 2259.48, 110.9])
labels = ["Burgos", "Cuenca del sureste", "Golfo de México profundo", "Tampico misantla", "Veracruz", "Otros"]

fig, ax = plt.subplots(1, figsize=(10, 5))
myexplode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

plt.pie(gas_provincias_p1, labels = labels, explode = myexplode, autopct='%1.2f%%')
plt.legend()
#-----------------------------------------RESERVAS 1P DE GAS POR CONTRATO--------------------------------------------------------
gas_contratos_p1 = np.array([951.22, 8803.2, 226.54])
labels = ["Contratos", "Asignaciones", "Sin asignar"]

fig, ax = plt.subplots(1, figsize=(10, 5))
myexplode = [0.1, 0.1, 0.1]

plt.pie(gas_contratos_p1, labels = labels, explode = myexplode, autopct='%1.2f%%')
plt.legend()

plt.show()