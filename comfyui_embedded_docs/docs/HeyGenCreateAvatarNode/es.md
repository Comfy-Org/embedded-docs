# HeyGenCreateAvatarNode

Crea un avatar reutilizable de HeyGen a partir de una foto de una persona o de una instrucción de texto que describa un personaje para generar. El ID del avatar resultante se puede usar con el nodo Video de Avatar de HeyGen para crear videos con este avatar.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `source` | Genera un nuevo personaje a partir de una instrucción de texto, o crea el avatar desde una foto conectada de una persona. | COMBO | Sí | `"prompt"`<br>`"photo"` |

Cuando `source` está configurado en `"prompt"`, los siguientes parámetros adicionales están disponibles:

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descripción del avatar a generar (hasta 1000 caracteres). | STRING | Sí | 1 a 1000 caracteres |
| `reference_images` | Hasta 3 imágenes de referencia que guían la apariencia generada. | IMAGE | No | 0 a 3 imágenes |

Cuando `source` está configurado en `"photo"`, el siguiente parámetro adicional está disponible:

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `identity_photo` | Foto de la persona para convertir en avatar. Se reduce automáticamente si es mayor a 2K. | IMAGE | Sí | Imagen única |

**Nota:** El parámetro `source` cambia entre dos modos. En el modo `"prompt"`, proporcionas una descripción de texto y opcionalmente hasta 3 imágenes de referencia. En el modo `"photo"`, proporcionas una sola foto de una persona. Estos modos son mutuamente excluyentes.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|-------------|-------------|-----------|
| `avatar_id` | ID de apariencia del avatar. Pásalo al `custom_avatar_id` de Video de Avatar de HeyGen; guárdalo para reutilizar el avatar más tarde. | STRING |
| `preview` | Imagen de vista previa del avatar generado. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/es.md)

---
**Source fingerprint (SHA-256):** `c60e9cdb0d91fb5ec6ea83b503b9aa10c978ce065a16c751a52e90c12e70a5e2`
