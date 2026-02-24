> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/es.md)

Este nodo es una prueba para la función de entrada Autogrow. Toma un número dinámico de entradas de tipo FLOAT, cada una etiquetada con un nombre específico, y combina sus valores en una única cadena separada por comas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `autogrow` | FLOAT | Sí | N/A | Un grupo de entrada dinámico. Puedes añadir múltiples entradas FLOAT, cada una con un nombre predefinido de la lista: "a", "b" o "c". El nodo aceptará cualquier combinación de estas entradas nombradas. |

**Nota:** La entrada `autogrow` es dinámica. Puedes añadir o eliminar entradas FLOAT individuales (nombradas "a", "b" o "c") según sea necesario para tu flujo de trabajo. El nodo procesa todos los valores proporcionados.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | STRING | Una única cadena que contiene los valores de todas las entradas FLOAT proporcionadas, unidos por comas. |
