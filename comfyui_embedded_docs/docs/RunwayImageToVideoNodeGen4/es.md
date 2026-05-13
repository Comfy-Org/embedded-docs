> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/es.md)

El nodo Runway Image to Video (Gen4 Turbo) genera un video a partir de un único fotograma inicial utilizando el modelo Gen4 Turbo de Runway. Toma un mensaje de texto y una imagen de fotograma inicial, luego crea una secuencia de video basada en la duración y la configuración de relación de aspecto proporcionadas. El nodo se encarga de cargar el fotograma inicial a la API de Runway y devuelve el video generado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | - | Mensaje de texto para la generación (predeterminado: cadena vacía) |
| `frame_inicial` | IMAGE | Sí | - | Fotograma inicial que se utilizará para el video |
| `duración` | COMBO | Sí | `"5"`<br>`"10"` | Duración del video en segundos (predeterminado: "5") |
| `proporción` | COMBO | Sí | `"1024:1024"`<br>`"1280:720"`<br>`"720:1280"`<br>`"1920:1080"`<br>`"1080:1920"`<br>`"2048:1080"`<br>`"1080:2048"` | Relación de aspecto para el video generado (predeterminado: "1024:1024") |
| `semilla` | INT | No | 0 a 4294967295 | Semilla aleatoria para la generación (predeterminado: 0) |

**Restricciones de parámetros:**

- La imagen `start_frame` debe tener dimensiones que no superen los 7999x7999 píxeles
- La imagen `start_frame` debe tener una relación de aspecto entre 0.5 y 2.0
- El `prompt` debe contener al menos un carácter

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `output` | VIDEO | El video generado basado en el fotograma de entrada y el mensaje |

---
**Source fingerprint (SHA-256):** `ebb5f1cd5e6bf6e0fcfb4910c774c087980daf9a1987900ad966120608b924e7`
