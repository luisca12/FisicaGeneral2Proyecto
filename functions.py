import numpy as np
import matplotlib.pyplot as plt

def simular_proyectil(v0, angle, g=9.81, num_puntos=500):
    """
    Simula y grafica la trayectoria de un proyectil en 2D.
    :param v0: Velocidad inicial (m/s)
    :param angle: Ángulo de lanzamiento (grados)
    :param g: Aceleración gravitatoria (m/s^2)
    :param num_puntos: Número de puntos para graficar
    """
    # Convertir ángulo a radianes
    theta = np.radians(angle)
    
    # Calcular tiempo total de vuelo
    t_total = (2 * v0 * np.sin(theta)) / g
    
    # Generar puntos de tiempo
    t = np.linspace(0, t_total, num_puntos)
    
    # Calcular posiciones
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    
    # Encontrar alcance y altura máxima
    x_max = v0**2 * np.sin(2 * theta) / g
    y_max = (v0 * np.sin(theta))**2 / (2 * g)
    
    # Graficar trayectoria
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'Trayectoria (v0={v0} m/s, θ={angle}°)')
    plt.axhline(y_max, color='r', linestyle='--', label=f'Altura Máx: {y_max:.2f} m')
    plt.axvline(x_max, color='g', linestyle='--', label=f'Alcance: {x_max:.2f} m')
    plt.scatter([x_max], [0], color='g', marker='o')
    plt.scatter([x[np.argmax(y)]], [y_max], color='r', marker='o')
    plt.title('Simulación de Movimiento en 2D')
    plt.xlabel('Distancia (m)')
    plt.ylabel('Altura (m)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Parámetros iniciales
v0 = 10  # Velocidad inicial (m/s)
angle = 90  # Ángulo de lanzamiento (grados)

# Ejecutar simulación
simular_proyectil(v0, angle)

