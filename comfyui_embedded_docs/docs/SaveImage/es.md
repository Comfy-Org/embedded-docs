# Guardar Imagen

El nodo SaveImage guarda las imágenes que recibe en tu directorio `ComfyUI/output`. Guarda cada imagen como un archivo PNG y puede incrustar metadatos del flujo de trabajo, como el prompt, en el archivo guardado para referencia futura.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `images` | Las imágenes a guardar. | IMAGE | Sí | - |
| `filename_prefix` | El prefijo para el archivo a guardar. Puede incluir información de formato como `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%` para incluir valores de nodos (predeterminado: "ComfyUI"). | STRING | Sí | - |
| `prompt` | Entrada oculta, proporcionada automáticamente por ComfyUI: los datos del prompt incrustados como metadatos en el archivo PNG guardado. | PROMPT | No | - |
| `extra_pnginfo` | Entrada oculta, proporcionada automáticamente por ComfyUI: información adicional del flujo de trabajo incrustada como metadatos en el archivo PNG guardado. | EXTRA_PNGINFO | No | - |

Cada imagen se guarda como un archivo PNG. En el nombre de archivo guardado, `%batch_num%` en el prefijo se reemplaza con el número de lote de la imagen, y se añade un contador rellenado con ceros.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `images` | Las mismas imágenes que se guardaron, pasadas para que otros nodos puedan usarlas. | IMAGE |
| `ui` | Resultado de UI que contiene una lista de las imágenes guardadas con sus nombres de archivo, subcarpetas y tipo, mostrado en la interfaz de ComfyUI. | UI_RESULT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/es.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
