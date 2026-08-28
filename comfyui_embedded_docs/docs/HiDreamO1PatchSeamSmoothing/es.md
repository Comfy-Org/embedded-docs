# Suavizado de Costuras de Parches HiDream-O1

Este nodo reduce las costuras visibles en las imágenes generadas por el modelo HiDream-O1 al promediar la salida del modelo en múltiples posiciones desplazadas de la cuadrícula de parches durante la parte final del proceso de muestreo. Funciona ejecutando el modelo varias veces con alineaciones de imagen ligeramente diferentes y combinando los resultados, lo que ayuda a cancelar los artefactos similares a una cuadrícula que pueden aparecer en los bordes de los parches.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo HiDream-O1 al que se aplicará el suavizado de costuras. | MODEL | Sí | - |
| `porcentaje_inicio` | El progreso del muestreo (0=inicio, 1=fin) en el que el efecto de suavizado se activa (predeterminado: 0.8). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `porcentaje_fin` | El progreso del muestreo en el que el efecto de suavizado se desactiva (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `patrón` | La disposición de las posiciones de cuadrícula desplazadas. `single_shift`: una pasada en la cuadrícula de parches natural más otras desplazadas. `symmetric`: todas las pasadas están fuera de la cuadrícula, con desplazamientos divididos alrededor del origen (predeterminado: `"single_shift"`). | COMBO | Sí | `"single_shift"`<br>`"symmetric"` |
| `pasadas` | El número de pasadas (ejecuciones del modelo) por paso activado. `2` o `4` son recuentos fijos. `ramp_2_4` y `ramp_2_4_8` aumentan el número de pasadas a medida que el muestreo se acerca al final, proporcionando un mayor suavizado donde las costuras son más visibles (predeterminado: `"2"`). | COMBO | Sí | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `mezcla` | El método utilizado para combinar los resultados de cada pasada. `average`: media ponderada por igual de todas las pasadas. `window`: utiliza una ventana de Hann para dar más peso al centro de cada pasada, reduciendo los artefactos de borde. `median`: toma la mediana por píxel, que puede rechazar pasadas atípicas causadas por el efecto envolvente (predeterminado: `"average"`). | COMBO | Sí | `"average"`<br>`"window"`<br>`"median"` |
| `fuerza` | Controla la interpolación entre la salida original del modelo (0.0) y el resultado completamente suavizado (1.0) (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |

**Nota sobre las restricciones de los parámetros:**
- El efecto de suavizado no se aplicará si `strength` es 0.0 o menor, o si `end_percent` es menor o igual que `start_percent`. En esos casos, el nodo devuelve el modelo sin cambios.
- Las opciones de rampa del parámetro `passes` (`ramp_2_4`, `ramp_2_4_8`) solo tienen sentido cuando `start_percent` y `end_percent` definen un rango, ya que el número de pasadas aumenta a medida que el muestreo avanza a través de ese rango.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con el envoltorio de suavizado de costuras aplicado. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/es.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
