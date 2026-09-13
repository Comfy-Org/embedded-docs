# AutogrowNamesTestNode

Este nodo es una prueba de la función de entrada Autogrow. Acepta un grupo dinámico de entradas de tipo float, cada una con un nombre predefinido, y combina sus valores en una única cadena separada por comas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `autogrow` | Un grupo de entrada dinámico. Puedes agregar múltiples entradas de tipo float, cada una con un nombre predefinido de la lista: "a", "b" o "c". El nodo acepta cualquier combinación de estas entradas con nombre. | FLOAT | Sí | Ranuras nombradas: `a`, `b`, `c` |

**Nota:** La entrada `autogrow` es dinámica. Las entradas float individuales llamadas "a", "b" y "c" se pueden agregar o quitar según sea necesario. Todos los valores proporcionados son procesados por el nodo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | Una única cadena que contiene los valores de todas las entradas float proporcionadas, unidos entre sí por comas. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/es.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`
