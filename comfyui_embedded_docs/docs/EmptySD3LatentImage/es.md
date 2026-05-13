> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/es.md)

El nodo EmptySD3LatentImage crea un tensor de imagen latente en blanco formateado específicamente para modelos Stable Diffusion 3. Genera un tensor relleno de ceros con las dimensiones y estructura correctas que esperan los pipelines de SD3. Se utiliza comúnmente como punto de partida para flujos de trabajo de generación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `ancho` | INT | Sí | 16 a MAX_RESOLUTION (paso: 16) | El ancho de la imagen latente de salida en píxeles (predeterminado: 1024) |
| `altura` | INT | Sí | 16 a MAX_RESOLUTION (paso: 16) | La altura de la imagen latente de salida en píxeles (predeterminado: 1024) |
| `tamaño_del_lote` | INT | Sí | 1 a 4096 | La cantidad de imágenes latentes a generar en un lote (predeterminado: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `LATENT` | LATENT | Un tensor latente que contiene muestras en blanco con dimensiones compatibles con SD3. El tensor tiene 16 canales y está reducido espacialmente por un factor de 8 en comparación con el ancho y alto de entrada. |

---
**Source fingerprint (SHA-256):** `21eb5b6385b9b0db95d48fa2f4b85eafe44f865af11ee194945ab7ffe54b6acc`
