> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/es.md)

El nodo TripleCLIPLoader carga tres modelos de codificador de texto diferentes simultáneamente y los combina en un único modelo CLIP. Esto es útil para escenarios avanzados de codificación de texto donde se necesitan múltiples codificadores de texto, como en flujos de trabajo SD3 que requieren que los modelos clip-l, clip-g y t5 trabajen juntos.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `clip_name1` | STRING | Sí | Varias opciones disponibles | El primer modelo de codificador de texto a cargar de entre los codificadores de texto disponibles |
| `clip_name2` | STRING | Sí | Varias opciones disponibles | El segundo modelo de codificador de texto a cargar de entre los codificadores de texto disponibles |
| `clip_name3` | STRING | Sí | Varias opciones disponibles | El tercer modelo de codificador de texto a cargar de entre los codificadores de texto disponibles |

**Nota:** Los tres parámetros del codificador de texto deben seleccionarse de entre los modelos de codificador de texto disponibles en su sistema. El nodo cargará los tres modelos y los combinará en un único modelo CLIP para su procesamiento.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `CLIP` | CLIP | Un modelo CLIP combinado que contiene los tres codificadores de texto cargados |

---
**Source fingerprint (SHA-256):** `7a9e61090d9d3b0a776d49006dddece08bc4b463b2acd0a9a0f808170ebde348`
