import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def simularProyectil3D(v0, elevacion, azimut, spin=0, g=9.81, num_puntos=500):
    """
    Simula y grafica la trayectoria de un proyectil en 3D considerando gravedad y efecto Magnus (spin).
    :param v0: Velocidad inicial (m/s)
    :param elevacion: Ángulo de elevación (grados, respecto a la horizontal)
    :param azimut: Ángulo azimutal (grados, 0=X+, 90=Y+)
    :param spin: Magnitud del spin (rad/s) para efecto Magnus
    :param g: Aceleración gravitatoria (m/s^2)
    :param num_puntos: Número de puntos para graficar
    """

    # Conversión de ángulos a radianes
    elev = np.radians(elevacion)
    azim = np.radians(azimut)

    # Componentes de velocidad inicial
    v0x = v0 * np.cos(elev) * np.cos(azim)
    v0y = v0 * np.cos(elev) * np.sin(azim)
    v0z = v0 * np.sin(elev)

    # Tiempo total de vuelo (usando el eje Z, vertical)
    t_total = (2 * v0z) / g if g != 0 else 2  # Para que no falle si g=0

    # Puntos de tiempo
    t = np.linspace(0, t_total, num_puntos)

    # Parámetros del efecto Magnus (simplificado)
    # Fuerza Magnus ~ k * (v × w), suponemos w = [0, 0, spin]
    # Aceleración Magnus en XY perpendicular a v_xy
    k = 0.03  # constante ajustable (depende de objeto y aire)
    v_xy = np.array([v0x, v0y])
    if np.linalg.norm(v_xy) != 0:
        mag_dir = np.array([-v0y, v0x]) / np.linalg.norm(v_xy)  # dirección perpendicular a v_xy
    else:
        mag_dir = np.array([0,0])

    # Aceleración Magnus constante para demostración
    a_mag = k * spin * np.linalg.norm(v_xy)
    ax_mag = a_mag * mag_dir[0]
    ay_mag = a_mag * mag_dir[1]

    # Posiciones en el tiempo
    x = v0x * t + 0.5 * ax_mag * t**2
    y = v0y * t + 0.5 * ay_mag * t**2
    z = v0z * t - 0.5 * g * t**2

    # Solo mostramos hasta que toca el suelo (z >= 0)
    mask = z >= 0
    x, y, z = x[mask], y[mask], z[mask]

    # Graficar en 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label=f'Trayectoria (v0={v0} m/s, elev={elevacion}°, azim={azimut}°, spin={spin})')
    ax.scatter([x[0]], [y[0]], [z[0]], color='green', s=60, label="Inicio")
    ax.scatter([x[-1]], [y[-1]], [z[-1]], color='red', s=60, label="Fin")
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (Altura, m)')
    ax.set_title('Simulación de Movimiento en 3D con Efecto Magnus')
    ax.legend()
    plt.show()

# Parámetros de ejemplo
v0 = 25        # Velocidad inicial (m/s)
elevacion = 45 # Ángulo de elevación (grados)
azimut = 30    # Ángulo azimutal (grados)
spin = 20      # Spin (rad/s, ajusta para ver el efecto)

# Ejecutar simulación 3D
simularProyectil3D(v0, elevacion, azimut, spin)


