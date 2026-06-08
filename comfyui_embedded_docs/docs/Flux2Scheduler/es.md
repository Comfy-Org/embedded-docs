El nodo Flux2Scheduler genera una secuencia de niveles de ruido (sigmas) para el proceso de eliminación de ruido, diseñado específicamente para el modelo Flux. Calcula un cronograma basado en la cantidad de pasos de eliminación de ruido y las dimensiones de la imagen objetivo, lo que influye en la progresión de la eliminación de ruido durante la generación de imágenes.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `pasos` | El número de pasos de eliminación de ruido a realizar. Un valor más alto generalmente produce resultados más detallados, pero requiere más tiempo de procesamiento (predeterminado: 20). | INT | Sí | 1 a 4096 |
| `ancho` | El ancho de la imagen a generar, en píxeles. Este valor influye en el cálculo del cronograma de ruido (predeterminado: 1024). | INT | Sí | 16 a 16384 |
| `alto` | La altura de la imagen a generar, en píxeles. Este valor influye en el cálculo del cronograma de ruido (predeterminado: 1024). | INT | Sí | 16 a 16384 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sigmas` | Una secuencia de valores de nivel de ruido (sigmas) que definen el cronograma de eliminación de ruido para el muestreador. | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/es.md)

---
**Source fingerprint (SHA-256):** `dbe44a6eb454dd61ab22df5770ad5ac559e03b20fd36d17d33730cdb835f7ede`
