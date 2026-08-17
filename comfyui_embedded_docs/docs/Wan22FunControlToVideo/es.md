# Wan22FunControlToVideo

El nodo Wan22FunControlToVideo prepara las representaciones de condicionamiento y latentes para la generación de video utilizando la arquitectura del modelo de video Wan. Procesa entradas de condicionamiento positivo y negativo junto con imágenes de referencia opcionales y videos de control para crear las representaciones necesarias en el espacio latente para la síntesis de video. El nodo maneja el escalado espacial y las dimensiones temporales para generar datos de condicionamiento apropiados para los modelos de video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamiento positivo para guiar la generación de video | CONDITIONING | Sí | - |
| `negative` | Entrada de condicionamiento negativo para guiar la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar imágenes al espacio latente | VAE | Sí | - |
| `width` | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `height` | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `length` | Número de fotogramas en la secuencia de video (predeterminado: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `batch_size` | Número de secuencias de video a generar (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `ref_image` | Imagen de referencia opcional para proporcionar guía visual | IMAGE | No | - |
| `control_video` | Video de control opcional para guiar el proceso de generación | IMAGE | No | - |

**Nota:** El parámetro `length` se procesa en bloques de 4 fotogramas, y el nodo maneja automáticamente el escalado temporal para el espacio latente. Cuando se proporciona `ref_image`, influye en el condicionamiento a través de los latentes de referencia. Cuando se proporciona `control_video`, afecta directamente a la representación latente concatenada utilizada en el condicionamiento. El parámetro `start_image` no está expuesto como entrada en el esquema de este nodo, pero se hace referencia a él en la lógica de ejecución.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | Condicionamiento positivo modificado con datos latentes específicos del video, incluidos el latente concatenado, la máscara y los latentes de referencia opcionales | CONDITIONING |
| `negative` | Condicionamiento negativo modificado con datos latentes específicos del video, incluidos el latente concatenado, la máscara y los latentes de referencia opcionales | CONDITIONING |
| `latent` | Tensor latente vacío con las dimensiones adecuadas para la generación de video según el tamaño del lote, los canales latentes y el escalado espacial/temporal | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/es.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
