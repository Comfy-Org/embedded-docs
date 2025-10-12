> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/es.md)

El LossGraphNode crea un gráfico visual de los valores de pérdida del entrenamiento a lo largo del tiempo y lo guarda como un archivo de imagen. Toma datos de pérdida de procesos de entrenamiento y genera un gráfico de líneas que muestra cómo cambia la pérdida a través de los pasos de entrenamiento. El gráfico resultante incluye etiquetas de ejes, valores mínimos/máximos de pérdida, y se guarda automáticamente en el directorio temporal de salida con una marca de tiempo.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `loss` | LOSS | Sí | Múltiples opciones disponibles | Los datos de pérdida que contienen los valores a graficar (valor por defecto: diccionario vacío) |
| `filename_prefix` | STRING | Sí | - | El prefijo para el nombre del archivo de imagen de salida (valor por defecto: "loss_graph") |

**Nota:** El parámetro `loss` requiere un diccionario de pérdida válido que contenga una clave "loss" con valores de pérdida. El nodo escala automáticamente los valores de pérdida para ajustarse a las dimensiones del gráfico y genera un gráfico de líneas que muestra la progresión de la pérdida a lo largo de los pasos de entrenamiento.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `ui.images` | IMAGE | La imagen del gráfico de pérdida generada guardada en el directorio temporal |
