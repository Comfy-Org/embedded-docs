# AñadirRuido

Este nodo añade ruido controlado a una imagen latente utilizando un generador de ruido específico y valores sigma. Procesa la entrada a través del sistema de muestreo del modelo para aplicar una escala de ruido apropiada para el rango sigma dado, devolviendo una nueva representación latente con el ruido aplicado.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo que contiene los parámetros de muestreo y las funciones de procesamiento | MODEL | Sí | - |
| `noise` | El generador de ruido que produce el patrón de ruido base | NOISE | Sí | - |
| `sigmas` | Valores sigma que controlan la intensidad de la escala de ruido. Si está vacío, el nodo devuelve la imagen latente original sin cambios. Cuando se proporcionan varios sigmas, la escala de ruido se calcula como la diferencia absoluta entre el primer y el último valor sigma. Cuando solo se proporciona un sigma, ese valor se usa directamente como escala. | SIGMAS | Sí | - |
| `latent_image` | La representación latente de entrada a la que se añadirá ruido. Las imágenes latentes vacías (que contienen solo ceros) no se desplazan durante el procesamiento. | LATENT | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `LATENT` | La representación latente modificada con ruido añadido. Cualquier valor NaN o infinito en la salida se convierte a ceros para garantizar la estabilidad. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/es.md)

---
**Source fingerprint (SHA-256):** `6b11db10af9a2b8ea24dbf3b40c08d7e37de39df746e3966e5bfc94b84dee068`
