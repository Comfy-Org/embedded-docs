> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/es.md)

El nodo AudioAdjustVolume modifica el volumen del audio aplicando ajustes en decibeles. Toma una entrada de audio y aplica un factor de ganancia basado en el nivel de volumen especificado, donde los valores positivos aumentan el volumen y los valores negativos lo disminuyen. El nodo devuelve el audio modificado con la misma tasa de muestreo que el original.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `audio` | AUDIO | requerido | - | - | La entrada de audio a procesar |
| `volume` | INT | requerido | 1.0 | -100 a 100 | Ajuste de volumen en decibeles (dB). 0 = sin cambios, +6 = doble, -6 = mitad, etc |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | El audio procesado con el nivel de volumen ajustado |
