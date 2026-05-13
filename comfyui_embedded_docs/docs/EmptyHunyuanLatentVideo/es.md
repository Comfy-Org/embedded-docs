> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanLatentVideo/es.md)

El nodo `EmptyHunyuanLatentVideo` es similar al nodo `EmptyLatentImage`. Puede considerarse como un lienzo en blanco para la generación de video, donde el ancho, la altura y la longitud definen las propiedades del lienzo, y el tamaño del lote determina la cantidad de lienzos a crear. Este nodo crea lienzos vacíos listos para tareas posteriores de generación de video.

## Entradas

| Parámetro    | Tipo Comfy | Descripción                                                                                |
| ----------- | ---------- | ------------------------------------------------------------------------------------------ |
| `ancho`     | `INT`      | Ancho del video, valor predeterminado 848, mínimo 16, máximo `nodes.MAX_RESOLUTION`, tamaño de paso 16.        |
| `altura`    | `INT`      | Altura del video, valor predeterminado 480, mínimo 16, máximo `nodes.MAX_RESOLUTION`, tamaño de paso 16.       |
| `longitud`    | `INT`      | Longitud del video, valor predeterminado 25, mínimo 1, máximo `nodes.MAX_RESOLUTION`, tamaño de paso 4.          |
| `tamaño_del_lote`| `INT`      | Tamaño del lote, valor predeterminado 1, mínimo 1, máximo 4096.                                           |

## Salidas

| Parámetro | Tipo Comfy | Descripción                                                                               |
| --------- | ---------- | ----------------------------------------------------------------------------------------- |
| `samples` | `LATENT`   | Muestras de video latente generadas que contienen tensores cero, listas para tareas de procesamiento y generación. |