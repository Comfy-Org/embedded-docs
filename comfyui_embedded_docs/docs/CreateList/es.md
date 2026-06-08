El nodo Crear Lista combina múltiples entradas en una única lista secuencial. Toma cualquier número de entradas del mismo tipo de datos y las concatena en el orden en que están conectadas. Este nodo es útil para preparar lotes de datos, como imágenes o texto, para ser procesados por otros nodos en un flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `input_*` | Un número variable de ranuras de entrada. Puedes agregar más entradas haciendo clic en el icono de suma (+). Todas las entradas deben ser del mismo tipo de datos (por ejemplo, todas IMAGE o todas STRING). | Varía | Sí | Cualquiera |

**Nota:** El nodo creará automáticamente nuevas ranuras de entrada a medida que conectes elementos. Todas las entradas conectadas deben compartir el mismo tipo de datos para que el nodo funcione correctamente.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `list` | Una única lista que contiene todos los elementos de las entradas conectadas, concatenados en el orden en que fueron proporcionados. El tipo de dato de salida coincide con el tipo de dato de entrada. | Varía |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/es.md)

---
**Source fingerprint (SHA-256):** `d0e10c4d1186e694a72b18407c34cc1df74f77d02c989b507af75594c1a0794e`
