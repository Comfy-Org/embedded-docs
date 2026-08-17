# Cargador Triple CLIP

El nodo TripleCLIPLoader carga tres modelos de codificador de texto al mismo tiempo y los combina en un único modelo CLIP. Esto es útil para escenarios avanzados de codificación de texto donde se necesitan múltiples codificadores de texto, como en flujos de trabajo SD3 que requieren que los modelos clip-l, clip-g y t5 trabajen juntos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `clip_name1` | El primer modelo de codificador de texto que se carga entre los codificadores de texto disponibles | COMBO | Sí | Todos los archivos de codificador de texto en la carpeta text_encoders |
| `clip_name2` | El segundo modelo de codificador de texto que se carga entre los codificadores de texto disponibles | COMBO | Sí | Todos los archivos de codificador de texto en la carpeta text_encoders |
| `clip_name3` | El tercer modelo de codificador de texto que se carga entre los codificadores de texto disponibles | COMBO | Sí | Todos los archivos de codificador de texto en la carpeta text_encoders |

**Nota:** Los tres parámetros de codificador de texto deben seleccionarse entre los modelos de codificador de texto disponibles en tu sistema. El nodo carga los tres modelos en el orden indicado y los combina en un único modelo CLIP para su procesamiento. Para flujos de trabajo SD3, usa clip-l, clip-g y t5 como los tres codificadores.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-----------|-------------|-----------|
| `CLIP` | Un modelo CLIP combinado que contiene los tres codificadores de texto cargados | CLIP |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/es.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`
