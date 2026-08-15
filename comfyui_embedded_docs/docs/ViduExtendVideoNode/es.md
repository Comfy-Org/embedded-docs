# Extensión de video Vidu

El nodo ViduExtendVideoNode genera fotogramas adicionales para ampliar la duración de un video existente. Utiliza un modelo de IA específico para crear una continuación fluida basada en el video de origen y una indicación de texto opcional.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | Modelo a utilizar para la extensión de video. Al seleccionar un modelo se muestran sus ajustes específicos de duración y resolución. | DYNAMIC_COMBO | Sí | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `video` | El video de origen que se va a extender. | VIDEO | Sí | - |
| `prompt` | Una indicación de texto opcional para el video extendido (máximo 2000 caracteres, por defecto: vacío). | STRING | No | - |
| `semilla` | Un valor de semilla para controlar la aleatoriedad de la generación (por defecto: 1). | INT | No | 0 a 2147483647 |
| `fotograma_final` | Una imagen opcional para usar como fotograma final de destino para la extensión. | IMAGE | No | - |

### Entradas de viduq2-pro y viduq2-turbo

Estas configuraciones son comunes a ambos modelos.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `duración` | Duración del video extendido en segundos (por defecto: 4). Esta configuración aparece después de seleccionar un modelo. | INT | Sí | 1 a 7 |
| `resolución` | Resolución del video de salida. Esta configuración aparece después de seleccionar un modelo. | COMBO | Sí | `"720p"`<br>`"1080p"` |

**Nota:** El `video` de origen debe tener una duración de entre 4 y 55 segundos. Si se proporciona `end_frame`, su relación de aspecto debe estar entre 1:4 y 4:1, y tanto su ancho como su alto deben ser de al menos 128 píxeles.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El nuevo archivo de video generado que contiene el metraje extendido. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `bfa79dd1aee8a3e56d95fe7a899454b5c5f93679e098f59fc3bf58d93d290819`
