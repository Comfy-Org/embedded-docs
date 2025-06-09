
Este nodo está diseñado para procesar información de condicionamiento de manera por lotes, específicamente adaptado para el modelo StableZero123. Se centra en manejar eficientemente múltiples conjuntos de datos de condicionamiento simultáneamente, optimizando el flujo de trabajo para escenarios donde el procesamiento por lotes es crucial.

## Entradas

| Parámetro             | Tipo de Dato | Descripción |
|----------------------|--------------|-------------|
| `clip_vision`         | `CLIP_VISION` | Las incrustaciones de visión CLIP que proporcionan contexto visual para el proceso de condicionamiento. |
| `init_image`          | `IMAGE`      | La imagen inicial sobre la cual se va a condicionar, sirviendo como punto de partida para el proceso de generación. |
| `vae`                 | `VAE`        | El autoencoder variacional utilizado para codificar y decodificar imágenes en el proceso de condicionamiento. |
| `width`               | `INT`        | El ancho de la imagen de salida. |
| `height`              | `INT`        | La altura de la imagen de salida. |
| `batch_size`          | `INT`        | El número de conjuntos de condicionamiento que se procesarán en un solo lote. |
| `elevation`           | `FLOAT`      | El ángulo de elevación para el condicionamiento del modelo 3D, afectando la perspectiva de la imagen generada. |
| `azimuth`             | `FLOAT`      | El ángulo de acimut para el condicionamiento del modelo 3D, afectando la orientación de la imagen generada. |
| `elevation_batch_increment` | `FLOAT` | El cambio incremental en el ángulo de elevación a través del lote, permitiendo perspectivas variadas. |
| `azimuth_batch_increment` | `FLOAT` | El cambio incremental en el ángulo de acimut a través del lote, permitiendo orientaciones variadas. |

## Salidas

| Parámetro     | Tipo de Dato | Descripción |
|---------------|--------------|-------------|
| `positive`    | `CONDITIONING` | La salida de condicionamiento positiva, adaptada para promover ciertas características o aspectos en el contenido generado. |
| `negative`    | `CONDITIONING` | La salida de condicionamiento negativa, adaptada para despromover ciertas características o aspectos en el contenido generado. |
| `latent`      | `LATENT`     | La representación latente derivada del proceso de condicionamiento, lista para pasos de procesamiento o generación adicionales. |
