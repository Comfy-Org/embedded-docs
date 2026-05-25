> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Image/es.md)

# Descripción General

Este nodo genera un modelo 3D a partir de una a cinco imágenes de referencia utilizando la API de Rodin Gen-2.5. Puedes elegir entre los modos de calidad Rápido, Regular o Ultra-Alta para equilibrar la velocidad de generación y el costo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `images` | IMAGE | Sí | 1 a 5 imágenes | De una a cinco imágenes de entrada. La primera imagen se utiliza para los materiales cuando se proporcionan múltiples imágenes. |
| `mode` | COMBO | Sí | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` | El modo de calidad de generación. Los modos de mayor calidad producen mejores resultados pero tienen un costo más elevado. |
| `material` | COMBO | Sí | `"PBR"`<br>`"Matte"` | El tipo de material para el modelo 3D generado. |
| `geometry_file_format` | COMBO | Sí | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` | El formato de archivo de salida para la geometría del modelo 3D. |
| `texture_mode` | COMBO | Sí | `"Original"`<br>`"Clean"`<br>`"Style"` | El modo de generación de texturas. "Original" conserva las texturas de entrada, "Clean" las elimina y "Style" aplica una textura estilizada. |
| `seed` | INT | Sí | 0 a 2147483647 | Una semilla aleatoria para obtener resultados reproducibles. Usa la misma semilla para obtener la misma salida. |
| `TAPose` | BOOLEAN | Sí | Verdadero / Falso | Si se debe aplicar la pose T al modelo generado. |
| `hd_texture` | BOOLEAN | Sí | Verdadero / Falso | Si se debe generar un mapa de textura de alta definición. |
| `texture_delight` | BOOLEAN | Sí | Verdadero / Falso | Si se debe eliminar la iluminación de las imágenes de entrada antes de la generación de texturas. |
| `use_original_alpha` | BOOLEAN | Sí | Verdadero / Falso | Si se debe utilizar el canal alfa original de las imágenes de entrada. |
| `addon_highpack` | BOOLEAN | Sí | Verdadero / Falso | Si se debe generar una versión de alto poligonaje del modelo además de la estándar. |
| `bbox_width` | INT | Sí | 1 a 1000 | El ancho de la caja delimitadora para el modelo generado en centímetros. |
| `bbox_height` | INT | Sí | 1 a 1000 | La altura de la caja delimitadora para el modelo generado en centímetros. |
| `bbox_length` | INT | Sí | 1 a 1000 | La longitud de la caja delimitadora para el modelo generado en centímetros. |
| `height_cm` | INT | Sí | 1 a 300 | La altura del modelo generado en centímetros. |

**Nota sobre la cantidad de imágenes:** El nodo acepta entre 1 y 5 imágenes. Si proporcionas un lote de imágenes (por ejemplo, un lote de 4 imágenes), cada imagen del lote se trata como una imagen de entrada independiente. Proporcionar más de 5 imágenes generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `model_file` | FILE3D | El archivo de modelo 3D generado en el formato de geometría seleccionado. |

---
**Source fingerprint (SHA-256):** `65f755a2c3bd2317eb61c4681a406b51b06f960e36864d3602c3d03a44aa4878`
