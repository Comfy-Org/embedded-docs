# HappyHorse Texto a Video

Genera un video basado en un prompt de texto utilizando el modelo HappyHorse. Este nodo envía tu prompt y configuración a la API de HappyHorse, espera a que se genere el video y luego descarga el resultado.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo HappyHorse utilizado para la generación, junto con sus subparámetros. Seleccionar un modelo determina qué subparámetros están disponibles (consulta las secciones de modelos a continuación). | DICT | Sí | "happyhorse-1.1-t2v"<br>"happyhorse-1.0-t2v" |
| `seed` | Semilla a utilizar para la generación. Usar la misma semilla con las mismas entradas producirá el mismo resultado. (predeterminado: 0). | INT | Sí | 0 a 2147483647 |
| `watermark` | Si se debe añadir una marca de agua generada por IA al resultado. (predeterminado: False). | BOOLEAN | No | True / False |

### Entradas de happyhorse-1.1-t2v

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model.prompt` | Prompt que describe los elementos y las características visuales. Admite inglés y chino. (predeterminado: ""). | STRING | Sí | - |
| `model.resolution` | La resolución del video de salida. | STRING | Sí | "720P"<br>"1080P" |
| `model.ratio` | La relación de aspecto del video de salida. | STRING | Sí | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21"<br>"5:4"<br>"4:5" |
| `model.duration` | La duración del video en segundos. (predeterminado: 5, mínimo: 3, máximo: 15, paso: 1). | INT | Sí | 3 a 15 |

### Entradas de happyhorse-1.0-t2v

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model.prompt` | Prompt que describe los elementos y las características visuales. Admite inglés y chino. (predeterminado: ""). | STRING | Sí | - |
| `model.resolution` | La resolución del video de salida. | STRING | Sí | "720P"<br>"1080P" |
| `model.ratio` | La relación de aspecto del video de salida. | STRING | Sí | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `model.duration` | La duración del video en segundos. (predeterminado: 5, mínimo: 3, máximo: 15, paso: 1). | INT | Sí | 3 a 15 |

Nota: El prompt no debe estar vacío; se genera un error si no se proporciona ningún prompt. Ambos modelos admiten duraciones de video de 3 a 15 segundos. El modelo `happyhorse-1.1-t2v` ofrece relaciones de aspecto adicionales (`21:9`, `9:21`, `5:4`, `4:5`) que no están disponibles con `happyhorse-1.0-t2v`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `VIDEO` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/es.md)

---
**Source fingerprint (SHA-256):** `b60cfc3ce4935d7eb36bb28f9bd268446c4df5b437e06278b7e6d91d349d0238`
