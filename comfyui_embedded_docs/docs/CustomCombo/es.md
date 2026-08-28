# Combinación personalizada

El nodo Custom Combo le permite crear un menú desplegable personalizado con su propia lista de opciones de texto. Es un nodo centrado en el frontend que incluye una representación en el backend para mantener la compatibilidad con su flujo de trabajo. Cuando selecciona una opción del menú desplegable, el nodo emite ese texto como una cadena y su posición de índice.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `elección` | La opción de texto seleccionada en el menú desplegable personalizado. La lista de opciones disponibles la define el usuario en la interfaz frontend del nodo. | COMBO | Sí | Definido por el usuario |
| `index` | Un valor entero que se puede utilizar para especificar un índice. Por defecto: 0. | INT | No | Cualquier entero (por defecto: 0) |

**Nota:** La validación de las entradas de este nodo está deshabilitada intencionalmente. Esto le permite escribir cualquier opción de texto personalizada en el frontend sin que el backend verifique si su selección coincide con una lista predefinida. Los widgets distintos del menú desplegable del combo se definen completamente en el frontend. Este nodo está marcado como experimental.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `STRING` | La cadena de texto de la opción seleccionada en el cuadro combinado personalizado. | STRING |
| `ÍNDICE` | La posición de índice de la opción seleccionada en la lista desplegable. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/es.md)

---
**Source fingerprint (SHA-256):** `143eafcf32de7ebaf72b5387537154b5deee7d3e3a520a0b2c12ac4fb67890f8`
