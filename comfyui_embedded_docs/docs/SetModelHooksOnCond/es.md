> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/es.md)

Este nodo adjunta hooks personalizados a los datos de condicionamiento, permitiéndole interceptar y modificar el proceso de condicionamiento durante la ejecución del modelo. Toma un conjunto de hooks y los aplica a los datos de condicionamiento proporcionados, permitiendo una personalización avanzada del flujo de trabajo de generación de texto a imagen. El condicionamiento modificado con los hooks adjuntos se devuelve para su uso en pasos de procesamiento posteriores.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Sí | - | Los datos de condicionamiento a los que se adjuntarán los hooks |
| `hooks` | HOOKS | Sí | - | Las definiciones de hooks que se aplicarán a los datos de condicionamiento |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Los datos de condicionamiento modificados con hooks adjuntos |