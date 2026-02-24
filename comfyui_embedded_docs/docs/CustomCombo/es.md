> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/es.md)

El nodo Custom Combo (Combinación Personalizada) te permite crear un menú desplegable personalizado con tu propia lista de opciones de texto. Es un nodo enfocado en el frontend que proporciona una representación en el backend para garantizar la compatibilidad dentro de tu flujo de trabajo. Cuando seleccionas una opción del menú desplegable, el nodo emite ese texto como una cadena.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `choice` | COMBO | Sí | Definido por el usuario | La opción de texto seleccionada del menú desplegable personalizado. La lista de opciones disponibles la define el usuario en la interfaz de frontend del nodo. |

**Nota:** La validación para la entrada de este nodo está intencionalmente deshabilitada. Esto te permite definir cualquier opción de texto personalizada que desees en el frontend sin que el backend verifique si tu selección proviene de una lista predefinida.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | STRING | La cadena de texto de la opción seleccionada en el cuadro combinado personalizado. |
