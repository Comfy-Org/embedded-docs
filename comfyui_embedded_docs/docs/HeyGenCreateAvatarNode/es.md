# Crear Avatar HeyGen

Crea un avatar HeyGen reutilizable a partir de una foto de una persona o de un prompt de texto que describa un personaje para generar. El `avatar_id` resultante puede usarse con el nodo HeyGen Avatar Video y debe guardarse para reutilizar el avatar en futuros flujos de trabajo.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `fuente` | Genera un nuevo personaje a partir de un prompt de texto, o crea el avatar a partir de una foto de una persona conectada. | DYNAMIC_COMBO | Sí | `"prompt"`<br>`"photo"` |

### Entradas de prompt

Disponible cuando `source` está configurado como `"prompt"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Descripción del avatar a generar (hasta 1000 caracteres). Debe contener al menos 1 carácter que no sea un espacio. Valor predeterminado: cadena vacía. | STRING | Sí | 1 a 1000 caracteres |

### Entradas de foto

Disponible cuando `source` está configurado como `"photo"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `identity_photo` | Foto de la persona que se convertirá en avatar. Se reduce automáticamente si es mayor de 2K. | IMAGE | Sí | Imagen única |

### Entradas de referencia

Disponible cuando `source` está configurado como `"prompt"`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `reference_images` | Ranura ampliable: conecta hasta 3 imágenes (`ref_image_1`...`ref_image_3`) que guían la apariencia generada. Las imágenes se reducen automáticamente si son mayores de 2K. | IMAGE | No | 0 a 3 imágenes |

**Nota:** El parámetro `source` cambia entre dos modos mutuamente excluyentes. En el modo `"prompt"`, `prompt` es obligatorio y se pueden conectar opcionalmente hasta 3 imágenes de referencia. En el modo `"photo"`, `identity_photo` es obligatorio. Las fotos y las imágenes de referencia se reducen automáticamente cuando son mayores de 2K; no se aceptan más de 3 imágenes de referencia.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `avatar_id` | ID de apariencia del avatar. Pásalo al `custom_avatar_id` de HeyGen Avatar Video; consérvalo para reutilizar el avatar en futuros flujos de trabajo. | STRING |
| `vista previa` | Imagen de vista previa del avatar generado. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/es.md)

---
**Source fingerprint (SHA-256):** `c60e9cdb0d91fb5ec6ea83b503b9aa10c978ce065a16c751a52e90c12e70a5e2`
