# BriaGenFill

Este nodo genera objetos o escenarios dentro de una región enmascarada de una imagen mediante la API de Bria. Carga la imagen y la máscara, envía el prompt al servicio de relleno generativo de Bria, espera a que la operación se complete y devuelve la imagen editada. Esta es una operación de pago de la API (US$0.0429 por solicitud).

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `image` | La imagen de entrada para editar. | IMAGE | Sí | - |
| `mask` | Las áreas blancas se rellenan con contenido generado, las áreas negras se conservan. La máscara se binariza antes de enviarse, por lo que las áreas parcialmente pintadas se consideran blancas. Debe tener la misma relación de aspecto que la imagen. | MASK | Sí | - |
| `prompt` | Descripción de lo que se debe generar dentro de la región enmascarada. Debe contener al menos 1 carácter. (por defecto: "") | STRING | Sí | - |
| `negative_prompt` | Un prompt que describe el contenido que se debe evitar en el resultado generado. Si se deja vacío, no se envía a la API. (por defecto: "") | STRING | Sí | - |
| `refine_prompt` | Ajusta automáticamente el prompt para obtener mejores resultados; desactívelo para usar el prompt tal como está escrito. (por defecto: true) | BOOLEAN | Sí | true<br>false |
| `seed` | Semilla para el proceso de generación. (por defecto: 42) | INT | Sí | 1 a 2147483647 |
| `moderación` | Configuración de moderación. Cuando se establece en "true", se aplican las opciones de moderación siguientes. (por defecto: "false") | DYNAMIC_COMBO | Sí | "false"<br>"true" |

### Entradas de moderación (cuando `moderation` = "true")

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Aplica moderación de contenido al prompt. (por defecto: false) | BOOLEAN | No | true<br>false |
| `visual_input_moderation` | Aplica moderación de contenido a la imagen de entrada. (por defecto: false) | BOOLEAN | No | true<br>false |
| `visual_output_moderation` | Aplica moderación de contenido a la imagen de salida. (por defecto: false) | BOOLEAN | No | true<br>false |

**Nota:** El `prompt` no debe estar vacío. La `mask` debe tener la misma relación de aspecto que la `image`. La máscara se binariza al 50% de opacidad, por lo que las áreas pintadas con menos de la mitad de opacidad se ignoran; si la máscara no contiene áreas blancas después de la binarización, el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `image` | La imagen resultante con la región enmascarada rellenada por el contenido generado. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/es.md)

---
**Source fingerprint (SHA-256):** `0d9babfa5e14c03f73d2b5befbd1c5cd1f5ffc685a0d7ccb3db09cfec51ba4fa`
