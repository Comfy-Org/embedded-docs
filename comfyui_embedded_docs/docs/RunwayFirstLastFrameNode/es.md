# Runway Primer-Fotograma-Último a Video

El nodo Runway First-Last-Frame to Video genera videos cargando el primer y último fotogramas clave junto con un prompt de texto. Crea transiciones suaves entre los fotogramas inicial y final proporcionados utilizando el modelo Gen-3 de Runway. Esto es particularmente útil para transiciones complejas donde el fotograma final difiere significativamente del inicial.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `prompt` | Prompt de texto para la generación (por defecto: cadena vacía) | STRING | Sí | N/A |
| `start_frame` | Fotograma inicial que se usará para el video | IMAGE | Sí | N/A |
| `end_frame` | Fotograma final que se usará para el video. Solo compatible con gen3a_turbo. | IMAGE | Sí | N/A |
| `duration` | Duración del video en segundos (por defecto: "5") | COMBO | Sí | `"5"`<br>`"10"` |
| `ratio` | Relación de aspecto para el video generado (por defecto: "768:1280") | COMBO | Sí | `"768:1280"`<br>`"1280:768"` |
| `seed` | Semilla aleatoria para la generación. Establece 0 para semilla aleatoria (por defecto: 0). | INT | No | 0 a 4294967295 |

**Restricciones de parámetros:**

- El `prompt` debe contener al menos 1 carácter
- Tanto `start_frame` como `end_frame` deben tener dimensiones máximas de 7999x7999 píxeles
- Tanto `start_frame` como `end_frame` deben tener relaciones de aspecto entre 0.5 y 2.0
- El parámetro `end_frame` solo es compatible cuando se utiliza el modelo gen3a_turbo

**Nota:** Este nodo está marcado como obsoleto. Revisa las mejores prácticas de Runway para crear con fotogramas clave en Gen-3 antes de usarlo: https://help.runwayml.com/hc/en-us/articles/34170748696595-Creating-with-Keyframes-on-Gen-3

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `output` | El video generado con la transición entre los fotogramas inicial y final | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/es.md)

---
**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`
