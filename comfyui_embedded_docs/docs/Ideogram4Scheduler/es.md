# Planificador Ideogram 4

El nodo Ideogram 4 Scheduler genera una secuencia de valores sigma (niveles de ruido) para el proceso de muestreo de difusión, basado en el programa de referencia Ideogram 4. Crea un programa de ruido personalizado que se adapta a las dimensiones de la imagen y permite un ajuste fino mediante parámetros estadísticos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `steps` | El número de pasos de muestreo para generar el programa (predeterminado: 20) | INT | Sí | 1 a 200 |
| `width` | El ancho de la imagen en píxeles (predeterminado: 1024) | INT | Sí | 256 a 8192 (paso: 16) |
| `height` | La altura de la imagen en píxeles (predeterminado: 1024) | INT | Sí | 256 a 8192 (paso: 16) |
| `mu` | El parámetro de media para la distribución logit-normal, que controla el nivel de ruido central (predeterminado: 0.0) | FLOAT | Sí | -10.0 a 10.0 (paso: 0.05) |
| `std` | El parámetro de desviación estándar para la distribución logit-normal, que controla la dispersión de los niveles de ruido (predeterminado: 1.75) | FLOAT | Sí | 0.1 a 5.0 (paso: 0.05) |

Nota: El desplazamiento central efectivo del programa está determinado por `mu` combinado con un término de resolución basado en el área de la imagen relativa a una referencia de 512×512. Por lo tanto, las áreas de imagen más grandes desplazan el programa de ruido en comparación con las más pequeñas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `SIGMAS` | Un tensor de valores sigma que representa el programa de ruido, con longitud igual a `steps + 1`. Los valores descienden de ruido alto a ruido bajo, con el valor final establecido en 0.0 para un denoizado completo. | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/es.md)

---
**Source fingerprint (SHA-256):** `af0749713ce223d2246fc24b5100f18aa68d56746480990282899c223578b8f4`
