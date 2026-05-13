> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/es.md)

El nodo ByteDance Image genera imágenes utilizando modelos de ByteDance a través de una API basada en indicaciones de texto. Permite seleccionar un modelo, especificar las dimensiones de la imagen y controlar varios parámetros de generación como la semilla y la escala de guía. El nodo se conecta al servicio de generación de imágenes de ByteDance y devuelve la imagen creada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | STRING | Sí | `"seedream-3-0-t2i-250415"` | El modelo de ByteDance a utilizar para la generación de imágenes. Actualmente solo hay una opción de modelo disponible. |
| `prompt` | STRING | Sí | - | La indicación de texto utilizada para generar la imagen. Debe tener al menos 1 carácter después de eliminar espacios en blanco. |
| `size_preset` | STRING | Sí | Ver descripción | Elige un tamaño recomendado. Selecciona Personalizado para usar el ancho y alto indicados a continuación. Los preajustes disponibles están definidos por la lista `RECOMMENDED_PRESETS`. |
| `width` | INT | Sí | 512 a 2048 (paso 64) | Ancho personalizado para la imagen. Este valor solo se utiliza cuando `size_preset` está configurado en `Personalizado`. Valor predeterminado: 1024. |
| `height` | INT | Sí | 512 a 2048 (paso 64) | Alto personalizado para la imagen. Este valor solo se utiliza cuando `size_preset` está configurado en `Personalizado`. Valor predeterminado: 1024. |
| `seed` | INT | No | 0 a 2147483647 (paso 1) | Semilla a utilizar para la generación. Valor predeterminado: 0. |
| `guidance_scale` | FLOAT | No | 1.0 a 10.0 (paso 0.01) | Un valor más alto hace que la imagen siga la indicación más fielmente. Valor predeterminado: 2.5. |
| `watermark` | BOOLEAN | No | Verdadero / Falso | Si se debe agregar una marca de agua "Generado por IA" a la imagen. Valor predeterminado: Falso. Este es un parámetro avanzado. |

**Nota sobre los parámetros de tamaño:** Los parámetros `width` y `height` solo se utilizan cuando `size_preset` está configurado en `Personalizado`. Si se selecciona un tamaño predefinido, las dimensiones del preajuste anulan los valores personalizados de ancho y alto. Tanto el ancho como el alto deben estar entre 512 y 2048 píxeles al usar dimensiones personalizadas.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `IMAGE` | IMAGEN | La imagen generada devuelta por la API de ByteDance como un tensor. |

---
**Source fingerprint (SHA-256):** `6ad3011ae942e81bc5e5296fa7120ee89637ef7487e2f12822d84b6917ec211e`
