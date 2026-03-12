import numpy as np

G = 1.0  # Constante gravitacional (puedes normalizarla a 1 para pruebas)

def compute_acceleration(r1, r2, m1, m2):
    """
    Calcula la aceleración de cada cuerpo debido a la gravedad mutua.
    
    Parámetros:
    r1, r2 : np.array de tamaño 2 -> posiciones de los cuerpos
    m1, m2 : float -> masas de los cuerpos
    
    Retorna:
    a1, a2 : np.array de tamaño 2 -> aceleraciones de los cuerpos
    """
    r12 = r2 - r1
    distance = np.linalg.norm(r12)
    
    if distance == 0:
        raise ValueError("Los cuerpos están superpuestos (distancia = 0)")
    
    force = G * m1 * m2 * r12 / distance**3
    a1 = force / m1
    a2 = -force / m2
    
    return a1, a2

def compute_energy(r1, r2, v1, v2, m1, m2):
    # Energía cinética
    Ek = 0.5 * m1 * np.dot(v1, v1) + 0.5 * m2 * np.dot(v2, v2)
    # Energía potencial
    distance = np.linalg.norm(r2 - r1)
    Ep = -G * m1 * m2 / distance
    return Ek + Ep