# Rodin 3D Gen-2.5 - Texto a 3D

## Descripción general

Genera un modelo 3D a partir de un texto de indicación usando la API Rodin Gen-2.5. Puedes elegir entre diferentes modos de calidad (Fast, Regular o Extreme-High) para equilibrar la velocidad de generación y la calidad de salida.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texto de indicación para el modelo 3D. | STRING | Sí | 1 a 1024 caracteres |
| `mode` | El modo de calidad y velocidad de generación. "Fast" es el más rápido; "Extreme-High" produce la mayor calidad, pero tarda más. | COMBO | Sí | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `material` | El estilo de material para el modelo 3D generado. | COMBO | Sí | `"PBR"`<br>`"Matte"`<br>`"Shiny"` |
| `geometry_file_format` | El formato de archivo para el modelo 3D de salida. | COMBO | Sí | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `texture_mode` | Modo de generación de texturas. "None" no produce texturas; "Generated" crea texturas estándar; "Generated+HD" crea texturas de alta definición. | COMBO | Sí | `"None"`<br>`"Generated"`<br>`"Generated+HD"` |
| `seed` | Semilla aleatoria para resultados reproducibles. Usar la misma semilla con las mismas entradas producirá la misma salida. | INT | Sí | 0 a 2147483647 |
| `TAPose` | Indica si se debe aplicar la pose en T (brazos extendidos) al modelo generado. | BOOLEAN | Sí | True / False |
| `hd_texture` | Indica si se deben generar texturas de alta definición para el modelo. | BOOLEAN | Sí | True / False |
| `texture_delight` | Indica si se debe aplicar realce de texturas (calidad de textura mejorada) al modelo. | BOOLEAN | Sí | True / False |
| `addon_highpack` | Indica si se debe generar una versión de alta densidad de polígonos del modelo además de la estándar. | BOOLEAN | Sí | True / False |
| `bbox_width` | El ancho de la caja delimitadora en unidades de mundo. | INT | Sí | 1 a 1000 |
| `bbox_height` | La altura de la caja delimitadora en unidades de mundo. | INT | Sí | 1 a 1000 |
| `bbox_length` | La longitud de la caja delimitadora en unidades de mundo. | INT | Sí | 1 a 1000 |
| `height_cm` | La altura del modelo generado en centímetros. | INT | Sí | 1 a 300 |

**Nota:** El parámetro `prompt` debe tener entre 1 y 1024 caracteres. El parámetro `seed` tiene como valor predeterminado 0 (aleatorio) si no se especifica.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `model_file` | El archivo del modelo 3D generado en el formato especificado. | FILE3DANY |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/es.md)

---
**Source fingerprint (SHA-256):** `95d5faa36298f09f0ae4dcda95dfd8913ebb393bb5934ae2c4622acfe79c85d6`
