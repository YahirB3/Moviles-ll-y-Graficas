import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Dibujar el círculo
circulo = plt.Circle((0, 2.5), 2, edgecolor='pink', facecolor='pink', linewidth=2)
ax.add_patch(circulo)

# Ojo izquierdo
circulo = plt.Circle((-1, 2.5), 0.5, edgecolor='black', facecolor='white', linewidth=1)
ax.add_patch(circulo)

# Ojo izquierdo pupila
circulo = plt.Circle((-1, 2.5), 0.2, edgecolor='black', facecolor='black', linewidth=1)
ax.add_patch(circulo)


# Ojo derecha pupila
circulo = plt.Circle((1, 2.5), 0.5, edgecolor='black', facecolor='white', linewidth=1)
ax.add_patch(circulo)


# Ojo derecho
circulo = plt.Circle((1, 2.5), 0.2, edgecolor='black', facecolor='black', linewidth=1)
ax.add_patch(circulo)

# Dibujar el sombrero 
x = [-2.5, 0, 2.5, -2]  
y = [4, 8, 4, 4]    
ax.fill(x, y, 'green',  edgecolor='black', linewidth=2)  

# Dibujar el torso 
body_x = -1.5  
body_y = -3    
body_width = 3  
body_height = 4  
ax.add_patch(plt.Rectangle((body_x, body_y), body_width, body_height, edgecolor='black', facecolor='blue', linewidth=2))

# brazo izquierdo 
body_x = -3
body_y = -3.1    
body_width = 1.5 
body_height = 4  
ax.add_patch(plt.Rectangle((body_x, body_y), body_width, body_height, edgecolor='black', facecolor='pink', linewidth=1))

# brazo derecho 
body_x = 3
body_y = -3.1    
body_width = -1.5 
body_height = 4  
ax.add_patch(plt.Rectangle((body_x, body_y), body_width, body_height, edgecolor='black', facecolor='pink', linewidth=1))

# pierna izquierda 
body_x = -1.5
body_y = -6.5    
body_width = 1.5 
body_height = 3.5  
ax.add_patch(plt.Rectangle((body_x, body_y), body_width, body_height, edgecolor='black', facecolor='#A0522D', linewidth=1))

# pierna derecha 
body_x = 1.5
body_y = -6.5    
body_width = -1.5 
body_height = 3.5  
ax.add_patch(plt.Rectangle((body_x, body_y), body_width, body_height, edgecolor='black', facecolor='#A0522D', linewidth=1))

#boca 
ax.plot([-1.15, 1.15], [1.5, 1.5], color='black', linewidth=1.5)

#nariz
x = [-.5, 0, .5, -.5]  
y = [1.75, 2.5, 1.75, 1.75]    
ax.fill(x, y, 'pink',  edgecolor='black', linewidth=1)  


ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')  # Mantiene la proporción 1:1


plt.grid(True)
plt.show()
