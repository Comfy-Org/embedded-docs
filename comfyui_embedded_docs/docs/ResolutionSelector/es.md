> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/es.md)

El nodo Selector de Resolución calcula el ancho y alto en píxeles de una imagen basándose en una relación de aspecto elegida y una resolución total objetivo en megapíxeles. Es útil para generar dimensiones consistentes para otros nodos, como el nodo Imagen Latente Vacía. Las dimensiones de salida siempre se redondean al múltiplo más cercano de 8.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `aspect_ratio` | COMBO | Sí | `"SQUARE"`<br>`"PORTRAIT_2_3"`<br>`"PORTRAIT_3_4"`<br>`"PORTRAIT_9_16"`<br>`"LANDSCAPE_3_2"`<br>`"LANDSCAPE_4_3"`<br>`"LANDSCAPE_16_9"` | La relación de aspecto para las dimensiones de salida (por defecto: `"SQUARE"`). |
| `megapixels` | FLOAT | Sí | 0.1 - 16.0 | Megapíxeles totales objetivo. 1.0 MP ≈ 1024×1024 para una relación de aspecto cuadrada (por defecto: 1.0). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `width` | INT | El ancho calculado en píxeles, que es un múltiplo de 8. |
| `height` | INT | El alto calculado en píxeles, que es un múltiplo de 8. |