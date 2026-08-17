# Combinación personalizada

El nodo Custom Combo te permite crear un menú desplegable personalizado con tu propia lista de opciones de texto. Es un nodo orientado al frontend que proporciona una representación en el backend para garantizar la compatibilidad dentro de tu flujo de trabajo. Cuando seleccionas una opción del menú desplegable, el nodo genera ese texto como una cadena y su posición de índice.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `choice` | La opción de texto seleccionada en el menú desplegable personalizado. La lista de opciones disponibles está definida por el usuario en la interfaz de frontend del nodo. | COMBO | Sí | Definido por el usuario |
| `index` | Un valor entero que se puede usar para especificar un índice. Predeterminado: 0. | INT | No | Cualquier entero |

**Nota:** La validación para la entrada de este nodo está deshabilitada intencionalmente. Esto te permite definir cualquier opción de texto personalizada que desees en el frontend sin que el backend verifique si tu selección proviene de una lista predefinida. Este nodo está marcado como experimental.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `STRING` | La cadena de texto de la opción seleccionada en el menú desplegable personalizado. | STRING |
| `INDEX` | La posición de índice de la opción seleccionada en la lista desplegable. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/es.md)

---
**Source fingerprint (SHA-256):** `143eafcf32de7ebaf72b5387537154b5deee7d3e3a520a0b2c12ac4fb67890f8`
