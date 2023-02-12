import matplotlib.pyplot as plt  
import numpy as np

xpoints = np.array([0, 6]) # Uřčí body X
ypoints = np.array([0, 250]) # Určí body Y

Xpoints = np.array([0, 10])
Ypoints = np.array([0, 50])

xp = np.array([3, 7])
yp = np.array([0, 90])

y1 = np.array([50, 120, 30, 70]) # Můžeme mít vícero bodů

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 1) # Vytvoří další tabulku 1.číslo = počet řad; 2.číslo = počet sloupců; 3.číslo = číslo tabulky
plt.plot(x,y) # první tabulka

plt.subplot(1, 2, 2) 

plt.plot(xpoints, ypoints) # Udává nám jak bude finální graf vypadat (zde se jedná o pouhou čáru)
plt.plot(Xpoints, Ypoints, ls=':') # Dále můžeme měnit i styl pomocí linestyle či zkráceně ls (zde se jedná o tečkovanou čáru)
plt.plot(xp, yp, color = 'r') # Můžeme měnit i barvu (r = red = červená)
plt.plot(y1) # Stačí i jedna souřadnice
#Druhá tabulka




plt.title("Titulek") # Přidá titulek 
plt.xlabel("Podtitulek") # Přidá podtitulek souřadnici X (pro bod y = plt.ylabel)
