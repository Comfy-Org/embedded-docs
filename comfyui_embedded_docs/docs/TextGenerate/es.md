> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerate/es.md)

El nodo TextGenerate utiliza un modelo CLIP para crear texto basado en un *prompt* del usuario. Opcionalmente, puede usar una imagen como referencia visual para guiar la generación de texto. Puedes controlar la longitud de la salida y elegir si usar muestreo aleatorio con varios ajustes o generar texto sin muestreo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sí | N/A | El modelo CLIP utilizado para tokenizar el *prompt* y generar texto. |
| `prompt` | STRING | Sí | N/A | El *prompt* de texto que guía la generación. Este campo admite múltiples líneas y *prompts* dinámicos. El valor por defecto es una cadena vacía. |
| `image` | IMAGE | No | N/A | Una imagen opcional que puede usarse junto con el *prompt* de texto para influir en el texto generado. |
| `max_length` | INT | Sí | 1 a 2048 | El número máximo de *tokens* que generará el modelo. El valor por defecto es 256. |
| `sampling_mode` | COMBO | Sí | `"on"`<br>`"off"` | Controla si se utiliza muestreo aleatorio durante la generación de texto. Cuando se establece en "on", se habilitan parámetros adicionales para controlar el muestreo. El valor por defecto es "on". |
| `temperature` | FLOAT | No | 0.01 a 2.0 | Controla la aleatoriedad de la salida. Valores más bajos hacen la salida más predecible, valores más altos la hacen más creativa. Este parámetro solo está disponible cuando `sampling_mode` es "on". El valor por defecto es 0.7. |
| `top_k` | INT | No | 0 a 1000 | Limita el grupo de muestreo a los K *tokens* siguientes más probables. Un valor de 0 desactiva este filtro. Este parámetro solo está disponible cuando `sampling_mode` es "on". El valor por defecto es 64. |
| `top_p` | FLOAT | No | 0.0 a 1.0 | Utiliza muestreo de núcleo (*nucleus sampling*), limitando las opciones a *tokens* cuya probabilidad acumulada es menor que este valor. Este parámetro solo está disponible cuando `sampling_mode` es "on". El valor por defecto es 0.95. |
| `min_p` | FLOAT | No | 0.0 a 1.0 | Establece un umbral de probabilidad mínimo para que los *tokens* sean considerados. Este parámetro solo está disponible cuando `sampling_mode` es "on". El valor por defecto es 0.05. |
| `repetition_penalty` | FLOAT | No | 0.0 a 5.0 | Penaliza los *tokens* que ya se han generado para reducir la repetición. Un valor de 1.0 no aplica penalización. Este parámetro solo está disponible cuando `sampling_mode` es "on". El valor por defecto es 1.05. |
| `seed` | INT | No | 0 a 18446744073709551615 | Un número utilizado para inicializar el generador de números aleatorios para obtener resultados reproducibles cuando el muestreo está en "on". El valor por defecto es 0. |

**Nota:** Los parámetros `temperature`, `top_k`, `top_p`, `min_p`, `repetition_penalty` y `seed` solo están activos y visibles en la interfaz del nodo cuando el `sampling_mode` está establecido en "on".

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `generated_text` | STRING | El texto generado por el modelo basado en el *prompt* de entrada y la imagen opcional. |
