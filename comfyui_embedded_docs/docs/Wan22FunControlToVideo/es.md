El nodo Wan22FunControlToVideo prepara las representaciones de condicionamiento y latentes para la generación de video utilizando la arquitectura del modelo Wan de video. Procesa entradas de condicionamiento positivo y negativo junto con imágenes de referencia opcionales y videos de control para crear las representaciones en el espacio latente necesarias para la síntesis de video. El nodo maneja el escalado espacial y las dimensiones temporales para generar datos de condicionamiento adecuados para los modelos de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamiento positivo para guiar la generación de video | CONDITIONING | Sí | - |
| `negativo` | Entrada de condicionamiento negativo para guiar la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar imágenes al espacio latente | VAE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `duración` | Número de fotogramas en la secuencia de video (predeterminado: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | Número de secuencias de video a generar (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `imagen_ref` | Imagen de referencia opcional para proporcionar guía visual | IMAGE | No | - |
| `video_control` | Video de control opcional para guiar el proceso de generación | IMAGE | No | - |

**Nota:** El parámetro `length` se procesa en bloques de 4 fotogramas, y el nodo maneja automáticamente el escalado temporal para el espacio latente. Cuando se proporciona `ref_image`, influye en el condicionamiento a través de latentes de referencia. Cuando se proporciona `control_video`, afecta directamente la representación latente concatenada utilizada en el condicionamiento. El parámetro `start_image` no está expuesto como entrada en el esquema de este nodo, pero se referencia en la lógica de ejecución.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negativo` | Condicionamiento positivo modificado con datos latentes específicos de video, incluyendo latente concatenado, máscara y latentes de referencia opcionales | CONDITIONING |
| `latente` | Condicionamiento negativo modificado con datos latentes específicos de video, incluyendo latente concatenado, máscara y latentes de referencia opcionales | CONDITIONING |
| `latent` | Tensor latente vacío con dimensiones apropiadas para la generación de video basadas en el tamaño del lote, canales latentes y escalado espacial/temporal | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/es.md)

---
**Source fingerprint (SHA-256):** `8b24058f06aa9f779371a402c41cffc95d13ad0131d23d1438067d77755c73e2`
