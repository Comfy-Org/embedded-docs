> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/es.md)

El nodo TrainLoraNode crea y entrena un modelo LoRA (Adaptación de Bajo Rango) en un modelo de difusión utilizando latentes y datos de condicionamiento proporcionados. Permite ajustar un modelo con parámetros de entrenamiento personalizados, optimizadores y funciones de pérdida. El nodo genera los pesos LoRA entrenados, un mapa del historial de pérdidas y el total de pasos de entrenamiento completados.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo sobre el cual entrenar el LoRA. |
| `latentes` | LATENT | Sí | - | Los Latentes a utilizar para el entrenamiento, funcionan como conjunto de datos/entrada del modelo. |
| `positivo` | CONDITIONING | Sí | - | El condicionamiento positivo a utilizar para el entrenamiento. |
| `tamaño_lote` | INT | Sí | 1-10000 | El tamaño de lote a utilizar para el entrenamiento (predeterminado: 1). |
| `pasos_acumulación_gradiente` | INT | Sí | 1-1024 | El número de pasos de acumulación de gradiente a utilizar para el entrenamiento (predeterminado: 1). |
| `pasos` | INT | Sí | 1-100000 | El número de pasos para entrenar el LoRA (predeterminado: 16). |
| `tasa_aprendizaje` | FLOAT | Sí | 0.0000001-1.0 | La tasa de aprendizaje a utilizar para el entrenamiento (predeterminado: 0.0005). |
| `rango` | INT | Sí | 1-128 | El rango de las capas LoRA (predeterminado: 8). |
| `optimizador` | COMBO | Sí | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" | El optimizador a utilizar para el entrenamiento (predeterminado: "AdamW"). |
| `función_pérdida` | COMBO | Sí | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" | La función de pérdida a utilizar para el entrenamiento (predeterminado: "MSE"). |
| `semilla` | INT | Sí | 0-18446744073709551615 | La semilla a utilizar para el entrenamiento (utilizada en el generador para la inicialización de pesos LoRA y el muestreo de ruido) (predeterminado: 0). |
| `tipo_datos_entrenamiento` | COMBO | Sí | "bf16"<br>"fp32"<br>"none" | El tipo de dato a utilizar para el entrenamiento. 'none' preserva el tipo de dato de cómputo nativo del modelo en lugar de sobrescribirlo. Para modelos fp16, GradScaler se habilita automáticamente (predeterminado: "bf16"). |
| `tipo_datos_lora` | COMBO | Sí | "bf16"<br>"fp32" | El tipo de dato a utilizar para el LoRA (predeterminado: "bf16"). |
| `quantized_backward` | BOOLEAN | Sí | - | Al usar training_dtype 'none' y entrenar en un modelo cuantizado, realiza la retropropagación con multiplicación de matrices cuantizada cuando está habilitado (predeterminado: False). |
| `algoritmo` | COMBO | Sí | Múltiples opciones disponibles | El algoritmo a utilizar para el entrenamiento. |
| `verificación_gradiente` | BOOLEAN | Sí | - | Usar puntos de control de gradiente para el entrenamiento (predeterminado: True). |
| `checkpoint_depth` | INT | Sí | 1-5 | Nivel de profundidad para los puntos de control de gradiente (predeterminado: 1). |
| `offloading` | BOOLEAN | Sí | - | Descargar los pesos del modelo a la CPU durante el entrenamiento para ahorrar memoria de GPU (predeterminado: False). |
| `lora_existente` | COMBO | Sí | Múltiples opciones disponibles | El LoRA existente al que añadir. Establecer en None para un nuevo LoRA (predeterminado: "[None]"). |
| `bucket_mode` | BOOLEAN | Sí | - | Habilitar el modo de cubeta de resolución. Cuando está habilitado, espera latentes pre-agrupados en cubetas del nodo ResolutionBucket (predeterminado: False). |
| `bypass_mode` | BOOLEAN | Sí | - | Habilitar el modo de derivación para el entrenamiento. Cuando está habilitado, los adaptadores se aplican mediante hooks directos en lugar de modificación de pesos. Útil para modelos cuantizados donde los pesos no se pueden modificar directamente (predeterminado: False). |

**Nota:** El número de entradas de condicionamiento positivo debe coincidir con el número de imágenes latentes. Si solo se proporciona un condicionamiento positivo con múltiples imágenes, se repetirá automáticamente para todas las imágenes.

**Nota sobre `training_dtype`:** Cuando se establece en "none", se preserva el tipo de dato de cómputo nativo del modelo. Para modelos fp16, GradScaler se habilita automáticamente para evitar el subdesbordamiento durante el cálculo del gradiente. Si `fp16_accumulation` también está habilitado (a través de las banderas `--fast`), esta combinación puede ser numéricamente inestable y puede causar valores NaN.

**Nota sobre `quantized_backward`:** Este parámetro solo es relevante cuando `training_dtype` está establecido en "none" y el modelo es un modelo cuantizado. Habilita la multiplicación de matrices cuantizada durante el paso de retropropagación.

**Nota sobre `bypass_mode`:** Cuando está habilitado, los adaptadores se aplican mediante hooks directos en lugar de modificar los pesos del modelo directamente. Esto es particularmente útil para modelos cuantizados donde los pesos no se pueden modificar directamente.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `mapa_de_pérdida` | LORA_MODEL | Los pesos LoRA entrenados que se pueden guardar o aplicar a otros modelos. |
| `pasos` | LOSS_MAP | Un diccionario que contiene los valores de pérdida del entrenamiento a lo largo del tiempo. |
| `pasos` | INT | El número total de pasos de entrenamiento completados (incluyendo cualquier paso anterior de un LoRA existente). |

---
**Source fingerprint (SHA-256):** `df315ef416ff3ce81e6a526af2c4e5115980e6c35830825967e7189d4f8541d8`
