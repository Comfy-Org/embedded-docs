> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/es.md)

El nodo ResizeAndPadImage redimensiona una imagen para que se ajuste a unas dimensiones específicas, manteniendo su relación de aspecto original. Escala la imagen proporcionalmente para que quepa dentro del ancho y alto objetivo, y luego añade relleno alrededor de los bordes para llenar el espacio restante. El color de relleno y el método de interpolación se pueden personalizar para controlar la apariencia de las áreas rellenas y la calidad del redimensionamiento.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se redimensionará y rellenará |
| `target_width` | INT | Sí | 1 a MAX_RESOLUTION | El ancho deseado de la imagen de salida (predeterminado: 512) |
| `target_height` | INT | Sí | 1 a MAX_RESOLUTION | La altura deseada de la imagen de salida (predeterminado: 512) |
| `padding_color` | COMBO | Sí | "white"<br>"black" | El color que se usará para las áreas de relleno alrededor de la imagen redimensionada (predeterminado: "white") |
| `interpolation` | COMBO | Sí | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" | El método de interpolación utilizado para redimensionar la imagen (predeterminado: "area") |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `image` | IMAGE | La imagen de salida redimensionada y rellenada |

---
**Source fingerprint (SHA-256):** `01566327d46043d1ff9ce404b4df8f49e853d0b01d07cc189fb843157dac1cac`
