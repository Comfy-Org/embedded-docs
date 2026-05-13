> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/es.md)

Este nodo utiliza el servicio de IA de Magnific para ampliar y mejorar creativamente una imagen. Permite guiar la mejora con un texto descriptivo, elegir un estilo específico para optimizar el resultado y controlar diversos aspectos del proceso creativo como el detalle, el parecido con la original y la fuerza de estilización. El nodo genera una imagen ampliada según el factor seleccionado (2x, 4x, 8x o 16x), con un tamaño máximo de salida de 25,3 megapíxeles.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se ampliará y mejorará. |
| `prompt` | STRING | No | - | Una descripción textual para guiar la mejora creativa de la imagen. Es opcional (valor predeterminado: vacío). |
| `scale_factor` | COMBO | Sí | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` | El factor por el cual se ampliarán las dimensiones de la imagen. |
| `optimized_for` | COMBO | Sí | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` | El estilo o tipo de contenido para optimizar el proceso de mejora. |
| `creativity` | INT | No | -10 a 10 | Controla el nivel de interpretación creativa aplicada a la imagen (valor predeterminado: 0). |
| `hdr` | INT | No | -10 a 10 | El nivel de definición y detalle (valor predeterminado: 0). |
| `resemblance` | INT | No | -10 a 10 | El nivel de parecido con la imagen original (valor predeterminado: 0). |
| `fractality` | INT | No | -10 a 10 | La fuerza del texto descriptivo y la complejidad por píxel cuadrado (valor predeterminado: 0). |
| `engine` | COMBO | Sí | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` | El motor de IA específico a utilizar para el procesamiento. Este es un parámetro avanzado. |
| `auto_downscale` | BOOLEAN | No | - | Cuando está habilitado, el nodo reducirá automáticamente la escala de la imagen de entrada si la ampliación solicitada supera el tamaño máximo de salida permitido de 25,3 megapíxeles. Este es un parámetro avanzado (valor predeterminado: Falso). |

**Restricciones:**

* La `image` de entrada debe ser exactamente una imagen.
* La imagen de entrada debe tener una altura y anchura mínimas de 160 píxeles.
* La relación de aspecto de la imagen de entrada debe estar entre 1:3 y 3:1.
* El tamaño final de salida (dimensiones de entrada multiplicadas por el `scale_factor`) no puede superar los 25.300.000 píxeles. Si `auto_downscale` está deshabilitado y se superaría este límite, el nodo generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `image` | IMAGE | La imagen de salida ampliada y mejorada creativamente. |

---
**Source fingerprint (SHA-256):** `f5f046347c2992a2589153e803de14fc23b27187864b45eb566556418ebc161c`
