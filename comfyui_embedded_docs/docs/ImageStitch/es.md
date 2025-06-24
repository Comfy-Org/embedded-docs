Este nodo te permite unir dos imágenes en una dirección específica (arriba, abajo, izquierda, derecha), con soporte para ajustar el tamaño y añadir espaciado entre las imágenes.

## Entradas

| Nombre del Parámetro | Tipo de Dato | Tipo de Entrada | Valor Predeterminado | Rango | Descripción |
|---------------------|--------------|-----------------|---------------------|--------|-------------|
| `image1` | IMAGE | Requerido | - | - | La primera imagen a unir |
| `image2` | IMAGE | Opcional | None | - | La segunda imagen a unir, si no se proporciona solo devuelve la primera imagen |
| `direction` | STRING | Requerido | right | right/down/left/up | La dirección para unir la segunda imagen: right (derecha), down (abajo), left (izquierda), o up (arriba) |
| `match_image_size` | BOOLEAN | Requerido | True | True/False | Si se debe redimensionar la segunda imagen para que coincida con las dimensiones de la primera imagen |
| `spacing_width` | INT | Requerido | 0 | 0-1024 | Ancho del espaciado entre imágenes, debe ser un número par |
| `spacing_color` | STRING | Requerido | white | white/black/red/green/blue | Color del espaciado entre las imágenes unidas |

> Para `spacing_color`, cuando se usan colores diferentes a "white/black", si `match_image_size` está configurado como `false`, el área de relleno será de color negro

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `IMAGE` | IMAGE | La imagen unida |

## Ejemplo de Flujo de Trabajo

En el flujo de trabajo a continuación, usamos 3 imágenes de entrada de diferentes tamaños como ejemplos:

- image1: 500x300
- image2: 400x250
- image3: 300x300

![workflow](./asset/workflow.webp)

**Primer Nodo Image Stitch**

- `match_image_size`: false, las imágenes se unirán en sus tamaños originales
- `direction`: up, `image2` se colocará encima de `image1`
- `spacing_width`: 20
- `spacing_color`: black

Imagen de salida 1:

![output1](./asset/output-1.webp)

**Segundo Nodo Image Stitch**

- `match_image_size`: true, la segunda imagen se escalará para coincidir con la altura o el ancho de la primera imagen
- `direction`: right, `image3` aparecerá en el lado derecho
- `spacing_width`: 20
- `spacing_color`: white

Imagen de salida 2:

![output2](./asset/output-2.webp)
