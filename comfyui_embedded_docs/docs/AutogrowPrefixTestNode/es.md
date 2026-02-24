> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/es.md)

El AutogrowPrefixTestNode es un nodo lógico diseñado para probar la función de entrada de crecimiento automático. Acepta un número dinámico de entradas de tipo float, combina sus valores en una cadena separada por comas y emite esa cadena.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `autogrow` | AUTOGROW | Sí | De 1 a 10 entradas | Un grupo de entrada dinámico que puede aceptar entre 1 y 10 valores de tipo float. Cada entrada en el grupo es de tipo FLOAT. |

**Nota:** La entrada `autogrow` es una entrada dinámica especial. Puedes añadir múltiples entradas float a este grupo, hasta un máximo de 10. El nodo procesará todos los valores proporcionados.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | STRING | Una única cadena que contiene todos los valores float de entrada, separados por comas. |
