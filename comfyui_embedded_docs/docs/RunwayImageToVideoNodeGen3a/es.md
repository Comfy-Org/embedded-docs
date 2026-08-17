# Runway Imagen a Video (Gen3a Turbo)

El nodo Runway Image to Video (Gen3a Turbo) genera un video a partir de un único fotograma inicial utilizando el modelo Gen3a Turbo de Runway. Toma un prompt de texto y un fotograma inicial, y luego crea una secuencia de video basada en la duración y la relación de aspecto especificadas. Este nodo se conecta a la API de Runway para procesar la generación de forma remota.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Prompt de texto para la generación (predeterminado: "") | STRING | Sí | N/A |
| `start_frame` | Fotograma inicial que se utilizará para el video | IMAGE | Sí | N/A |
| `duration` | Duración del video en segundos (predeterminado: "5") | COMBO | Sí | `"5"`<br>`"10"` |
| `ratio` | Relación de aspecto del video generado (predeterminado: "768:1280") | COMBO | Sí | `"768:1280"`<br>`"1280:768"` |
| `seed` | Semilla aleatoria para la generación (predeterminado: 0) | INT | No | 0 a 4294967295 |

**Restricciones de parámetros:**

- El `start_frame` debe tener dimensiones que no superen los 7999x7999 píxeles.
- El `start_frame` debe tener una relación de aspecto entre 0.5 y 2.0.
- El `prompt` debe contener al menos un carácter (no puede estar vacío).

**Notas:**

- Este nodo está obsoleto.
- Antes de generar, Runway recomienda revisar su guía de mejores prácticas: https://help.runwayml.com/hc/en-us/articles/33927968552339-Creating-with-Act-One-on-Gen-3-Alpha-and-Turbo

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | La secuencia de video generada | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/es.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
