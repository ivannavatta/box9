# box9

Herramienta de consola para evaluar empleados, inspirada en la **matriz 9-box** que usan las áreas de Recursos Humanos para cruzar el desempeño actual de una persona con su potencial de crecimiento. Cada empleado se autoevalúa del 1 al 5 en performance y en potencial, puede actualizar sus datos cuando quiera y el programa calcula quién tiene el mejor puntaje.

<p align="center">
  <img src="docs/demo.svg" alt="Demo de box9: alta de dos empleados, validación de una entrada inválida, actualización de datos y cálculo del mejor empleado" width="760">
</p>

> Proyecto académico, UADE 2025. Escrito en Python, solo con la librería estándar.

## Funcionalidades

| Opción | Qué hace |
| --- | --- |
| 1. Mostrar empleados | Lista los empleados cargados con su auto-performance y auto-potencial |
| 2. Agregar empleado | Alta con nombre y apellido y las dos calificaciones (1 a 5). No permite nombres repetidos |
| 3. Actualizar datos | Busca al empleado por nombre y deja cambiar los dos campos o solo uno |
| 4. Mejor empleado | Calcula el puntaje de cada uno (`performance × potencial`) y muestra el más alto |
| 5. Salir | Termina el programa |

## Cómo ejecutarlo

Requiere **Python 3.6 o superior**. No usa dependencias externas.

```bash
git clone https://github.com/ivannavatta/box9.git
cd box9
python main.py
```

Los datos viven en memoria mientras el programa está abierto: al salir se pierden.

## Conceptos aplicados

- **Listas paralelas:** `names`, `auto_performance` y `auto_potential` comparten el índice de cada empleado.
- **Validación de entradas:** `ask_option` usa `try/except ValueError` y una lista de opciones válidas, así que el programa vuelve a preguntar en lugar de cortarse si se escriben letras o números fuera de rango.
- **Búsqueda lineal** sin distinguir mayúsculas (`find_employed`), reutilizada para evitar duplicados y para actualizar datos.
- **Acumulador de máximo** para encontrar el mejor puntaje en una sola pasada.
- **Menú con bucle** y funciones separadas por responsabilidad.

## Equipo

- [Ivan Navatta](https://github.com/ivannavatta)
- [Baltazar García](https://github.com/baltaagarcia)
