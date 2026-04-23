> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/es.md)

El nodo Editor de Curvas proporciona una interfaz visual para ajustar y afinar una curva. Permite modificar la forma de una curva de entrada y, opcionalmente, visualizar su distribución con un histograma. El nodo devuelve la curva modificada para su uso en otras partes de su flujo de trabajo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `curve` | CURVE | Sí | N/A | La curva de entrada que se va a editar. |
| `histogram` | HISTOGRAM | No | N/A | Un histograma opcional para mostrar junto a la curva como referencia visual. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `curve` | CURVE | La curva editada después de realizar los ajustes en la interfaz del nodo. |