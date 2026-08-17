# Suavizado de Costuras de Parches HiDream-O1

## Resumen

Este nodo reduce las costuras visibles en las imágenes generadas por el modelo HiDream-O1 al promediar la salida del modelo en varias posiciones desplazadas de la cuadrícula de parches durante la parte final del proceso de muestreo. Funciona ejecutando el modelo varias veces con alineaciones de imagen ligeramente diferentes y combinando los resultados, lo que ayuda a cancelar los artefactos de cuadrícula que pueden aparecer en los bordes de los parches.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo HiDream-O1 al que se le aplicará el envoltorio de suavizado de costuras. | MODEL | Sí | - |
| `start_percent` | Progreso del muestreo (0=inicio, 1=fin) en el que la mezcla se activa (predeterminado: 0.8). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `end_percent` | Progreso del muestreo en el que la mezcla se desactiva (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `pattern` | Disposición de desplazamiento. `single_shift`: una pasada en la cuadrícula de parches natural más otras desplazadas. `symmetric`: todas las pasadas fuera de la cuadrícula, con desplazamientos divididos alrededor del origen (predeterminado: `"single_shift"`). | COMBO | Sí | `"single_shift"`<br>`"symmetric"` |
| `passes` | Número de pasadas por paso activado. `2`/`4` = fijo. `ramp_*`: el número de pasadas aumenta a medida que el muestreo se acerca al final (más suavizado donde las costuras son más visibles) (predeterminado: `"2"`). | COMBO | Sí | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `blend` | `average`: media con pesos iguales. `window`: ponderación con ventana de Hann que favorece cada pasada lejos de los bordes de sus parches. `median`: mediana por píxel, rechaza las pasadas atípicas por ajuste envolvente (predeterminado: `"average"`). | COMBO | Sí | `"average"`<br>`"window"`<br>`"median"` |
| `strength` | Interpolación entre la predicción de la cuadrícula natural (0) y el resultado promediado (1) (predeterminado: 1.0). | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |

**Notas sobre las restricciones:**

- El efecto de suavizado no se aplica si `strength` es 0.0 o menor, o si `end_percent` es menor o igual que `start_percent`; en esos casos, el nodo devuelve el modelo sin cambios.
- Las opciones de rampa de `passes` (`ramp_2_4`, `ramp_2_4_8`) aumentan el número de pasadas a medida que el muestreo avanza hacia `end_percent` dentro del rango activado, por lo que solo tienen sentido cuando `start_percent` y `end_percent` definen un rango no vacío.
- El resultado promediado se combina con la salida del modelo solo lejos de los bordes de la imagen: una máscara mantiene la predicción original en la franja de 32 píxeles a lo largo de cada borde (con un difuminado de 4 píxeles), evitando la contaminación por ajuste envolvente causada por las pasadas desplazadas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con el envoltorio de suavizado de costuras de parches aplicado. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/es.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
