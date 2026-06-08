El nodo LotusConditioning proporciona embeddings de condicionamiento precalculados para el modelo Lotus. Utiliza un codificador congelado con condicionamiento nulo y devuelve embeddings de prompt fijos para lograr paridad con la implementación de referencia sin necesidad de inferencia ni cargar archivos grandes de tensores. Este nodo genera un tensor de condicionamiento fijo que puede usarse directamente en el pipeline de generación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| *Sin entradas* | Este nodo no acepta ningún parámetro de entrada. | - | - | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `conditioning` | Los embeddings de condicionamiento precalculados para el modelo Lotus, que contienen embeddings de prompt fijos y un diccionario vacío. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/es.md)

---
**Source fingerprint (SHA-256):** `aa428f8c355e2840dadbf634fe27d20c7c323dbe8c21255b40f4dafa12e4a0d0`
