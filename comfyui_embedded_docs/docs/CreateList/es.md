# Crear lista

El nodo Create List combina múltiples entradas en una única lista secuencial. Acepta cualquier número de entradas del mismo tipo de datos y las concatena en el orden en que están conectadas. Este nodo es útil para preparar lotes de datos, como imágenes o texto, para ser procesados por otros nodos en un flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `entradas` | Un número variable de ranuras de entrada denominadas `input`, `input_2`, `input_3`, y así sucesivamente. Cada ranura acepta una lista de elementos del mismo tipo de datos. Puede agregar más ranuras haciendo clic en el icono de más (+). Todas las ranuras deben usar el mismo tipo de datos (por ejemplo, todas IMAGE o todas STRING). | Varía | Sí | Cualquier número de ranuras; cada ranura acepta cualquier número de elementos |

**Nota:** El nodo crea automáticamente nuevas ranuras de entrada a medida que conecta elementos. Todas las entradas conectadas deben compartir el mismo tipo de datos para que el nodo funcione correctamente. Cada ranura conectada proporciona una lista de elementos, y el nodo combina las listas en el orden de las ranuras (`input`, luego `input_2`, luego `input_3`, ...). El nodo también se puede buscar con los alias "Image Iterator", "Text Iterator" e "Iterator".

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `lista` | Una única lista que contiene todos los elementos de las entradas conectadas, concatenados en el orden en que se proporcionaron. El tipo de datos de salida coincide con el tipo de datos de entrada. | Varía |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/es.md)

---
**Source fingerprint (SHA-256):** `457d17da815ef9cee000d9e8dc8768f19ddfe247feae4b2ff4ce3c6cc0fd564e`
