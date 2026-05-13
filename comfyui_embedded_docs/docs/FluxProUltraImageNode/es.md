> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/es.md)

Genera imágenes usando Flux Pro 1.1 Ultra a través de API basándose en una descripción textual y resolución. Este nodo se conecta a un servicio externo para crear imágenes según tu descripción de texto y las dimensiones especificadas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Descripción textual para la generación de la imagen (valor predeterminado: cadena vacía) |
| `prompt_upsampling` | BOOLEAN | No | - | Si se debe realizar un sobremuestreo en la descripción textual. Si está activo, modifica automáticamente la descripción para una generación más creativa, pero los resultados no son deterministas (la misma semilla no producirá exactamente el mismo resultado). (valor predeterminado: False) |
| `seed` | INT | No | 0 a 18446744073709551615 | La semilla aleatoria utilizada para crear el ruido. (valor predeterminado: 0) |
| `aspect_ratio` | STRING | No | - | Relación de aspecto de la imagen; debe estar entre 1:4 y 4:1. (valor predeterminado: "16:9") |
| `raw` | BOOLEAN | No | - | Cuando es True, genera imágenes menos procesadas y de apariencia más natural. (valor predeterminado: False) |
| `image_prompt` | IMAGE | No | - | Imagen de referencia opcional para guiar la generación |
| `image_prompt_strength` | FLOAT | No | 0.0 a 1.0 | Mezcla entre la descripción textual y la imagen de referencia. (valor predeterminado: 0.1) |

**Nota:** El parámetro `aspect_ratio` debe estar entre 1:4 y 4:1. Cuando se proporciona `image_prompt`, `image_prompt_strength` se activa y controla cuánto influye la imagen de referencia en el resultado final. Si no se proporciona `image_prompt`, el parámetro `prompt` se valida para asegurar que no esté vacío.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output_image` | IMAGE | La imagen generada por Flux Pro 1.1 Ultra |

---
**Source fingerprint (SHA-256):** `8632aeb76e9007d65d7f3fd51465fe78f56ba92264ef65ce505db2fc95cfd25b`
