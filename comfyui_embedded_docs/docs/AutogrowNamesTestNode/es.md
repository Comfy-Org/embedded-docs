# AutogrowNamesTestNode

Este nodo es una prueba para la funcionalidad de entrada Autogrow. Toma un número dinámico de entradas de tipo float, cada una etiquetada con un nombre específico, y combina sus valores en una sola cadena de texto separada por comas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `autogrow` | Un grupo de entrada dinámico. Puedes agregar múltiples entradas float, cada una con un nombre predefinido de la lista: "a", "b" o "c". El nodo aceptará cualquier combinación de estas entradas nombradas. | FLOAT | Sí | N/A |

**Nota:** La entrada `autogrow` es dinámica. Puedes agregar o eliminar entradas float individuales (nombradas "a", "b" o "c") según sea necesario para tu flujo de trabajo. El nodo procesa todos los valores proporcionados.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | Una sola cadena de texto que contiene los valores de todas las entradas float proporcionadas, unidos con comas. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/es.md)

---
**Source fingerprint (SHA-256):** `33e8b2e2c369d06979415c31ef2623cff55d98ecf49137c5cafbeba7cc3b0451`
