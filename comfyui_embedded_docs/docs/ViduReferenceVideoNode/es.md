> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/es.md)

El nodo Vidu Reference Video genera videos a partir de múltiples imágenes de referencia y un texto descriptivo. Utiliza modelos de IA para crear contenido de video consistente basado en las imágenes proporcionadas y la descripción. El nodo admite varias configuraciones de video, incluyendo duración, relación de aspecto, resolución y control de movimiento.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"vidu_q1"`<br>`"vidu_q2"`<br>`"vidu_q3"`<br>`"vidu_q4"`<br>`"vidu_q5"`<br>`"vidu_q6"`<br>`"vidu_q7"`<br>`"vidu_q8"`<br>`"vidu_q9"`<br>`"vidu_q10"`<br>`"vidu_q11"`<br>`"vidu_q12"`<br>`"vidu_q13"`<br>`"vidu_q14"`<br>`"vidu_q15"`<br>`"vidu_q16"`<br>`"vidu_q17"`<br>`"vidu_q18"`<br>`"vidu_q19"`<br>`"vidu_q20"`<br>`"vidu_q21"`<br>`"vidu_q22"`<br>`"vidu_q23"`<br>`"vidu_q24"`<br>`"vidu_q25"`<br>`"vidu_q26"`<br>`"vidu_q27"`<br>`"vidu_q28"`<br>`"vidu_q29"`<br>`"vidu_q30"`<br>`"vidu_q31"`<br>`"vidu_q32"`<br>`"vidu_q33"`<br>`"vidu_q34"`<br>`"vidu_q35"`<br>`"vidu_q36"`<br>`"vidu_q37"`<br>`"vidu_q38"`<br>`"vidu_q39"`<br>`"vidu_q40"`<br>`"vidu_q41"`<br>`"vidu_q42"`<br>`"vidu_q43"`<br>`"vidu_q44"`<br>`"vidu_q45"`<br>`"vidu_q46"`<br>`"vidu_q47"`<br>`"vidu_q48"`<br>`"vidu_q49"`<br>`"vidu_q50"`<br>`"vidu_q51"`<br>`"vidu_q52"`<br>`"vidu_q53"`<br>`"vidu_q54"`<br>`"vidu_q55"`<br>`"vidu_q56"`<br>`"vidu_q57"`<br>`"vidu_q58"`<br>`"vidu_q59"`<br>`"vidu_q60"`<br>`"vidu_q61"`<br>`"vidu_q62"`<br>`"vidu_q63"`<br>`"vidu_q64"`<br>`"vidu_q65"`<br>`"vidu_q66"`<br>`"vidu_q67"`<br>`"vidu_q68"`<br>`"vidu_q69"`<br>`"vidu_q70"`<br>`"vidu_q71"`<br>`"vidu_q72"`<br>`"vidu_q73"`<br>`"vidu_q74"`<br>`"vidu_q75"`<br>`"vidu_q76"`<br>`"vidu_q77"`<br>`"vidu_q78"`<br>`"vidu_q79"`<br>`"vidu_q80"`<br>`"vidu_q81"`<br>`"vidu_q82"`<br>`"vidu_q83"`<br>`"vidu_q84"`<br>`"vidu_q85"`<br>`"vidu_q86"`<br>`"vidu_q87"`<br>`"vidu_q88"`<br>`"vidu_q89"`<br>`"vidu_q90"`<br>`"vidu_q91"`<br>`"vidu_q92"`<br>`"vidu_q93"`<br>`"vidu_q94"`<br>`"vidu_q95"`<br>`"vidu_q96"`<br>`"vidu_q97"`<br>`"vidu_q98"`<br>`"vidu_q99"`<br>`"vidu_q100"` | Nombre del modelo para generación de video (por defecto: "vidu_q1") |
| `images` | IMAGE | Sí | - | Imágenes a utilizar como referencias para generar un video con sujetos consistentes (máximo 7 imágenes) |
| `prompt` | STRING | Sí | - | Descripción textual para la generación de video |
| `duration` | INT | No | 5-5 | Duración del video de salida en segundos (por defecto: 5) |
| `seed` | INT | No | 0-2147483647 | Semilla para la generación de video (0 para aleatorio) (por defecto: 0) |
| `aspect_ratio` | COMBO | No | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` | La relación de aspecto del video de salida (por defecto: "16:9") |
| `resolution` | COMBO | No | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"1440p"`<br>`"2160p"` | Los valores admitidos pueden variar según el modelo y la duración (por defecto: "1080p") |
| `movement_amplitude` | COMBO | No | `"auto"`<br>`"low"`<br>`"medium"`<br>`"high"` | La amplitud de movimiento de los objetos en el cuadro (por defecto: "auto") |

**Restricciones y Limitaciones:**
- El campo `prompt` es obligatorio y no puede estar vacío
- Se permite un máximo de 7 imágenes como referencia
- Cada imagen debe tener una relación de aspecto entre 1:4 y 4:1
- Cada imagen debe tener dimensiones mínimas de 128x128 píxeles
- La duración está fijada en 5 segundos

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado basado en las imágenes de referencia y el texto descriptivo |