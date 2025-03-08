import matplotlib.pyplot as plt
import numpy as np
import time 

start_time = time.time() 
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)

# (y=mx+b)
#m=(y2-y1)/(x2-x1)
x1, y1 = -10, -5  
x2, y2 = 10, 8    
m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1 

x_vals = np.linspace(-15, 15, 2)
y_vals = m * x_vals + b             

ax.plot(x_vals, y_vals, 'r-', label=f'y = {m:.2f}x + {b:.2f}')
ax.plot([x1, x2], [y1, y2], 'bo', label="Puntos dados")

end_time = time.time()
elapsed_time = end_time - start_time
print("tiempo de la recta: " , elapsed_time)
plt.grid()
plt.title('Recta')
plt.show()

#Circulo
start_time = time.time() 
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)

#ecuación (x-a)^2 + (y-b)^2 = r^2
cx, cy, r = 0, 0, 8
for angle in np.linspace(0, 2*np.pi, 300):
    x = cx + r * np.cos(angle)
    y = cy + r * np.sin(angle)
    ax.plot(x, y, 'bo', markersize=2)

end_time = time.time()
elapsed_time = end_time - start_time

print("tiempo del circulo: " , elapsed_time)
plt.title("Circulo")
plt.grid()
plt.show()

#hiperbola
start_time = time.time() 
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
cx, cy, r = 0, 0, 8

# (x/a)^2 - (y/b)^2 = 1
a, b = 5, 3
for x in np.linspace(-10, -a, 200):
    y = b * np.sqrt((x**2 / a**2) - 1)
    ax.plot(x, y, 'ro', markersize=2)
    ax.plot(x, -y, 'ro', markersize=2)
for x in np.linspace(a, 10, 200):
    y = b * np.sqrt((x**2 / a**2) - 1)
    ax.plot(x, y, 'ro', markersize=2)
    ax.plot(x, -y, 'ro', markersize=2)

end_time = time.time()
elapsed_time = end_time - start_time
print("tiempo del hiperbola: " , elapsed_time)
plt.title("hiperbola")
plt.grid()
plt.show()

#elipse

start_time = time.time() 
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
cx, cy, r = 0, 0, 8

#(x/a)^2 + (y/b)^2 = 1
a, b = 12, 6
for angle in np.linspace(0, 2*np.pi, 300):
    x = cx + a * np.cos(angle)
    y = cy + b * np.sin(angle)
    ax.plot(x, y, 'go', markersize=2)

end_time = time.time()
elapsed_time = end_time - start_time

print("tiempo de la elipse: " , elapsed_time)
plt.title("elipse")
plt.grid()
plt.show()
