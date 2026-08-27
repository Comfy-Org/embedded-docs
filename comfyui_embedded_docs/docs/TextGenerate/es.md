# TextGenerate

El nodo TextGenerate utiliza un modelo CLIP para crear texto basado en el prompt del usuario. Opcionalmente, puede usar imágenes, video o audio como contexto adicional para guiar la generación de texto. Puedes controlar la longitud de la salida, habilitar un modo de pensamiento para los modelos compatibles y elegir si usar muestreo aleatorio con diversas configuraciones o generar texto sin muestreo.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modo_de_muestreo` | Controla si se utiliza muestreo aleatorio durante la generación de texto. Cuando se establece en "on", hay disponibles parámetros de muestreo adicionales. Cuando se establece en "off", el nodo genera texto sin muestreo aleatorio. | DYNAMIC_COMBO | Sí | `"on"`<br>`"off"` |
| `clip` | El modelo CLIP utilizado para tokenizar el prompt y generar texto. | CLIP | Sí | N/A |
| `prompt` | El prompt de texto que guía la generación. Este campo admite múltiples líneas y prompts dinámicos. El valor predeterminado es una cadena vacía. | STRING | Sí | N/A |
| `imagen` | Una imagen opcional que puede usarse junto con el prompt de texto para influir en el texto generado. | IMAGE | No | N/A |
| `video` | Fotogramas de video como un lote de imágenes. Se asume que son 24 FPS; se submuestran a 1 FPS internamente. | IMAGE | No | N/A |
| `audio` | Una entrada de audio opcional que puede usarse junto con el prompt de texto para influir en el texto generado. | AUDIO | No | N/A |
| `longitud_máxima` | El número máximo de tokens que generará el modelo. El valor predeterminado es 512. | INT | Sí | 1 a 32768 |
| `pensando` | Opera en modo de pensamiento si el modelo lo admite. El valor predeterminado es False. | BOOLEAN | No | True o False |
| `use_default_template` | Usa el prompt/plantilla del sistema integrado si el modelo tiene uno. El valor predeterminado es True. Este es un parámetro avanzado. | BOOLEAN | No | True o False |

### Parámetros de muestreo (cuando `sampling_mode` es "on")

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `temperature` | Controla la aleatoriedad de la salida. Los valores más bajos hacen que la salida sea más predecible, los valores más altos la hacen más creativa. El valor predeterminado es 0.7. | FLOAT | Sí | 0.01 a 2.0 |
| `top_k` | Limita el grupo de muestreo a los K tokens más probables siguientes. Un valor de 0 desactiva este filtro. El valor predeterminado es 64. | INT | Sí | 0 a 1000 |
| `top_p` | Utiliza muestreo de núcleo (nucleus sampling), limitando las opciones a tokens cuya probabilidad acumulativa es menor que este valor. El valor predeterminado es 0.95. | FLOAT | Sí | 0.0 a 1.0 |
| `min_p` | Establece un umbral de probabilidad mínimo para que los tokens sean considerados. El valor predeterminado es 0.05. | FLOAT | Sí | 0.0 a 1.0 |
| `repetition_penalty` | Penaliza los tokens que ya han sido generados para reducir la repetición. Un valor de 1.0 no aplica penalización. El valor predeterminado es 1.05. | FLOAT | Sí | 0.0 a 5.0 |
| `seed` | Un número utilizado para inicializar el generador de números aleatorios y obtener resultados reproducibles. El valor predeterminado es 0. | INT | Sí | 0 a 18446744073709551615 |
| `presence_penalty` | Penaliza los tokens nuevos según si han aparecido en el texto hasta ahora, animando al modelo a hablar de temas nuevos. El valor predeterminado es 0.0. | FLOAT | No | 0.0 a 5.0 |

**Nota:** Los parámetros de muestreo anteriores solo están activos y visibles en la interfaz del nodo cuando `sampling_mode` está establecido en "on". Cuando `sampling_mode` está establecido en "off", no hay parámetros de muestreo disponibles y el nodo genera texto sin muestreo aleatorio.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `texto_generado` | El texto generado por el modelo basado en el prompt de entrada y la imagen, el video o el audio opcionales. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/es.md)

---
**Source fingerprint (SHA-256):** `6274a2db7c9a963304daf6df494b2b20879155e918d73429fd2ce7f3b5b9da02`
