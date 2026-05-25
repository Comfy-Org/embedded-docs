> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/es.md)

# Descripción General

Este nodo reduce las costuras visibles en imágenes generadas por el modelo HiDream-O1 promediando la salida del modelo en múltiples posiciones de cuadrícula desplazadas durante la parte final del proceso de muestreo. Funciona ejecutando el modelo varias veces con alineaciones de imagen ligeramente diferentes y combinando los resultados, lo que ayuda a cancelar los artefactos en forma de cuadrícula que pueden aparecer en los bordes de los parches.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-------------|-------------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo HiDream-O1 al que se aplicará el suavizado de costuras. |
| `porcentaje_inicio` | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) | El progreso del muestreo (0=inicio, 1=fin) en el que el efecto de suavizado se ACTIVA (predeterminado: 0.8). |
| `porcentaje_fin` | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) | El progreso del muestreo en el que el efecto de suavizado se DESACTIVA (predeterminado: 1.0). |
| `patrón` | COMBO | Sí | `"single_shift"`<br>`"symmetric"` | La disposición de las posiciones de cuadrícula desplazadas. `single_shift`: una pasada en la cuadrícula natural de parches más otras desplazadas. `symmetric`: todas las pasadas están fuera de la cuadrícula, con desplazamientos divididos alrededor del origen (predeterminado: `"single_shift"`). |
| `pasadas` | COMBO | Sí | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` | El número de pasadas (ejecuciones del modelo) por paso controlado. `2` o `4` son cantidades fijas. `ramp_2_4` y `ramp_2_4_8` aumentan el número de pasadas a medida que el muestreo se acerca al final, proporcionando más suavizado donde las costuras son más visibles (predeterminado: `"2"`). |
| `mezcla` | COMBO | Sí | `"average"`<br>`"window"`<br>`"median"` | El método utilizado para combinar los resultados de cada pasada. `average`: media de igual peso de todas las pasadas. `window`: utiliza una ventana Hann para dar más peso al centro de cada pasada, reduciendo artefactos en los bordes. `median`: toma la mediana por píxel, lo que puede rechazar pasadas atípicas causadas por envolvente (predeterminado: `"average"`). |
| `fuerza` | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) | Controla la interpolación entre la salida original del modelo (0.0) y el resultado completamente suavizado (1.0) (predeterminado: 1.0). |

**Nota sobre Restricciones de Parámetros:**
- El efecto de suavizado no se aplicará si `strength` es 0.0 o menor, o si `end_percent` es menor o igual que `start_percent`.
- Las opciones de rampa del parámetro `passes` (`ramp_2_4`, `ramp_2_4_8`) solo tienen sentido cuando `start_percent` y `end_percent` definen un rango, ya que el número de pasadas aumenta a medida que el muestreo progresa a través de ese rango.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|-------------|-------------|
| `modelo` | MODEL | El modelo modificado con el envoltorio de suavizado de costuras aplicado. |

---
**Source fingerprint (SHA-256):** `f4d1a617d88f880dcae3afda25699333df023d7b4ec13a22a73512713d6ef18c`
