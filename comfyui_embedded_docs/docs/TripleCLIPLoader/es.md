> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/es.md)

El nodo TripleCLIPLoader carga tres modelos diferentes de codificación de texto simultáneamente y los combina en un único modelo CLIP. Esto es útil para escenarios avanzados de codificación de texto donde se necesitan múltiples codificadores de texto, como en los flujos de trabajo de SD3 que requieren que los modelos clip-l, clip-g y t5 trabajen juntos.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip_name1` | STRING | Sí | Múltiples opciones disponibles | El primer modelo de codificador de texto a cargar de los codificadores de texto disponibles |
| `clip_name2` | STRING | Sí | Múltiples opciones disponibles | El segundo modelo de codificador de texto a cargar de los codificadores de texto disponibles |
| `clip_name3` | STRING | Sí | Múltiples opciones disponibles | El tercer modelo de codificador de texto a cargar de los codificadores de texto disponibles |

**Nota:** Los tres parámetros de codificador de texto deben seleccionarse de los modelos de codificador de texto disponibles en su sistema. El nodo cargará los tres modelos y los combinará en un único modelo CLIP para su procesamiento.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Un modelo CLIP combinado que contiene los tres codificadores de texto cargados |