> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/es.md)

El nodo ImageYUVToRGB convierte imágenes del espacio de color YUV al espacio de color RGB. Toma tres imágenes de entrada separadas que representan los canales Y (luma), U (proyección azul) y V (proyección roja) y las combina en una sola imagen RGB mediante conversión de espacio de color.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `Y` | IMAGE | Sí | - | Imagen de entrada del canal Y (luminancia) |
| `U` | IMAGE | Sí | - | Imagen de entrada del canal U (proyección azul) |
| `V` | IMAGE | Sí | - | Imagen de entrada del canal V (proyección roja) |

**Nota:** Las tres imágenes de entrada (Y, U y V) deben proporcionarse juntas y deben tener dimensiones compatibles para una conversión adecuada.

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `output` | IMAGE | La imagen RGB convertida |

---
**Source fingerprint (SHA-256):** `ee160be21fce75b3a3e41e25dc1cb0b20305383ff26f9698f07b93d42f98c64f`
