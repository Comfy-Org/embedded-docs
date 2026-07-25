# TextEncodeMageFlowEdit

Este nodo codifica una instrucción de edición (prompt) junto con una o más imágenes de referencia para el modelo Mage-Flow-Edit. Redimensiona todas las imágenes de referencia a la resolución de salida objetivo, las codifica en el espacio latente si se proporciona un VAE, y adjunta los latentes de referencia a la salida de condicionamiento. También se genera un tensor latente en blanco con las dimensiones correctas para el muestreo, garantizando que el tamaño coincida siempre con el ancho y alto de salida.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `clip` | El modelo CLIP utilizado para tokenizar y codificar los prompts de texto. | CLIP | Sí | |
| `prompt` | La instrucción de edición (prompt positivo) a aplicar. | STRING | Sí | multilínea, prompts dinámicos activados |
| `negative_prompt` | El prompt negativo para alejarse de él. Valor predeterminado: cadena vacía (internamente se usa un espacio cuando está en blanco). | STRING | No | multilínea, prompts dinámicos activados |
| `vae` | Modelo VAE para codificar las imágenes de referencia en el espacio latente. Si no se proporciona, no se añaden latentes de referencia al condicionamiento. | VAE | No | |
| `images` | Una o más imágenes de referencia para editar. Todas las imágenes se redimensionan a la resolución de salida antes de codificarlas. | IMAGE (crecimiento automático) | No | Hasta 16 imágenes (nombradas `image_1`…`image_16`), al menos 0 |
| `width` | Ancho de salida en píxeles. Si se establece en 0, se utiliza el ancho de la primera imagen de referencia. Siempre se redondea hacia abajo a un múltiplo de 16. Valor predeterminado: 0. | INT | Sí | 0 a 8192 (paso 16) |
| `height` | Alto de salida en píxeles. Mismo comportamiento de respaldo que el ancho. Valor predeterminado: 0. | INT | Sí | 0 a 8192 (paso 16) |
| `batch_size` | Número de muestras latentes a generar. Valor predeterminado: 1. | INT | Sí | 1 a 4096 |

**Notas sobre dependencias de parámetros:**
- Si `width` y/o `height` son 0 y no se proporcionan imágenes de referencia, se usan 1024 cada uno como valor de respaldo.
- El parámetro `vae` es opcional; los latentes de referencia solo se generan y se adjuntan al condicionamiento cuando se conecta un VAE.
- El campo `negative_prompt` es opcional; si se deja vacío, internamente se usa un espacio como texto negativo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positive` | Salida de condicionamiento que contiene los tokens del prompt positivo, más (si se proporcionó un VAE) los latentes de referencia codificados. | CONDITIONING |
| `negative` | Salida de condicionamiento que contiene los tokens del prompt negativo, más los mismos latentes de referencia (si se proporcionó un VAE). | CONDITIONING |
| `latent` | Un tensor latente en blanco con forma `[batch_size, 128, height÷16, width÷16]` para usar como ruido inicial durante el muestreo. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMageFlowEdit/es.md)

---
**Source fingerprint (SHA-256):** `880d8856b7f6e656bc68ca953fbf892898d05bc5d65290ae3bf7a4405ee09be3`
