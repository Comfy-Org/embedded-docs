> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/es.md)

El nodo SD_4XUpscale_Conditioning prepara datos de condicionamiento para el escalado de imágenes utilizando modelos de difusión. Toma imágenes de entrada y datos de condicionamiento, luego aplica escalado y aumento de ruido para crear un condicionamiento modificado que guía el proceso de escalado. El nodo genera tanto condicionamiento positivo como negativo junto con representaciones latentes para las dimensiones escaladas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imágenes` | IMAGE | Sí | - | Imágenes de entrada que se van a escalar |
| `positivo` | CONDITIONING | Sí | - | Datos de condicionamiento positivo que guían la generación hacia el contenido deseado |
| `negativo` | CONDITIONING | Sí | - | Datos de condicionamiento negativo que alejan la generación del contenido no deseado |
| `relación_escala` | FLOAT | No | 0.0 - 10.0 | Factor de escalado aplicado a las imágenes de entrada (valor por defecto: 4.0) |
| `aumento_ruido` | FLOAT | No | 0.0 - 1.0 | Cantidad de ruido a añadir durante el proceso de escalado (valor por defecto: 0.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `negativo` | CONDITIONING | Condicionamiento positivo modificado con información de escalado aplicada |
| `latente` | CONDITIONING | Condicionamiento negativo modificado con información de escalado aplicada |
| `latent` | LATENT | Representación latente vacía que coincide con las dimensiones escaladas |