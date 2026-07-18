El nodo Combo Personalizado te permite crear un menú desplegable personalizado con tu propia lista de opciones de texto. Es un nodo centrado en el frontend que proporciona una representación en el backend para garantizar la compatibilidad dentro de tu flujo de trabajo. Cuando seleccionas una opción del menú desplegable, el nodo genera ese texto como una cadena y su posición de índice.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `elección` | La opción de texto seleccionada del menú desplegable personalizado. La lista de opciones disponibles es definida por el usuario en la interfaz del frontend del nodo. | COMBO | Sí | Definido por el usuario |
| `index` | Un valor entero que se puede usar para especificar un índice. Valor predeterminado: 0. | INT | No | 0 |

**Nota:** La validación para la entrada de este nodo está intencionalmente deshabilitada. Esto te permite definir cualquier opción de texto personalizada que desees en el frontend sin que el backend verifique si tu selección proviene de una lista predefinida.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `ÍNDICE` | La cadena de texto de la opción seleccionada del cuadro combinado personalizado. | STRING |
| `ÍNDICE` | La posición de índice de la opción seleccionada en la lista desplegable. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/es.md)

---
**Source fingerprint (SHA-256):** `d950207b94deee37abce294eb3dab035e622925dc1118fe37f9c874784dc1672`
