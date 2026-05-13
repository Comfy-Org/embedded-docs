> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/es.md)

Este nodo añade ruido controlado a una imagen latente utilizando un generador de ruido específico y valores sigma. Procesa la entrada a través del sistema de muestreo del modelo para aplicar un escalado de ruido adecuado al rango sigma dado, devolviendo una nueva representación latente con el ruido aplicado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo que contiene los parámetros de muestreo y las funciones de procesamiento |
| `noise` | NOISE | Sí | - | El generador de ruido que produce el patrón base de ruido |
| `sigmas` | SIGMAS | Sí | - | Valores sigma que controlan la intensidad del escalado de ruido. Si está vacío, el nodo devuelve la imagen latente original sin cambios. Cuando se proporcionan múltiples sigma, la escala de ruido se calcula como la diferencia absoluta entre el primer y el último valor sigma. Cuando solo se proporciona un sigma, ese valor se utiliza directamente como escala. |
| `latent_image` | LATENT | Sí | - | La representación latente de entrada a la que se le añadirá ruido. Las imágenes latentes vacías (que contienen solo ceros) no se desplazan durante el procesamiento. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `LATENT` | LATENT | La representación latente modificada con el ruido añadido. Cualquier valor NaN o infinito en la salida se convierte a ceros para mantener la estabilidad. |

---
**Source fingerprint (SHA-256):** `8f387f95aeec2780d27bee5b954ad2c6cd6daa9242a1ea15697455b157bc80d5`
