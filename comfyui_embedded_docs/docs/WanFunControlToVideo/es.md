Este nodo se ha añadido para soportar el modelo Wan Fun Control en video, introducido después de [este commit](https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82).

- **Propósito:** Preparar la información condicional necesaria para generar videos utilizando el modelo Wan 2.1 Fun Control.

El nodo WanFunControlToVideo es una adición de ComfyUI para soportar el modelo Wan Fun Control en video, diseñado para aprovechar el control WanFun en la generación de videos.

Este nodo actúa como el punto central para preparar la información condicional necesaria e inicializar el espacio latente, guiando el proceso de generación de video utilizando el modelo Wan 2.1 Fun. El nombre del nodo indica claramente su función: acepta diversas entradas y las convierte en un formato adecuado para controlar la generación de video dentro del marco WanFun.

La posición del nodo en la jerarquía de nodos de ComfyUI indica que opera en las primeras etapas del pipeline de generación de video, enfocándose en manipular las señales condicionales antes de la muestreo o decodificación real de los fotogramas de video.

## Entradas

| Nombre del parámetro | Parámetro requerido | Tipo de dato       | Descripción                                                                                                                                                                                                                                         | Valor por defecto |
|:---------------------|:--------------------|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| positive             | Sí                  | CONDITIONING       | Datos condicionales estándar de ComfyUI, generalmente provenientes del nodo de "codificación de texto CLIP". Las indicaciones positivas describen el contenido, tema y estilo artístico del video que el usuario imagina.                           | N/A               |
| negative             | Sí                  | CONDITIONING       | Datos condicionales negativos estándar de ComfyUI, generalmente generados por el nodo de "codificación de texto CLIP". Las indicaciones negativas especifican los elementos, estilos o artefactos que el usuario desea evitar en el video generado. | N/A               |
| vae                  | Sí                  | VAE                | Se requiere un modelo VAE (autoencoder variacional) compatible con la serie de modelos Wan 2.1 Fun, para codificar y decodificar datos de imagen/video.                                                                                             | N/A               |
| width                | Sí                  | INT                | Ancho esperado de los fotogramas de video de salida (en píxeles), valor por defecto 832, valor mínimo 16, valor máximo determinado por nodes.MAX_RESOLUTION, paso de 16.                                                                            | 832               |
| height               | Sí                  | INT                | Altura esperada de los fotogramas de video de salida (en píxeles), valor por defecto 480, valor mínimo 16, valor máximo determinado por nodes.MAX_RESOLUTION, paso de 16.                                                                           | 480               |
| length               | Sí                  | INT                | Número total de fotogramas en el video generado, valor por defecto 81, valor mínimo 1, valor máximo determinado por nodes.MAX_RESOLUTION, paso de 4.                                                                                                | 81                |
| batch_size           | Sí                  | INT                | Número de videos generados en un solo lote, valor por defecto 1, valor mínimo 1, valor máximo 4096.                                                                                                                                                 | 1                 |
| clip_vision_output   | No                  | CLIP_VISION_OUTPUT | (Opcional) Características visuales extraídas por el modelo visual CLIP, permitiendo la guía de estilo y contenido visual.                                                                                                                          | None              |
| start_image          | No                  | IMAGE              | (Opcional) Imagen inicial que influye en el comienzo del video generado.                                                                                                                                                                            | None              |
| control_video        | No                  | IMAGE              | (Opcional) Permite al usuario proporcionar un video de referencia preprocesado por ControlNet, que guiará el movimiento y la estructura latente del video generado.                                                                                 | None              |

## Salidas

| Nombre del parámetro | Tipo de dato | Descripción                                                                                                                  |
|:---------------------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------|
| positive             | CONDITIONING | Proporciona datos condicionales positivos mejorados, incluyendo la imagen latente codificada de start_image y control_video. |
| negative             | CONDITIONING | Proporciona datos condicionales negativos, que también han sido mejorados, conteniendo la misma imagen latente concatenada.  |
| latent               | LATENT       | Un diccionario que contiene un tensor latente vacío, con la clave "samples".                                                 |
