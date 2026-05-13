> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToImageApi/es.md)

El nodo Wan Image to Image genera una imagen a partir de una o dos imágenes de entrada y una descripción textual. Transforma tus imágenes de entrada según la descripción que proporciones, creando una nueva imagen que mantiene la relación de aspecto de tu entrada original. La imagen de salida tiene una resolución fija de 1,6 megapíxeles, independientemente del tamaño de entrada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | "wan2.5-i2i-preview" | Modelo a utilizar (predeterminado: "wan2.5-i2i-preview"). |
| `imagen` | IMAGE | Sí | - | Edición de una sola imagen o fusión de múltiples imágenes, máximo 2 imágenes. |
| `texto_descriptivo` | STRING | Sí | - | Prompt que describe los elementos y características visuales. Compatible con inglés y chino (predeterminado: vacío). |
| `texto_negativo` | STRING | No | - | Prompt negativo que describe lo que se debe evitar (predeterminado: vacío). |
| `semilla` | INT | No | 0 a 2147483647 | Semilla a utilizar para la generación (predeterminado: 0). |
| `marca_agua` | BOOLEAN | No | - | Indica si se debe agregar una marca de agua de IA generada al resultado (predeterminado: falso). |

**Nota:** Este nodo acepta exactamente 1 o 2 imágenes de entrada. Si proporcionas más de 2 imágenes o ninguna imagen, el nodo devolverá un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------------|---------------|-------------|
| `imagen` | IMAGE | La imagen generada a partir de las imágenes de entrada y las descripciones textuales. |

---
**Source fingerprint (SHA-256):** `d69811ddaba718e5468f539fb9b25827efdf79f3ee9cbf31ad8f9387cea9b9be`
