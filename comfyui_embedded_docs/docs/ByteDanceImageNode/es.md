# Imagen ByteDance

El nodo ByteDance Image genera imágenes utilizando modelos de ByteDance a través de una API basada en indicaciones de texto. Permite seleccionar un modelo, especificar las dimensiones de la imagen y controlar varios parámetros de generación como la semilla y la escala de guía. El nodo se conecta al servicio de generación de imágenes de ByteDance y devuelve la imagen creada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de ByteDance a utilizar para la generación de imágenes. Actualmente solo hay una opción de modelo disponible. | STRING | Sí | `"seedream-3-0-t2i-250415"` |
| `prompt` | La indicación de texto utilizada para generar la imagen. Debe tener al menos 1 carácter después de eliminar espacios en blanco. | STRING | Sí | - |
| `tamaño_predefinido` | Elige un tamaño recomendado. Selecciona Personalizado para usar el ancho y alto indicados a continuación. Los preajustes disponibles están definidos por la lista `RECOMMENDED_PRESETS`. | STRING | Sí | Ver descripción |
| `ancho` | Ancho personalizado para la imagen. Este valor solo se utiliza cuando `tamaño_predefinido` está configurado en `Personalizado`. Valor predeterminado: 1024. | INT | Sí | 512 a 2048 (paso 64) |
| `alto` | Alto personalizado para la imagen. Este valor solo se utiliza cuando `tamaño_predefinido` está configurado en `Personalizado`. Valor predeterminado: 1024. | INT | Sí | 512 a 2048 (paso 64) |
| `semilla` | Semilla a utilizar para la generación. Valor predeterminado: 0. | INT | No | 0 a 2147483647 (paso 1) |
| `escala_de_guía` | Un valor más alto hace que la imagen siga la indicación más fielmente. Valor predeterminado: 2.5. | FLOAT | No | 1.0 a 10.0 (paso 0.01) |
| `marca_de_agua` | Si se debe agregar una marca de agua "Generado por IA" a la imagen. Valor predeterminado: Falso. Este es un parámetro avanzado. | BOOLEAN | No | Verdadero / Falso |

**Nota sobre los parámetros de tamaño:** Los parámetros `width` y `height` solo se utilizan cuando `size_preset` está configurado en `Personalizado`. Si se selecciona un tamaño predefinido, las dimensiones del preajuste anulan los valores personalizados de ancho y alto. Tanto el ancho como el alto deben estar entre 512 y 2048 píxeles al usar dimensiones personalizadas.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `IMAGE` | La imagen generada devuelta por la API de ByteDance como un tensor. | IMAGEN |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/es.md)

---
**Source fingerprint (SHA-256):** `6ad3011ae942e81bc5e5296fa7120ee89637ef7487e2f12822d84b6917ec211e`
