# LotusConditioning

El nodo `LotusConditioning` proporciona embeddings de condicionamiento precomputados para el modelo Lotus. Utiliza un codificador congelado con condicionamiento nulo y devuelve embeddings de prompt codificados para lograr paridad con la implementación de referencia sin requerir inferencia ni cargar archivos tensor grandes. Este nodo genera un tensor de condicionamiento fijo que se puede usar directamente en el pipeline de generación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| *Sin entradas* | Este nodo no acepta ningún parámetro de entrada. | - | - | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `conditioning` | Los embeddings de condicionamiento precomputados para el modelo Lotus, que contienen embeddings de prompt fijos y un diccionario vacío. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/es.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`
