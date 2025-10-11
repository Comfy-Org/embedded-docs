> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/es.md)

El TrainLoraNode crea y entrena un modelo LoRA (Low-Rank Adaptation) en un modelo de difusión utilizando latentes y datos de condicionamiento proporcionados. Permite ajustar un modelo con parámetros de entrenamiento personalizados, optimizadores y funciones de pérdida. El nodo genera como salida el modelo entrenado con LoRA aplicado, los pesos LoRA, métricas de pérdida de entrenamiento y el total de pasos de entrenamiento completados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo sobre el cual entrenar el LoRA. |
| `latents` | LATENT | Sí | - | Los latentes a utilizar para el entrenamiento, sirven como conjunto de datos/entrada del modelo. |
| `positive` | CONDITIONING | Sí | - | El condicionamiento positivo a utilizar para el entrenamiento. |
| `batch_size` | INT | Sí | 1-10000 | El tamaño del lote a utilizar para el entrenamiento (valor por defecto: 1). |
| `grad_accumulation_steps` | INT | Sí | 1-1024 | El número de pasos de acumulación de gradiente a utilizar para el entrenamiento (valor por defecto: 1). |
| `steps` | INT | Sí | 1-100000 | El número de pasos para entrenar el LoRA (valor por defecto: 16). |
| `learning_rate` | FLOAT | Sí | 0.0000001-1.0 | La tasa de aprendizaje a utilizar para el entrenamiento (valor por defecto: 0.0005). |
| `rank` | INT | Sí | 1-128 | El rango de las capas LoRA (valor por defecto: 8). |
| `optimizer` | COMBO | Sí | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" | El optimizador a utilizar para el entrenamiento (valor por defecto: "AdamW"). |
| `loss_function` | COMBO | Sí | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" | La función de pérdida a utilizar para el entrenamiento (valor por defecto: "MSE"). |
| `seed` | INT | Sí | 0-18446744073709551615 | La semilla a utilizar para el entrenamiento (utilizada en el generador para la inicialización de pesos LoRA y el muestreo de ruido) (valor por defecto: 0). |
| `training_dtype` | COMBO | Sí | "bf16"<br>"fp32" | El tipo de dato a utilizar para el entrenamiento (valor por defecto: "bf16"). |
| `lora_dtype` | COMBO | Sí | "bf16"<br>"fp32" | El tipo de dato a utilizar para el LoRA (valor por defecto: "bf16"). |
| `algorithm` | COMBO | Sí | Múltiples opciones disponibles | El algoritmo a utilizar para el entrenamiento. |
| `gradient_checkpointing` | BOOLEAN | Sí | - | Utilizar checkpointing de gradiente para el entrenamiento (valor por defecto: True). |
| `existing_lora` | COMBO | Sí | Múltiples opciones disponibles | El LoRA existente al cual añadir. Establecer a None para un nuevo LoRA (valor por defecto: "[None]"). |

**Nota:** El número de entradas de condicionamiento positivo debe coincidir con el número de imágenes latentes. Si solo se proporciona un condicionamiento positivo con múltiples imágenes, se repetirá automáticamente para todas las imágenes.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model_with_lora` | MODEL | El modelo original con el LoRA entrenado aplicado. |
| `lora` | LORA_MODEL | Los pesos LoRA entrenados que pueden guardarse o aplicarse a otros modelos. |
| `loss` | LOSS_MAP | Un diccionario que contiene los valores de pérdida de entrenamiento a lo largo del tiempo. |
| `steps` | INT | El número total de pasos de entrenamiento completados (incluyendo cualquier paso previo de un LoRA existente). |