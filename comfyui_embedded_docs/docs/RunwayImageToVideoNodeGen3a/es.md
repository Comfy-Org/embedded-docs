# Runway Imagen a Video (Gen3a Turbo)

El nodo Runway Image to Video (Gen3a Turbo) genera un video a partir de un único fotograma inicial utilizando el modelo Gen3a Turbo de Runway. Toma un prompt de texto y un fotograma de imagen inicial, y luego crea una secuencia de video basada en la duración y la relación de aspecto especificadas. Este nodo se conecta a la API de Runway para procesar la generación de forma remota. Runway recomienda revisar su guía de mejores prácticas antes de generar: https://help.runwayml.com/hc/en-us/articles/33927968552339-Creating-with-Act-One-on-Gen-3-Alpha-and-Turbo. Este nodo está marcado como obsoleto.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Prompt de texto para la generación (por defecto: "") | STRING | Sí | N/A |
| `fotograma_inicial` | Fotograma inicial que se utilizará para el video | IMAGE | Sí | N/A |
| `duración` | Duración del video en segundos (por defecto: "5") | COMBO | Sí | `"5"`<br>`"10"` |
| `relación` | Relación de aspecto del video generado (por defecto: "768:1280") | COMBO | Sí | `"768:1280"`<br>`"1280:768"` |
| `semilla` | Semilla aleatoria para la generación (por defecto: 0) | INT | Sí | 0 a 4294967295 |

**Restricciones de parámetros:**

- El `start_frame` no debe superar los 7999x7999 píxeles de dimensiones.
- El `start_frame` debe tener una relación de aspecto entre 0.5 y 2.0.
- El `start_frame` acepta una sola imagen (máximo 1).
- El `prompt` debe contener al menos un carácter (no puede estar vacío).

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-----------------|-------------|--------------|
| `output` | La secuencia de video generada | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/es.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
