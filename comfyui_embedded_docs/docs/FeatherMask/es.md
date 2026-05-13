> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FeatherMask/es.md)

El nodo `FeatherMask` aplica un efecto de difuminado en los bordes de una máscara determinada, suavizando la transición de sus bordes al ajustar su opacidad según distancias especificadas desde cada borde. Esto crea un efecto de borde más suave y difuminado.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `máscara`    | MASK         | La máscara a la que se aplicará el efecto de difuminado. Determina el área de la imagen que se verá afectada por el difuminado. |
| `izquierda`    | INT          | Especifica la distancia desde el borde izquierdo dentro de la cual se aplicará el efecto de difuminado. |
| `arriba`     | INT          | Especifica la distancia desde el borde superior dentro de la cual se aplicará el efecto de difuminado. |
| `derecha`   | INT          | Especifica la distancia desde el borde derecho dentro de la cual se aplicará el efecto de difuminado. |
| `abajo`  | INT          | Especifica la distancia desde el borde inferior dentro de la cual se aplicará el efecto de difuminado. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `máscara`    | MASK         | La salida es una versión modificada de la máscara de entrada con un efecto de difuminado aplicado en sus bordes. |