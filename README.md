# Two-Body Simulation 🌍🌕

Simulación numérica del problema gravitacional de dos cuerpos en 2D usando Python.

## Descripción

Este proyecto implementa la simulación del movimiento de dos cuerpos bajo su atracción gravitacional mutua. Se pueden comparar tres métodos de integración numérica diferentes y visualizar las órbitas y la conservación de energía.

## Estructura del proyecto
```
2-cossos/
├── main.py            # Script principal de simulación
├── two_body.py        # Física: aceleración y energía
├── integrators.py     # Métodos de integración numérica
├── plots.py           # Gráficos y animación
├── requirements.txt   # Librerías necesarias
├── examples/
│   └── demo.ipynb     # Notebook de demostración
└── README.md
```

## Instalación
```bash
pip install -r requirements.txt
```

## Uso

1. Abre `main.py` y ajusta los parámetros iniciales:
   - `m1, m2`: masas de los cuerpos
   - `r1, r2`: posiciones iniciales
   - `v1, v2`: velocidades iniciales
   - `dt`: paso de tiempo
   - `N`: número de pasos
   - `integrador`: método de integración

2. Ejecuta:
```bash
python main.py
```

## Integradores disponibles

| Integrador | Precisión | Velocidad | Conserva energía |
|------------|-----------|-----------|-----------------|
| `euler_step` | Baja | Alta | No |
| `verlet_step` | Media | Alta | Sí (aprox.) |
| `rk4_step` | Alta | Media | Sí |

## Ejemplos de condiciones iniciales

**Órbita circular:**
```python
r1 = np.array([1.0, 0.0])
r2 = np.array([-1.0, 0.0])
v1 = np.array([0.0, 0.5])
v2 = np.array([0.0, -0.5])
```

**Órbita elíptica:**
```python
r1 = np.array([1.0, 0.0])
r2 = np.array([-1.0, 0.0])
v1 = np.array([0.0, 0.3])
v2 = np.array([0.0, -0.3])
```

**Planeta-estrella:**
```python
m1, m2 = 10.0, 1.0
r1 = np.array([0.0, 0.0])
r2 = np.array([2.0, 0.0])
v1 = np.array([0.0, 0.1])
v2 = np.array([0.0, -1.0])
```

## Resultados

- Trayectorias de ambos cuerpos en 2D
- Gráfica de energía total para verificar conservación
- Animación de las órbitas en tiempo real