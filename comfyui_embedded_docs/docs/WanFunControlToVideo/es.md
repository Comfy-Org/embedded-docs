> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunControlToVideo/es.md)

Este nodo se añadió para dar soporte al modelo Alibaba Wan Fun Control para generación de video, y fue agregado después de [este commit](https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82).

- **Propósito:** Preparar la información de condicionamiento necesaria para la generación de video, utilizando el modelo Wan 2.1 Fun Control.

El nodo WanFunControlToVideo es una adición a ComfyUI diseñada para dar soporte a los modelos Wan Fun Control para generación de video, orientada a utilizar el control WanFun para la creación de videos.

Este nodo sirve como punto de preparación para información de condicionamiento esencial e inicializa el punto central del espacio latente, guiando el proceso posterior de generación de video utilizando el modelo Wan 2.1 Fun. El nombre del nodo indica claramente su función: acepta diversas entradas y las convierte a un formato adecuado para controlar la generación de video dentro del marco de trabajo WanFun.

La posición del nodo en la jerarquía de nodos de ComfyUI indica que opera en las etapas iniciales del proceso de generación de video, enfocándose en manipular las señales de condicionamiento antes del muestreo o decodificación real de los fotogramas de video.

## Entradas

| Nombre del Parámetro | Obligatorio | Tipo de Dato       | Descripción                                                                                                                                                                                                 | Valor por Defecto |
|:---------------------|:------------|:-------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| positive             | Sí          | CONDITIONING       | Datos de condicionamiento positivo estándar de ComfyUI, normalmente provenientes de un nodo "CLIP Text Encode". El prompt positivo describe el contenido, tema y estilo artístico que el usuario imagina para el video generado. | N/A               |
| negative             | Sí          | CONDITIONING       | Datos de condicionamiento negativo estándar de ComfyUI, normalmente generados por un nodo "CLIP Text Encode". El prompt negativo especifica elementos, estilos o artefactos que el usuario desea evitar en el video generado. | N/A               |
| vae                  | Sí          | VAE                | Requiere un modelo VAE (Autoencoder Variacional) compatible con la familia de modelos Wan 2.1 Fun, utilizado para codificar y decodificar datos de imagen/video.                                              | N/A               |
| width                | Sí          | INT                | El ancho deseado de los fotogramas de video de salida en píxeles, con un valor por defecto de 832, valor mínimo de 16, valor máximo determinado por nodes.MAX_RESOLUTION y un incremento de 16.              | 832               |
| height               | Sí          | INT                | La altura deseada de los fotogramas de video de salida en píxeles, con un valor por defecto de 480, valor mínimo de 16, valor máximo determinado por nodes.MAX_RESOLUTION y un incremento de 16.              | 480               |
| length               | Sí          | INT                | El número total de fotogramas en el video generado, con un valor por defecto de 81, valor mínimo de 1, valor máximo determinado por nodes.MAX_RESOLUTION y un incremento de 4.                                | 81                |
| batch_size           | Sí          | INT                | El número de videos generados en un solo lote, con un valor por defecto de 1, valor mínimo de 1 y valor máximo de 4096.                                                                                     | 1                 |
| clip_vision_output   | No          | CLIP_VISION_OUTPUT | (Opcional) Características visuales extraídas por un modelo de visión CLIP, que permiten guiar el estilo y contenido visual.                                                                                | None              |
| start_image          | No          | IMAGE              | (Opcional) Una imagen inicial que influye en el comienzo del video generado.                                                                                                                                | None              |
| control_video        | No          | IMAGE              | (Opcional) Permite a los usuarios proporcionar un video de referencia de ControlNet preprocesado que guiará el movimiento y la posible estructura del video generado.                                        | None              |

## Salidas

| Nombre del Parámetro | Tipo de Dato     | Descripción                                                                                                 |
|:---------------------|:-----------------|:------------------------------------------------------------------------------------------------------------|
| positive             | CONDITIONING     | Proporciona datos de condicionamiento positivo mejorados, incluyendo start_image y control_video codificados. |
| negative             | CONDITIONING     | Proporciona datos de condicionamiento negativo que también han sido mejorados, conteniendo el mismo concat_latent_image. |
| latent               | LATENT           | Un diccionario que contiene un tensor latente vacío con la clave "samples".                                   |