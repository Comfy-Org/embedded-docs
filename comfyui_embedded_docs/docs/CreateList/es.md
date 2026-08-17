# Crear lista

El nodo Create List combina múltiples entradas en una única lista secuencial. Toma cualquier número de entradas del mismo tipo de datos y las concatena en el orden en que están conectadas. Este nodo es útil para preparar lotes de datos, como imágenes o texto, para que sean procesados por otros nodos en un flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `inputs` | Un conjunto ampliable de ranuras de entrada. Agrega más ranuras haciendo clic en el icono de más (+), o conecta elementos y se crean nuevas ranuras automáticamente. Cada ranura acepta uno o más elementos, y todas las ranuras deben compartir el mismo tipo de datos (por ejemplo, todas IMAGE o todas STRING). | Varía (coincide con el tipo de datos conectado) | Sí | Cualquier número de ranuras; cada ranura acepta uno o más elementos |

**Nota:** El nodo crea automáticamente nuevas ranuras de entrada a medida que conectas elementos. Todas las entradas conectadas deben compartir el mismo tipo de datos para que el nodo funcione correctamente, y la lista de salida adopta ese mismo tipo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `list` | Una única lista que contiene todos los elementos de las ranuras de entrada conectadas, concatenados en el orden en que están conectadas las ranuras. El tipo de datos de salida coincide con el tipo de datos de entrada. | Varía (coincide con el tipo de datos de entrada) |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/es.md)

---
**Source fingerprint (SHA-256):** `457d17da815ef9cee000d9e8dc8768f19ddfe247feae4b2ff4ce3c6cc0fd564e`
