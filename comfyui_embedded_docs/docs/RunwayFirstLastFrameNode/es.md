> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/es.md)

El nodo Runway Primer-Último Fotograma a Video genera videos subiendo fotogramas clave inicial y final junto con un mensaje de texto. Crea transiciones suaves entre los fotogramas de inicio y fin proporcionados utilizando el modelo Gen-3 de Runway. Esto es particularmente útil para transiciones complejas donde el fotograma final difiere significativamente del fotograma inicial.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Mensaje de texto para la generación (predeterminado: cadena vacía) |
| `start_frame` | IMAGE | Sí | N/A | Fotograma inicial que se utilizará para el video |
| `end_frame` | IMAGE | Sí | N/A | Fotograma final que se utilizará para el video. Solo compatible con gen3a_turbo. |
| `duration` | COMBO | Sí | `"5"`<br>`"10"` | Duración del video en segundos (predeterminado: "5") |
| `ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Relación de aspecto para el video generado (predeterminado: "16:9") |
| `seed` | INT | No | 0 a 4294967295 | Semilla aleatoria para la generación. Establecer en 0 para semilla aleatoria (predeterminado: 0). |

**Restricciones de Parámetros:**

- El `prompt` debe contener al menos 1 carácter
- Tanto `start_frame` como `end_frame` deben tener dimensiones máximas de 7999x7999 píxeles
- Tanto `start_frame` como `end_frame` deben tener relaciones de aspecto entre 0.5 y 2.0
- El parámetro `end_frame` solo es compatible cuando se utiliza el modelo gen3a_turbo

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El video generado que realiza la transición entre los fotogramas inicial y final |

---
**Source fingerprint (SHA-256):** `57b72c1143b7053272107403279e1f84919cbfe71c57ca4f4e21b4324f7a5346`
