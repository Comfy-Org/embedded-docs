# Ruido aleatorio

El nodo RandomNoise genera patrones de ruido aleatorio basados en un valor de semilla. Crea ruido reproducible que puede utilizarse para diversas tareas de procesamiento y generación de imágenes. La misma semilla siempre producirá el mismo patrón de ruido, lo que permite obtener resultados consistentes en múltiples ejecuciones.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `noise_seed` | El valor de semilla utilizado para generar el patrón de ruido aleatorio (predeterminado: 0). La misma semilla siempre producirá la misma salida de ruido. El control posterior a la generación está habilitado, lo que permite aleatorizar, fijar, incrementar o decrementar el valor de semilla después de cada generación. | INT | Sí | 0 a 18446744073709551615 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `noise` | El patrón de ruido aleatorio generado basado en el valor de semilla proporcionado. | NOISE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/es.md)

---
**Source fingerprint (SHA-256):** `b55ff98c636c55f064ede82c6848ffa163d1fd9b0cf6195f4a35603cfbe2bc1e`
