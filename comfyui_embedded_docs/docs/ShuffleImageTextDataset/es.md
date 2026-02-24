> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/es.md)

Este nodo baraja una lista de imágenes y una lista de textos de manera conjunta, manteniendo intactos sus emparejamientos. Utiliza una semilla aleatoria para determinar el orden del barajado, garantizando que las mismas listas de entrada se barajen de la misma forma cada vez que se reutilice la semilla.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sí | - | Lista de imágenes a barajar. |
| `texts` | STRING | Sí | - | Lista de textos a barajar. |
| `seed` | INT | No | 0 a 18446744073709551615 | Semilla aleatoria. El orden del barajado se determina por este valor (por defecto: 0). |

**Nota:** Las entradas `images` y `texts` deben ser listas de la misma longitud. El nodo emparejará la primera imagen con el primer texto, la segunda imagen con el segundo texto, y así sucesivamente, antes de barajar estos pares de manera conjunta.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `images` | IMAGE | La lista barajada de imágenes. |
| `texts` | STRING | La lista barajada de textos, manteniendo sus emparejamientos originales con las imágenes. |
