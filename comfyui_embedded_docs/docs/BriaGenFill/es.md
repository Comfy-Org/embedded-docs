# BriaGenFill

Este nodo genera objetos o escenas dentro de una región enmascarada de una imagen mediante la API de Bria. Sube la imagen y la máscara, envía el prompt al servicio de relleno generativo de Bria, espera a que la operación se complete y devuelve la imagen editada. Esta es una operación de API de pago (US$0.0429 por solicitud).

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `image` | La imagen de entrada que se va a editar. | IMAGE | Sí | - |
| `mask` | Las áreas blancas se rellenan con contenido generado; las áreas negras se conservan. La máscara se binariza antes de enviarse, por lo que las áreas parcialmente pintadas se consideran blancas. Debe tener la misma relación de aspecto que la imagen. | MASK | Sí | - |
| `prompt` | Descripción de lo que se debe generar dentro de la región enmascarada. Debe contener al menos 1 carácter. | STRING | Sí | - |
| `negative_prompt` | Un prompt que describe el contenido que se debe evitar en el resultado generado. Si se deja vacío, no se envía a la API. | STRING | Sí | - |
| `refine_prompt` | Ajusta automáticamente el prompt para obtener mejores resultados; desactívelo para usar el prompt exactamente como está escrito. (predeterminado: true) | BOOLEAN | Sí | true<br>false |
| `seed` | Semilla para el proceso de generación. (predeterminado: 42) | INT | Sí | 1 a 2147483647 |
| `moderation` | Configuración de moderación para la solicitud. Cuando se establece en "true", se aplican las opciones de moderación anidadas descritas a continuación. (predeterminado: "false") | COMBO | Sí | "false"<br>"true" |

Nota: el `prompt` no debe estar vacío y la `mask` debe tener la misma relación de aspecto que la `image`. La máscara se binariza al 50% de opacidad, por lo que las áreas pintadas con menos de la mitad de opacidad se ignoran; si la máscara no contiene áreas blancas después de la binarización, el nodo genera un error.

Cuando `moderation` se establece en "true", están disponibles las siguientes opciones booleanas anidadas:
- `prompt_content_moderation` (predeterminado: false): aplica moderación de contenido al prompt.
- `visual_input_moderation` (predeterminado: false): aplica moderación de contenido a la imagen de entrada.
- `visual_output_moderation` (predeterminado: false): aplica moderación de contenido a la imagen de salida.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `image` | La imagen resultante con la región enmascarada rellenada por el contenido generado. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/es.md)

---
**Source fingerprint (SHA-256):** `0d9babfa5e14c03f73d2b5befbd1c5cd1f5ffc685a0d7ccb3db09cfec51ba4fa`
