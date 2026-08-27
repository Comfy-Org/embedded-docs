# FishAudioTextToSpeech

Este nodo convierte texto escrito en audio hablado utilizando modelos de conversión de texto a voz de Fish Audio. Admite indicaciones de emoción integradas en el texto ([happy], [whispering] en s2.1-pro; (happy) en s1) y diálogo multi-hablante mediante etiquetas @Voice1/@Voice2 cuando hay varias voces conectadas. Hay dos modelos disponibles: s2.1-pro, que admite hasta cinco voces y diálogo multi-hablante, y s1, que usa una única voz opcional.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `text` | El texto a convertir en voz. Con dos o más voces conectadas, marque los cambios de hablante con @Voice1, @Voice2, etc. No debe estar vacío. (por defecto: vacío) | STRING | Sí | Cualquier texto no vacío |
| `model` | Modelo a utilizar para la conversión de texto a voz. | DYNAMIC_COMBO | Sí | "s2.1-pro"<br>"s1" |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. (por defecto: 42) | INT | Sí | 0 a 2147483647 |

### Entradas de s2.1-pro

Estas entradas aparecen cuando se selecciona el modelo s2.1-pro.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `voices` | Ranura ampliable: conecte de 1 a 5 elementos de voz (`voice_1`, `voice_2`, ...). Voces para la síntesis. No conecte ninguna para usar la voz predeterminada. Con dos o más voces, marque los cambios de hablante en el texto con @Voice1, @Voice2, etc. | FISHAUDIO_VOICE | No | 0 a 5 voces |
| `temperature` | Expresividad. Los valores más altos son más variados; los más bajos, más consistentes. (por defecto: 0.7) | FLOAT | Sí | 0.0 a 1.0 |
| `top_p` | Diversidad mediante muestreo de núcleo. (por defecto: 0.7) | FLOAT | Sí | 0.01 a 1.0 |
| `speed` | Velocidad del habla. 1.0 es normal, <1.0 más lento, >1.0 más rápido. (por defecto: 1.0) | FLOAT | Sí | 0.5 a 2.0 |
| `volume` | Ajuste de volumen en decibelios. 0 significa sin cambios. (por defecto: 0.0) | FLOAT | Sí | -10.0 a 10.0 |
| `normalize` | Normaliza números y texto en inglés y chino, mejorando la estabilidad de números y fechas. (por defecto: true) | BOOLEAN | Sí | true / false |

### Entradas de s1

Estas entradas aparecen cuando se selecciona el modelo s1.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `voice` | Voz para la síntesis. Déjela sin conectar para usar la voz predeterminada. | FISHAUDIO_VOICE | No | Una sola voz opcional |
| `temperature` | Expresividad. Los valores más altos son más variados; los más bajos, más consistentes. (por defecto: 0.7) | FLOAT | Sí | 0.0 a 1.0 |
| `top_p` | Diversidad mediante muestreo de núcleo. (por defecto: 0.7) | FLOAT | Sí | 0.01 a 1.0 |
| `speed` | Velocidad del habla. 1.0 es normal, <1.0 más lento, >1.0 más rápido. (por defecto: 1.0) | FLOAT | Sí | 0.5 a 2.0 |
| `volume` | Ajuste de volumen en decibelios. 0 significa sin cambios. (por defecto: 0.0) | FLOAT | Sí | -10.0 a 10.0 |
| `normalize` | Normaliza números y texto en inglés y chino, mejorando la estabilidad de números y fechas. (por defecto: true) | BOOLEAN | Sí | true / false |

**Nota:** La entrada `text` no debe estar vacía. Las etiquetas de hablante (@Voice1, @Voice2, etc.) no distinguen entre mayúsculas y minúsculas y deben hacer referencia a una voz conectada; etiquetar una voz que no está conectada genera un error. Cuando hay dos o más voces conectadas, el texto debe hacer referencia al menos una vez a cada voz conectada; de lo contrario, el nodo informa de las etiquetas faltantes. En s2.1-pro, conectar 0 voces usa la voz predeterminada; con 1 voz se usa solo esa voz; y con 2 o más voces se habilita el diálogo multi-hablante. En s1, se usa una única voz opcional; si se deja sin conectar, se usa la voz predeterminada. Las indicaciones de emoción pueden colocarse en el texto: [happy] y [whispering] en s2.1-pro, y (happy) en s1.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `audio` | El habla generada como archivo de audio. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioTextToSpeech/es.md)

---
**Source fingerprint (SHA-256):** `6cc005ae76fc7b60d9399b1b0a3c5de40a6eff47cd6f0f0b73b4212c0270ae29`
