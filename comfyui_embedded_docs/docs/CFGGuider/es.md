> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/es.md)

El nodo CFGGuider crea un sistema de guía para controlar el proceso de muestreo en la generación de imágenes. Toma un modelo junto con entradas de condicionamiento positivo y negativo, y luego aplica una escala de guía libre de clasificador para dirigir la generación hacia el contenido deseado mientras evita elementos no deseados. Este nodo genera un objeto guía que puede ser utilizado por los nodos de muestreo para controlar la dirección de la generación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `modelo` | MODEL | Requerido | - | - | El modelo que se utilizará para la guía |
| `positivo` | CONDITIONING | Requerido | - | - | El condicionamiento positivo que guía la generación hacia el contenido deseado |
| `negativo` | CONDITIONING | Requerido | - | - | El condicionamiento negativo que aleja la generación del contenido no deseado |
| `cfg` | FLOAT | Requerido | 8.0 | 0.0 - 100.0 | La escala de guía libre de clasificador que controla qué tan fuerte influye el condicionamiento en la generación |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | Un objeto guía que puede pasarse a los nodos de muestreo para controlar el proceso de generación |
