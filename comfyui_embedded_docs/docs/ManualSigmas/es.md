> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/es.md)

El nodo ManualSigmas permite definir manualmente una secuencia personalizada de niveles de ruido (sigmas) para el proceso de muestreo. Se introduce una lista de números como una cadena de texto, y el nodo los convierte en un tensor que puede ser utilizado por otros nodos de muestreo. Esto es útil para pruebas o para crear programaciones de ruido específicas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | STRING | Sí | Cualquier número separado por comas o espacios | Una cadena de texto que contiene los valores sigma. El nodo extraerá todos los números de esta cadena. Por ejemplo, "1, 0.5, 0.1" o "1 0.5 0.1". El valor por defecto es "1, 0.5". |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | El tensor que contiene la secuencia de valores sigma extraídos de la cadena de entrada. |
