El nodo GeminiImage2Node genera o edita imágenes utilizando el modelo Gemini de Vertex AI de Google. Envía un mensaje de texto e imágenes o archivos de referencia opcionales a la API y devuelve la imagen generada y/o una descripción textual.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Mensaje de texto que describe la imagen a generar o las ediciones a aplicar. Incluye cualquier restricción, estilo o detalle que el modelo deba seguir. | STRING | Sí | N/A |
| `model` | El modelo Gemini específico a utilizar para la generación. La opción "Nano Banana 2" se asigna internamente al modelo `gemini-3.1-flash-image-preview`. | COMBO | Sí | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Cuando se fija a un valor específico, el modelo hace el mejor esfuerzo para proporcionar la misma respuesta en solicitudes repetidas. No se garantiza una salida determinista. Cambiar el modelo u otras configuraciones puede causar variaciones incluso con la misma semilla. Valor predeterminado: 42. | INT | Sí | 0 a 18446744073709551615 |
| `aspect_ratio` | La relación de aspecto deseada para la imagen de salida. Si se establece en 'auto', coincide con la relación de aspecto de la imagen de entrada; si no se proporciona ninguna imagen, generalmente se genera un cuadrado de 16:9. Valor predeterminado: "auto". | COMBO | Sí | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Resolución de salida objetivo. Para 2K/4K se utiliza el escalador nativo de Gemini. | COMBO | Sí | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Elige 'IMAGE' para salida solo de imagen, o 'IMAGE+TEXT' para devolver tanto la imagen generada como una respuesta de texto. | COMBO | Sí | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | Imagen(es) de referencia opcional(es). Para incluir múltiples imágenes, usa el nodo de Imágenes por Lote (hasta 14). | IMAGE | No | N/A |
| `files` | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo de Archivos de Entrada de Generación de Contenido Gemini. | CUSTOM | No | N/A |
| `system_prompt` | Instrucciones fundamentales que dictan el comportamiento de una IA. Valor predeterminado: Un mensaje de sistema predefinido para la generación de imágenes. | STRING | No | N/A |

**Restricciones:**

* La entrada `images` admite un máximo de 14 imágenes. Si se proporcionan más, se generará un error.
* La entrada `files` debe estar conectada a un nodo que genere el tipo de dato `GEMINI_INPUT_FILES`.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `image` | La imagen generada o editada por el modelo Gemini. | IMAGE |
| `string` | La respuesta de texto del modelo. Esta salida estará vacía si `response_modalities` está configurado en "IMAGE". | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/es.md)

---
**Source fingerprint (SHA-256):** `20a937a635f883a42e22582ae415f6d2a9a6ecc50f147c9090431877e5461144`
