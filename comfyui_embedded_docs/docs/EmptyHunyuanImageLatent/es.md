# ImagenLatenteHunyuanVacía

El nodo EmptyHunyuanImageLatent crea un espacio latente vacío (relleno de ceros) para los modelos de generación de imágenes Hunyuan. Genera un latente inicial en blanco con el ancho, alto y tamaño de lote especificados, que puede pasarse a los nodos posteriores del flujo de trabajo. El tensor latente tiene 64 canales, y sus dimensiones espaciales son el ancho y el alto divididos cada uno entre 32.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `ancho` | El ancho de la imagen latente generada en píxeles (por defecto: 2048, paso: 32) | INT | Sí | 64 a MAX_RESOLUTION |
| `alto` | El alto de la imagen latente generada en píxeles (por defecto: 2048, paso: 32) | INT | Sí | 64 a MAX_RESOLUTION |
| `tamaño_lote` | El número de muestras latentes a generar en un lote (por defecto: 1) | INT | Sí | 1 a 4096 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `LATENT` | Un tensor latente vacío con 64 canales y dimensiones de alto ÷ 32 por ancho ÷ 32, listo para el procesamiento de imágenes Hunyuan | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/es.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
