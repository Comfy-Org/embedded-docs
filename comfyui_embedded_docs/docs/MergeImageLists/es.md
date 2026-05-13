> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeImageLists/es.md)

El nodo Combinar Listas de Imágenes fusiona múltiples listas separadas de imágenes en una única lista continua. Funciona tomando todas las imágenes de cada entrada conectada y concatenándolas en el orden en que se reciben. Esto es útil para organizar o agrupar imágenes de diferentes fuentes para su procesamiento posterior.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `imágenes` | IMAGE | Sí | - | Una lista de imágenes que se fusionarán. Esta entrada puede aceptar múltiples conexiones, y cada lista conectada se concatenará en la salida final. |

**Nota:** Este nodo está diseñado para recibir múltiples entradas. Puedes conectar varias listas de imágenes a un único conector de entrada `images`. El nodo concatenará automáticamente todas las imágenes de todas las listas conectadas en una única lista de salida.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `imágenes` | IMAGE | La única lista fusionada que contiene todas las imágenes de cada lista de entrada conectada. |

---
**Source fingerprint (SHA-256):** `8fc53091b817a5036aae022aa841ba11fae0ed3242a969f5ae9072f48e061366`
