# TextGenerate

El nodo TextGenerate utiliza un modelo CLIP para crear texto basado en la indicación del usuario. Opcionalmente, puede usar imágenes, video o audio como contexto adicional para guiar la generación de texto. Puedes controlar la longitud de la salida, activar un modo de pensamiento para modelos compatibles y elegir si usar muestreo aleatorio con varias configuraciones o generar texto sin muestreo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para tokenizar la indicación y generar texto. | CLIP | Sí | N/A |
| `prompt` | La indicación de texto que guía la generación. Este campo admite múltiples líneas e indicaciones dinámicas. El valor predeterminado es una cadena vacía. | STRING | Sí | N/A |
| `imagen` | Una imagen opcional que se puede usar junto con la indicación de texto para influir en el texto generado. | IMAGE | No | N/A |
| `video` | Fotogramas de video como un lote de imágenes. Se asume que son 24 FPS; se submuestrea internamente a 1 FPS. | IMAGE | No | N/A |
| `audio` | Una entrada de audio opcional que se puede usar junto con la indicación de texto para influir en el texto generado. | AUDIO | No | N/A |
| `longitud_máxima` | El número máximo de tokens que generará el modelo. El valor predeterminado es 256. | INT | Sí | 1 a 2048 |
| `modo_de_muestreo` | Controla si se utiliza muestreo aleatorio durante la generación de texto. Cuando se establece en "on", los parámetros adicionales para controlar el muestreo están disponibles. El valor predeterminado es "on". | COMBO | Sí | `"on"`<br>`"off"` |
| `pensando` | Opera en modo de pensamiento si el modelo lo admite. El valor predeterminado es Falso. | BOOLEAN | No | Verdadero o Falso |
| `use_default_template` | Usa la plantilla/indicación del sistema incorporada si el modelo tiene una. El valor predeterminado es Verdadero. Este es un parámetro avanzado. | BOOLEAN | No | Verdadero o Falso |
| `temperature` | Controla la aleatoriedad de la salida. Los valores más bajos hacen que la salida sea más predecible, los valores más altos la hacen más creativa. Este parámetro solo está disponible cuando `modo_de_muestreo` está en "on". El valor predeterminado es 0.7. | FLOAT | No | 0.01 a 2.0 |
| `top_k` | Limita el grupo de muestreo a los K tokens siguientes más probables. Un valor de 0 desactiva este filtro. Este parámetro solo está disponible cuando `modo_de_muestreo` está en "on". El valor predeterminado es 64. | INT | No | 0 a 1000 |
| `top_p` | Utiliza muestreo de núcleo, limitando las opciones a tokens cuya probabilidad acumulada sea menor que este valor. Este parámetro solo está disponible cuando `modo_de_muestreo` está en "on". El valor predeterminado es 0.95. | FLOAT | No | 0.0 a 1.0 |
| `min_p` | Establece un umbral de probabilidad mínimo para que los tokens sean considerados. Este parámetro solo está disponible cuando `modo_de_muestreo` está en "on". El valor predeterminado es 0.05. | FLOAT | No | 0.0 a 1.0 |
| `repetition_penalty` | Penaliza los tokens que ya se han generado para reducir la repetición. Un valor de 1.0 no aplica penalización. Este parámetro solo está disponible cuando `modo_de_muestreo` está en "on". El valor predeterminado es 1.05. | FLOAT | No | 0.0 a 5.0 |
| `presence_penalty` | Penaliza los tokens nuevos según si han aparecido en el texto hasta ahora, lo que anima al modelo a hablar sobre temas nuevos. Este parámetro solo está disponible cuando `modo_de_muestreo` está en "on". El valor predeterminado es 0.0. | FLOAT | No | 0.0 a 5.0 |
| `seed` | Un número utilizado para inicializar el generador de números aleatorios para obtener resultados reproducibles cuando el muestreo está en "on". El valor predeterminado es 0. | INT | No | 0 a 18446744073709551615 |

**Nota:** Los parámetros `temperature`, `top_k`, `top_p`, `min_p`, `repetition_penalty`, `presence_penalty` y `seed` solo están activos y visibles en la interfaz del nodo cuando `sampling_mode` está configurado en "on".

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `generated_text` | El texto generado por el modelo basado en la indicación de entrada y la imagen, video o audio opcionales. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/es.md)

---
**Source fingerprint (SHA-256):** `dc6868bd7ebb63c485a4346113834f845416d7359759b2d428525398bdedf343`
