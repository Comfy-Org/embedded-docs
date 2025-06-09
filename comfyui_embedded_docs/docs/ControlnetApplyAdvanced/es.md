Este nodo ha sido renombrado a Aplicar ControlNet en la nueva versión de ComfyUI, reemplazando la versión anterior llamada Aplicar ControlNet (ANTIGUO). Dado que el anterior Aplicar ControlNet (ANTIGUO) es actualmente algo similar a un estado habilitado, la documentación más reciente para este nodo se ha trasladado a `Aplicar ControlNet` para mayor claridad.

Este nodo aplica transformaciones avanzadas de control net a los datos de acondicionamiento basados en una imagen y un modelo de control net. Permite ajustes precisos de la influencia del control net sobre el contenido generado, habilitando modificaciones más precisas y variadas al acondicionamiento.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | Los datos de acondicionamiento positivo a los que se aplicarán las transformaciones de control net. Representa los atributos o características deseadas para mejorar o mantener en el contenido generado. |
| `negative` | `CONDITIONING` | Los datos de acondicionamiento negativo, que representan atributos o características a disminuir o eliminar del contenido generado. Las transformaciones de control net también se aplican a estos datos, permitiendo un ajuste equilibrado de las características del contenido. |
| `control_net` | `CONTROL_NET` | El modelo de control net es crucial para definir los ajustes y mejoras específicos a los datos de acondicionamiento. Interpreta la imagen de referencia y los parámetros de fuerza para aplicar transformaciones, influyendo significativamente en el resultado final al modificar atributos en los datos de acondicionamiento tanto positivos como negativos. |
| `image` | `IMAGE` | La imagen que sirve como referencia para las transformaciones de control net. Influye en los ajustes realizados por el control net a los datos de acondicionamiento, guiando la mejora o supresión de características específicas. |
| `strength` | `FLOAT` | Un valor escalar que determina la intensidad de la influencia del control net sobre los datos de acondicionamiento. Valores más altos resultan en ajustes más pronunciados. |
| `start_percent` | `FLOAT` | El porcentaje inicial del efecto del control net, permitiendo la aplicación gradual de transformaciones sobre un rango especificado. |
| `end_percent` | `FLOAT` | El porcentaje final del efecto del control net, definiendo el rango sobre el cual se aplican las transformaciones. Esto permite un control más matizado sobre el proceso de ajuste. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | Los datos de acondicionamiento positivo modificados después de la aplicación de transformaciones de control net, reflejando las mejoras realizadas basadas en los parámetros de entrada. |
| `negative` | `CONDITIONING` | Los datos de acondicionamiento negativo modificados después de la aplicación de transformaciones de control net, reflejando la supresión o eliminación de características específicas basadas en los parámetros de entrada. |
