> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/es.md)

# AddNoise

Este nodo agrega ruido controlado a una imagen latente utilizando parámetros de ruido específicos y valores sigma. Procesa la entrada a través del sistema de muestreo del modelo para aplicar una escala de ruido apropiada para el rango sigma dado.

## Cómo Funciona

El nodo toma una imagen latente y le aplica ruido basándose en el generador de ruido y los valores sigma proporcionados. Primero verifica si hay sigmas proporcionados; si no los hay, devuelve la imagen latente original sin cambios. Luego, el nodo utiliza el sistema de muestreo del modelo para procesar la imagen latente y aplicar ruido escalado. La escala del ruido está determinada por la diferencia entre el primer y el último valor sigma cuando se proporcionan múltiples sigmas, o por el valor sigma único cuando solo hay uno disponible. Las imágenes latentes vacías (que contienen solo ceros) no se desplazan durante el procesamiento. La salida final es una nueva representación latente con el ruido aplicado, donde cualquier valor NaN o infinito se convierte a ceros para garantizar estabilidad.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `modelo` | MODEL | Requerido | - | - | El modelo que contiene los parámetros de muestreo y las funciones de procesamiento |
| `ruido` | NOISE | Requerido | - | - | El generador de ruido que produce el patrón de ruido base |
| `sigmas` | SIGMAS | Requerido | - | - | Valores sigma que controlan la intensidad de la escala de ruido |
| `imagen_latente` | LATENT | Requerido | - | - | La representación latente de entrada a la que se le agregará ruido |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `LATENT` | LATENT | La representación latente modificada con ruido agregado |
