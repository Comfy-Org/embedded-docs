> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/es.md)

El nodo TrimAudioDuration permite cortar un segmento de tiempo específico de un archivo de audio. Puedes especificar cuándo iniciar el corte y la duración que debe tener el clip de audio resultante. El nodo funciona convirtiendo los valores de tiempo en posiciones de fotogramas de audio y extrayendo la porción correspondiente de la forma de onda de audio.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `audio` | AUDIO | Sí | - | La entrada de audio que se va a recortar |
| `índice_inicio` | FLOAT | Sí | -0xffffffffffffffff a 0xffffffffffffffff | Tiempo de inicio en segundos, puede ser negativo para contar desde el final (admite subsegundos). Valor predeterminado: 0.0 |
| `duración` | FLOAT | Sí | 0.0 a 0xffffffffffffffff | Duración en segundos. Valor predeterminado: 60.0 |

**Nota:** El tiempo de inicio debe ser menor que el tiempo de finalización y estar dentro de la duración del audio. Los valores de inicio negativos cuentan hacia atrás desde el final del audio. Si el tiempo de inicio es negativo, se convierte en una posición de fotograma que cuenta desde el final del audio. Los fotogramas de inicio y final se ajustan a los límites del audio.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `audio` | AUDIO | El segmento de audio recortado con el tiempo de inicio y la duración especificados |

---
**Source fingerprint (SHA-256):** `695a9fe11fa086a317f94823e066688705e9f911cd6cfc5857596ff31dd539ed`
