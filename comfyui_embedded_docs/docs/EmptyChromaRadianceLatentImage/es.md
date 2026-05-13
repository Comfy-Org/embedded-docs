> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/es.md)

El nodo EmptyChromaRadianceLatentImage crea una imagen latente en blanco con dimensiones específicas para su uso en flujos de trabajo de croma radiancia. Genera un tensor relleno de ceros que sirve como punto de partida para operaciones en el espacio latente. El nodo permite definir el ancho, alto y tamaño de lote de la imagen latente vacía.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `ancho` | INT | Sí | 16 a MAX_RESOLUTION | El ancho de la imagen latente en píxeles (valor predeterminado: 1024, debe ser divisible entre 16) |
| `alto` | INT | Sí | 16 a MAX_RESOLUTION | El alto de la imagen latente en píxeles (valor predeterminado: 1024, debe ser divisible entre 16) |
| `tamaño_lote` | INT | No | 1 a 4096 | La cantidad de imágenes latentes a generar en un lote (valor predeterminado: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `samples` | LATENT | El tensor de imagen latente vacía generado con las dimensiones especificadas |

---
**Source fingerprint (SHA-256):** `f2bc90a236f91e0161142f5242647d15adc8a10c57c920d2eb97e87040ac99d4`
