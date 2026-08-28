# EmptyLatentHunyuan3Dv2

El nodo EmptyLatentHunyuan3Dv2 crea tensores latentes vacíos formateados específicamente para los modelos de generación 3D Hunyuan3Dv2. Genera espacios latentes vacíos con las dimensiones y la estructura correctas que requiere la arquitectura Hunyuan3Dv2, lo que permite iniciar flujos de trabajo de generación 3D desde cero. El nodo produce tensores latentes rellenos de ceros que sirven como base para los procesos posteriores de generación 3D.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `resolución` | La dimensión de resolución del espacio latente (por defecto: 3072) | INT | Sí | 1 - 8192 |
| `tamaño_del_lote` | El número de imágenes latentes en el lote (por defecto: 1) | INT | Sí | 1 - 4096 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `LATENT` | Devuelve un tensor latente que contiene muestras vacías etiquetadas con el tipo "hunyuan3dv2", formateado para la generación 3D de Hunyuan3Dv2 | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/es.md)

---
**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`
