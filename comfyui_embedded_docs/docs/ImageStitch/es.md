> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageStitch/es.md)

Este nodo te permite unir dos imágenes en una dirección especificada (arriba, abajo, izquierda, derecha), con soporte para ajuste de tamaño y espaciado entre imágenes.

## Entradas

| Nombre del Parámetro | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango | Descripción |
|---------------|-----------|-------------|---------|--------|-------------|
| `image1` | IMAGE | Requerida | - | - | La primera imagen que se va a unir |
| `image2` | IMAGE | Opcional | None | - | La segunda imagen que se va a unir; si no se proporciona, devuelve solo la primera imagen |
| `direction` | STRING | Requerida | right | right/down/left/up | La dirección para unir la segunda imagen: derecha, abajo, izquierda o arriba |
| `match_image_size` | BOOLEAN | Requerida | True | True/False | Si se debe redimensionar la segunda imagen para que coincida con las dimensiones de la primera imagen |
| `spacing_width` | INT | Requerida | 0 | 0-1024 | Ancho del espacio entre imágenes, debe ser un número par |
| `spacing_color` | STRING | Requerida | white | white/black/red/green/blue | Color del espacio entre las imágenes unidas |

> Para `spacing_color`, al usar colores distintos a "white/black", si `match_image_size` está configurado como `false`, el área de relleno se completará con negro

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La imagen unida |

## Ejemplo de Flujo de Trabajo

En el flujo de trabajo a continuación, usamos 3 imágenes de entrada de diferentes tamaños como ejemplo:

- image1: 500x300
- image2: 400x250
- image3: 300x300

![workflow](./asset/workflow.webp)

**Primer Nodo de Unión de Imágenes**

- `match_image_size`: false, las imágenes se unirán en sus tamaños originales
- `direction`: up, `image2` se colocará encima de `image1`
- `spacing_width`: 20
- `spacing_color`: black

Imagen de salida 1:

![output1](./asset/output-1.webp)

**Segundo Nodo de Unión de Imágenes**

- `match_image_size`: true, la segunda imagen se escalará para que coincida con la altura o el ancho de la primera imagen
- `direction`: right, `image3` aparecerá en el lado derecho
- `spacing_width`: 20
- `spacing_color`: white

Imagen de salida 2:

![output2](./asset/output-2.webp)