# FluxProImageNode

Genera imágenes de forma sincrónica a partir del prompt y la resolución. Este nodo crea imágenes utilizando el modelo Flux 1.1 Pro mediante el envío de solicitudes a un endpoint de la API y espera la respuesta completa antes de devolver la imagen generada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para la generación de la imagen (predeterminado: cadena vacía) | STRING | Sí | - |
| `prompt_upsampling` | Si se debe realizar sobremuestreo en el prompt. Si está activo, modifica automáticamente el prompt para una generación más creativa, pero los resultados no son deterministas (la misma semilla no producirá exactamente el mismo resultado). (predeterminado: False) | BOOLEAN | Sí | - |
| `width` | Ancho de la imagen en píxeles (predeterminado: 1024, paso: 32) | INT | Sí | 256-1440 |
| `height` | Alto de la imagen en píxeles (predeterminado: 768, paso: 32) | INT | Sí | 256-1440 |
| `seed` | La semilla aleatoria utilizada para crear el ruido. (predeterminado: 0) | INT | Sí | 0-18446744073709551615 |
| `image_prompt` | Imagen de referencia opcional para guiar la generación | IMAGE | No | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | La imagen generada devuelta por la API | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProImageNode/es.md)

---
**Source fingerprint (SHA-256):** `89316d84f364854541157b5b60bae3d4e25024bd4af61a47a1748c6671b463c1`
