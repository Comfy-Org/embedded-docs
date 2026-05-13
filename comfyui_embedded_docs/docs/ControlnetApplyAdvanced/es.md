> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplyAdvanced/es.md)

Este nodo aplica transformaciones avanzadas de red de control a datos de condicionamiento basándose en una imagen y un modelo de red de control. Permite ajustes precisos de la influencia de la red de control sobre el contenido generado, posibilitando modificaciones más exactas y variadas al condicionamiento.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | Los datos de condicionamiento positivo a los que se aplicarán las transformaciones de la red de control. Representa los atributos o características deseadas para mejorar o mantener en el contenido generado. |
| `negative` | `CONDITIONING` | Los datos de condicionamiento negativo, que representan atributos o características a disminuir o eliminar del contenido generado. Las transformaciones de la red de control también se aplican a estos datos, permitiendo un ajuste equilibrado de las características del contenido. |
| `control_net` | `CONTROL_NET` | El modelo de red de control es fundamental para definir los ajustes y mejoras específicos en los datos de condicionamiento. Interpreta la imagen de referencia y los parámetros de intensidad para aplicar transformaciones, influyendo significativamente en el resultado final al modificar atributos tanto en los datos de condicionamiento positivo como negativo. |
| `image` | `IMAGE` | La imagen que sirve como referencia para las transformaciones de la red de control. Influye en los ajustes que realiza la red de control sobre los datos de condicionamiento, guiando la mejora o supresión de características específicas. |
| `strength` | `FLOAT` | Un valor escalar que determina la intensidad de la influencia de la red de control sobre los datos de condicionamiento. Valores más altos resultan en ajustes más pronunciados. |
| `start_percent` | `FLOAT` | El porcentaje inicial del efecto de la red de control, permitiendo la aplicación gradual de transformaciones en un rango especificado. |
| `end_percent` | `FLOAT` | El porcentaje final del efecto de la red de control, que define el rango sobre el cual se aplican las transformaciones. Esto permite un control más matizado del proceso de ajuste. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | Los datos de condicionamiento positivo modificados tras la aplicación de las transformaciones de la red de control, reflejando las mejoras realizadas según los parámetros de entrada. |
| `negative` | `CONDITIONING` | Los datos de condicionamiento negativo modificados tras la aplicación de las transformaciones de la red de control, reflejando la supresión o eliminación de características específicas según los parámetros de entrada. |