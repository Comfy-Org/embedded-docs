> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/es.md)

Este nodo aplica el estilo visual de una imagen de referencia a tu imagen de entrada. Utiliza un servicio de IA externo para procesar las imágenes, permitiéndote controlar la intensidad de la transferencia de estilo y la preservación de la estructura de la imagen original.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen a la que se le aplicará la transferencia de estilo. |
| `reference_image` | IMAGE | Sí | - | La imagen de referencia de la cual extraer el estilo. |
| `prompt` | STRING | No | - | Un texto opcional para guiar la transferencia de estilo. |
| `style_strength` | INT | No | 0 a 100 | Porcentaje de intensidad del estilo (valor predeterminado: 100). |
| `structure_strength` | INT | No | 0 a 100 | Mantiene la estructura de la imagen original (valor predeterminado: 50). |
| `flavor` | COMBO | No | "faithful"<br>"gen_z"<br>"psychedelia"<br>"detaily"<br>"clear"<br>"donotstyle"<br>"donotstyle_sharp" | Sabor de la transferencia de estilo. |
| `engine` | COMBO | No | "balanced"<br>"definio"<br>"illusio"<br>"3d_cartoon"<br>"colorful_anime"<br>"caricature"<br>"real"<br>"super_real"<br>"softy" | Selección del motor de procesamiento. |
| `portrait_mode` | COMBO | No | "disabled"<br>"enabled" | Activar el modo retrato para mejoras faciales. |
| `portrait_style` | COMBO | No | "standard"<br>"pop"<br>"super_pop" | Estilo visual aplicado a las imágenes de retrato. Esta entrada solo está disponible cuando `portrait_mode` está configurado en "enabled". |
| `portrait_beautifier` | COMBO | No | "none"<br>"beautify_face"<br>"beautify_face_max" | Intensidad de embellecimiento facial en retratos. Esta entrada solo está disponible cuando `portrait_mode` está configurado en "enabled". |
| `fixed_generation` | BOOLEAN | No | - | Cuando está desactivado, se espera que cada generación introduzca un grado de aleatoriedad, lo que genera resultados más diversos (valor predeterminado: True). |

**Restricciones:**

* Se requiere exactamente una `image` y una `reference_image`.
* Ambas imágenes deben tener una relación de aspecto entre 1:3 y 3:1.
* Ambas imágenes deben tener una altura y anchura mínimas de 160 píxeles.
* Los parámetros `portrait_style` y `portrait_beautifier` solo están activos y son obligatorios cuando `portrait_mode` está configurado en "enabled".

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen resultante después de aplicar la transferencia de estilo. |

---
**Source fingerprint (SHA-256):** `4ae400183618953c369d089d39b878f0a24592967c29d779c577fb8b7339dea8`
