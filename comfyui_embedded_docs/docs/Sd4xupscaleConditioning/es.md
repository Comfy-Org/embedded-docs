Este nodo se especializa en mejorar la resolución de imágenes mediante un proceso de ampliación 4x, incorporando elementos de condicionamiento para refinar el resultado. Aprovecha técnicas de difusión para ampliar las imágenes, permitiendo ajustar la relación de escala y la aumentación de ruido para afinar el proceso de mejora.

## Entradas

| Parámetro | Descripción | Tipo Comfy |
| --- | --- | --- |
| `images` | Las imágenes de entrada que se ampliarán. Este parámetro es crucial, ya que influye directamente en la calidad y resolución de las imágenes de salida. | `IMAGE` |
| `positive` | Elementos de condicionamiento positivo que guían el proceso de ampliación hacia atributos o características deseadas en las imágenes de salida. | `CONDITIONING` |
| `negative` | Elementos de condicionamiento negativo que el proceso de ampliación debe evitar, ayudando a alejar la salida de atributos o características no deseadas. | `CONDITIONING` |
| `scale_ratio` | Determina el factor por el cual se incrementa la resolución de la imagen. Una relación de escala más alta produce una imagen de salida más grande, permitiendo mayor detalle y claridad. | `FLOAT` |
| `noise_augmentation` | Controla el nivel de aumentación de ruido aplicado durante el proceso de ampliación. Esto puede utilizarse para introducir variabilidad y mejorar la robustez de las imágenes de salida. | `FLOAT` |

## Salidas

| Parámetro | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positive` | Los elementos de condicionamiento positivo refinados resultantes del proceso de ampliación. | `CONDITIONING` |
| `negative` | Los elementos de condicionamiento negativo refinados resultantes del proceso de ampliación. | `CONDITIONING` |
| `latent` | Una representación latente generada durante el proceso de ampliación, que puede utilizarse en procesamiento adicional o entrenamiento de modelos. | `LATENT` |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Sd4xupscaleConditioning/es.md)
