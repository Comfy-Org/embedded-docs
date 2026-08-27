# AutogrowNamesTestNode

Este nodo es una prueba de la función de entrada Autogrow. Acepta un número dinámico de entradas de tipo float, cada una etiquetada con un nombre específico, y combina sus valores en una sola cadena separada por comas.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `autogrow` | Un grupo de entradas dinámico. Puede agregar múltiples entradas de tipo float, cada una con un nombre predefinido de la lista: "a", "b" o "c". El nodo aceptará cualquier combinación de estas entradas con nombre. | FLOAT | Sí | N/A |

**Nota:** La entrada `autogrow` es dinámica. Puede agregar o eliminar entradas de tipo float individuales (llamadas "a", "b" o "c") según sea necesario para su flujo de trabajo. El nodo procesa todos los valores proporcionados.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `output` | Una sola cadena que contiene los valores de todas las entradas de tipo float proporcionadas, unidas con comas. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/es.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`
