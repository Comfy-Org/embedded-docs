# Magnific Image Upscale (Creativo)

Este nodo utiliza el servicio Magnific AI para ampliar y mejorar creativamente una imagen. Permite guiar la mejora con un prompt de texto, elegir un estilo específico para optimizar y controlar varios aspectos del proceso creativo, como el detalle, la semejanza con la original y la fuerza de estilización. El nodo genera una imagen ampliada según el factor elegido (2x, 4x, 8x o 16x), con un tamaño máximo de salida de 25,3 megapíxeles.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `imagen` | La imagen de entrada que se va a ampliar y mejorar. | IMAGE | Sí | - |
| `prompt` | Una descripción de texto para guiar la mejora creativa de la imagen. Es opcional (por defecto: vacío). | STRING | No | - |
| `factor_de_escala` | El factor por el que se amplían las dimensiones de la imagen. | COMBO | Sí | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `optimizado_para` | El estilo o tipo de contenido para el que se optimiza el proceso de mejora. | COMBO | Sí | `"standard"`<br>`"soft_portraits"`<br>`"hard_portraits"`<br>`"art_n_illustration"`<br>`"videogame_assets"`<br>`"nature_n_landscapes"`<br>`"films_n_photography"`<br>`"3d_renders"`<br>`"science_fiction_n_horror"` |
| `creatividad` | Controla el nivel de interpretación creativa aplicada a la imagen (por defecto: 0). | INT | No | -10 a 10 |
| `hdr` | El nivel de definición y detalle (por defecto: 0). | INT | No | -10 a 10 |
| `semejanza` | El nivel de semejanza con la imagen original (por defecto: 0). | INT | No | -10 a 10 |
| `fractalidad` | La fuerza del prompt y la complejidad por píxel cuadrado (por defecto: 0). | INT | No | -10 a 10 |
| `motor` | El motor de IA específico que se utiliza para el procesamiento. Este es un parámetro avanzado. | COMBO | Sí | `"automatic"`<br>`"magnific_illusio"`<br>`"magnific_sharpy"`<br>`"magnific_sparkle"` |
| `reducción_automática` | Reduce automáticamente la escala de la imagen de entrada si la salida superara el límite máximo de píxeles (por defecto: False). Este es un parámetro avanzado. | BOOLEAN | No | - |

**Restricciones:**

* La imagen `image` de entrada debe ser exactamente una imagen.
* La imagen de entrada debe tener una altura y una anchura mínimas de 160 píxeles.
* La relación de aspecto de la imagen de entrada debe estar entre 1:3 y 3:1.
* El tamaño final de salida (dimensiones de entrada multiplicadas por el `scale_factor`) no puede superar los 25.300.000 píxeles. Si se excediera este límite:
  - Cuando `auto_downscale` está habilitado, el nodo reduce automáticamente el tamaño de la imagen de entrada (como máximo 2x) o utiliza un `scale_factor` menor para que la salida se mantenga dentro del límite.
  - Cuando `auto_downscale` está deshabilitado, el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `image` | La imagen de salida ampliada y mejorada creativamente. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerCreativeNode/es.md)

---
**Source fingerprint (SHA-256):** `36c38e87f9f1e568c78cf794aeb0a268c6d25d639006eb2cf18ee040d3071ad4`
