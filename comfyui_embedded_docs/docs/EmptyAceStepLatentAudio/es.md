# EmptyAceStepLatentAudio

El nodo **Empty Ace Step 1.0 Latent Audio** crea muestras de audio latente vacías con una duración especificada. Genera un lote de latentes de audio silenciosos rellenos con ceros, donde la longitud se calcula a partir de los segundos de entrada y los parámetros de procesamiento de audio. Este nodo es útil para inicializar flujos de trabajo de procesamiento de audio que requieren representaciones latentes.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `segundos` | La duración del audio en segundos (predeterminado: 120.0, paso: 0.1) | FLOAT | Sí | 1.0 - 1000.0 |
| `tamaño_del_lote` | El número de imágenes latentes en el lote (predeterminado: 1) | INT | Sí | 1 - 4096 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | Devuelve muestras de audio latente vacías con ceros. La salida contiene un tensor `samples` y un campo `type` establecido en "audio". | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/es.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
