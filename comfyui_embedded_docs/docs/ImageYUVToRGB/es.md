# ImageYUVToRGB

El nodo ImageYUVToRGB convierte imágenes del espacio de color YUV al espacio de color RGB. Toma tres imágenes de entrada separadas que representan los canales Y (luma), U (proyección azul) y V (proyección roja) y las combina en una sola imagen RGB mediante conversión de espacio de color.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `Y` | Imagen de entrada del canal Y (luminancia) | IMAGE | Sí | - |
| `U` | Imagen de entrada del canal U (proyección azul) | IMAGE | Sí | - |
| `V` | Imagen de entrada del canal V (proyección roja) | IMAGE | Sí | - |

**Nota:** Las tres imágenes de entrada (Y, U y V) deben proporcionarse juntas y deben tener dimensiones compatibles para una conversión adecuada.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `output` | La imagen RGB convertida | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/es.md)

---
**Source fingerprint (SHA-256):** `ee160be21fce75b3a3e41e25dc1cb0b20305383ff26f9698f07b93d42f98c64f`
