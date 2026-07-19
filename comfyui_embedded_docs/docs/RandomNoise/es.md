# Ruido aleatorio

El nodo RandomNoise genera patrones de ruido aleatorio basados en un valor de semilla. Crea ruido reproducible que puede utilizarse para diversas tareas de procesamiento y generación de imágenes. La misma semilla siempre producirá el mismo patrón de ruido, lo que permite obtener resultados consistentes en múltiples ejecuciones.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `semilla_ruido` | El valor de semilla utilizado para generar el patrón de ruido aleatorio (predeterminado: 0). La misma semilla siempre producirá la misma salida de ruido. | INT | Sí | 0 a 18446744073709551615 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `noise` | El patrón de ruido aleatorio generado basado en el valor de semilla proporcionado. | NOISE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/es.md)

---
**Source fingerprint (SHA-256):** `893d3eefdef78592ba3cc403ec1e4bf3a672607abe79f05db1b65078d6b9ea20`
