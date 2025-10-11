> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/es.md)

El nodo ImageYUVToRGB convierte imágenes del espacio de color YUV al espacio de color RGB. Toma tres imágenes de entrada separadas que representan los canales Y (luma), U (proyección azul) y V (proyección roja) y las combina en una única imagen RGB utilizando conversión de espacio de color.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `Y` | IMAGE | Sí | - | La imagen de entrada del canal Y (luminancia) |
| `U` | IMAGE | Sí | - | La imagen de entrada del canal U (proyección azul) |
| `V` | IMAGE | Sí | - | La imagen de entrada del canal V (proyección roja) |

**Nota:** Las tres imágenes de entrada (Y, U y V) deben proporcionarse juntas y deben tener dimensiones compatibles para una conversión adecuada.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La imagen RGB convertida |