# AutogrowNamesTestNode

Este nodo es una prueba de la función de entrada Autogrow. Acepta un número dinámico de entradas flotantes, cada una etiquetada con un nombre específico, y combina sus valores en una sola cadena separada por comas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `autogrow` | Un grupo de entrada dinámico. Puede agregar varias entradas flotantes, cada una con un nombre predefinido de la lista: "a", "b" o "c". El nodo aceptará cualquier combinación de estas entradas nombradas. | FLOAT | Sí | N/A |

**Nota:** La entrada `autogrow` es dinámica. Puede agregar o quitar entradas flotantes individuales (denominadas "a", "b" o "c") según sea necesario para su flujo de trabajo. El nodo procesa todos los valores proporcionados.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | Una sola cadena que contiene los valores de todas las entradas flotantes proporcionadas, unidos con comas. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/es.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`
