> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/es.md)

## Descripción general

Genera un modelo 3D a partir de una descripción textual utilizando la API de Rodin Gen-2.5. Puedes elegir entre diferentes modos de calidad (Rápido, Normal o Ultra-Alto) para equilibrar la velocidad de generación y la calidad del resultado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | Máximo 2500 caracteres | Descripción textual del modelo 3D que deseas generar. |
| `modo` | COMBO | Sí | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` | Modo de calidad y velocidad de generación. "Fast" es el más rápido, "Extreme-High" produce la mayor calidad pero tarda más tiempo. |
| `material` | COMBO | Sí | `"PBR"`<br>`"Matte"`<br>`"Shiny"` | El estilo de material para el modelo 3D generado. |
| `formato_archivo_geometría` | COMBO | Sí | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` | El formato de archivo para el modelo 3D de salida. |
| `modo_textura` | COMBO | Sí | `"None"`<br>`"Generated"`<br>`"Generated+HD"` | Modo de generación de texturas. "None" no produce texturas, "Generated" crea texturas estándar, "Generated+HD" crea texturas de alta definición. |
| `semilla` | INT | Sí | 0 a 2147483647 | Semilla aleatoria para resultados reproducibles. Usar la misma semilla con las mismas entradas producirá la misma salida. |
| `TAPose` | BOOLEAN | Sí | Verdadero / Falso | Si se debe aplicar la pose T (brazos extendidos) al modelo generado. |
| `textura_hd` | BOOLEAN | Sí | Verdadero / Falso | Si se deben generar texturas de alta definición para el modelo. |
| `eliminar_iluminación_textura` | BOOLEAN | Sí | Verdadero / Falso | Si se debe aplicar realce de textura (calidad de textura mejorada) al modelo. |
| `addon_highpack` | BOOLEAN | Sí | Verdadero / Falso | Si se debe generar una versión de alta poligonización del modelo además de la estándar. |
| `ancho_bbox` | INT | Sí | 1 a 1000 | El ancho de la caja delimitadora en unidades del mundo. |
| `alto_bbox` | INT | Sí | 1 a 1000 | La altura de la caja delimitadora en unidades del mundo. |
| `largo_bbox` | INT | Sí | 1 a 1000 | La longitud de la caja delimitadora en unidades del mundo. |
| `altura_cm` | INT | Sí | 1 a 300 | La altura del modelo generado en centímetros. |

**Nota:** El parámetro `prompt` debe tener entre 1 y 2500 caracteres. El parámetro `seed` tiene como valor predeterminado 0 (aleatorio) si no se especifica.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `model_file` | FILE3DANY | El archivo del modelo 3D generado en el formato especificado. |

---
**Source fingerprint (SHA-256):** `79fbaf466e9af88cdfdac0f9136a2df17ba4bc2e5bb65a35b9ad2b1181da94db`
