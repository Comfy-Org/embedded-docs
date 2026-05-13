> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/es.md)

El nodo ByteDance Seedream 4.5 y 5.0 proporciona capacidades unificadas de generación de texto a imagen y edición precisa por oración individual en resoluciones de hasta 4K. Puede crear nuevas imágenes a partir de descripciones textuales o editar imágenes existentes mediante instrucciones de texto. El nodo admite tanto la generación de una sola imagen como la generación secuencial de múltiples imágenes relacionadas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | STRING | Sí | Ver Descripción | El modelo Seedream a utilizar para la generación. Los modelos disponibles incluyen variantes seedream-4-0, seedream-4-5 y seedream-5-0. |
| `prompt` | STRING | Sí | - | Descripción textual para crear o editar una imagen. Debe tener al menos 1 carácter de longitud. |
| `imagen` | IMAGE | No | - | Imagen(es) de entrada para generación de imagen a imagen. Imagen(es) de referencia para generación con referencia única o múltiple. Máximo de 10 imágenes de referencia para la mayoría de modelos, o 14 para seedream-5-0-260128. |
| `predefinición_de_tamaño` | STRING | No | Múltiples opciones disponibles | Selecciona un tamaño recomendado. Elige "Custom" (Personalizado) para usar el ancho y alto indicados a continuación. Valor predeterminado: primer preset de RECOMMENDED_PRESETS_SEEDREAM_4. |
| `ancho` | INT | No | 1024 a 6240 (paso 2) | Ancho personalizado para la imagen. El valor solo funciona si `predefinición_de_tamaño` está configurado en `Custom`. Valor predeterminado: 2048. |
| `alto` | INT | No | 1024 a 4992 (paso 2) | Alto personalizado para la imagen. El valor solo funciona si `predefinición_de_tamaño` está configurado en `Custom`. Valor predeterminado: 2048. |
| `generación_secuencial_de_imágenes` | STRING | No | "disabled"<br>"auto" | Modo de generación de imágenes en grupo. "disabled" genera una sola imagen. "auto" permite que el modelo decida si generar múltiples imágenes relacionadas (ej. escenas de historias, variaciones de personajes). Valor predeterminado: "disabled". |
| `imágenes_máximas` | INT | No | 1 a 15 (paso 1) | Número máximo de imágenes a generar cuando sequential_image_generation='auto'. El total de imágenes (entrada + generadas) no puede exceder 15. Valor predeterminado: 1. |
| `semilla` | INT | No | 0 a 2147483647 (paso 1) | Semilla a utilizar para la generación. Valor predeterminado: 0. |
| `marca_de_agua` | BOOLEAN | No | - | Si se debe añadir una marca de agua "Generado por IA" a la imagen. Valor predeterminado: False. |
| `fallar_en_parcial` | BOOLEAN | No | - | Si está habilitado, aborta la ejecución si falta alguna de las imágenes solicitadas o devuelve un error. Valor predeterminado: True. |

**Notas sobre las restricciones de parámetros:**
- La resolución mínima de la imagen depende del modelo seleccionado: 3.68MP para modelos seedream-4-5 y seedream-5-0, 0.92MP para modelos seedream-4-0.
- La resolución máxima de la imagen es 10.4MP para modelos seedream-5-0 y 16.78MP para otros modelos.
- Las imágenes de referencia deben tener una relación de aspecto entre 1:3 y 3:1.
- Cuando `sequential_image_generation` está configurado en "auto", el número total de imágenes de entrada más `max_images` no puede exceder 15.
- Los parámetros `width` y `height` solo se utilizan cuando `size_preset` está configurado en "Custom".

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Imagen(es) generada(s) según los parámetros de entrada y la descripción textual. Devuelve un tensor de una sola imagen o un lote de tensores de imagen si se generan múltiples imágenes. |

---
**Source fingerprint (SHA-256):** `ce130246026e0f5036e137bea4e193f51097e0812459586dcbeb87ef01975630`
