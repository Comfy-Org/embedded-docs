# Programador Ideogram 4

El nodo Programador Ideogram 4 genera una secuencia de valores sigma (niveles de ruido) para el proceso de muestreo de difusión, basándose en el programa de referencia Ideogram 4. Crea un programa de ruido personalizado que se adapta a las dimensiones de la imagen y permite un ajuste fino mediante parámetros estadísticos.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `pasos` | El número de pasos de muestreo para generar el programa (predeterminado: 20) | INT | Sí | 1 a 200 |
| `ancho` | El ancho de la imagen en píxeles (predeterminado: 1024) | INT | Sí | 256 a 8192 (paso: 16) |
| `alto` | La altura de la imagen en píxeles (predeterminado: 1024) | INT | Sí | 256 a 8192 (paso: 16) |
| `mu` | El parámetro de media para la distribución logit-normal, que controla el nivel de ruido central (predeterminado: 0.0) | FLOAT | Sí | -10.0 a 10.0 (paso: 0.05) |
| `std` | El parámetro de desviación estándar para la distribución logit-normal, que controla la dispersión de los niveles de ruido (predeterminado: 1.75) | FLOAT | Sí | 0.1 a 5.0 (paso: 0.05) |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `SIGMAS` | Un tensor de valores sigma que representa el programa de ruido, con una longitud igual a `steps + 1`. Los valores descienden de ruido alto a ruido bajo, con el valor final establecido en 0.0 para una eliminación completa del ruido. | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/es.md)

---
**Source fingerprint (SHA-256):** `408ea680158500690e28e300098a5c4fd13eb1a2c96c3d95db06244151116f22`
