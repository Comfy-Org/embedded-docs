# ImagenLatenteChromaRadianceVacía

El nodo EmptyChromaRadianceLatentImage crea una imagen latente en blanco con dimensiones específicas para su uso en flujos de trabajo de croma radiancia. Genera un tensor relleno de ceros que sirve como punto de partida para operaciones en el espacio latente. El nodo permite definir el ancho, alto y tamaño de lote de la imagen latente vacía.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho de la imagen latente en píxeles (valor predeterminado: 1024, debe ser divisible entre 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | El alto de la imagen latente en píxeles (valor predeterminado: 1024, debe ser divisible entre 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `tamaño_lote` | La cantidad de imágenes latentes a generar en un lote (valor predeterminado: 1) | INT | No | 1 a 4096 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `samples` | El tensor de imagen latente vacía generado con las dimensiones especificadas | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/es.md)

---
**Source fingerprint (SHA-256):** `f2bc90a236f91e0161142f5242647d15adc8a10c57c920d2eb97e87040ac99d4`
