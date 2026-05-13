> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/es.md)

El nodo ByteDance Text to Video genera videos utilizando modelos de ByteDance a través de una API basada en descripciones de texto. Recibe como entrada una descripción textual y diversas configuraciones de video, y luego crea un video que coincide con las especificaciones proporcionadas. El nodo gestiona la comunicación con la API y devuelve el video generado como salida.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `modelo` | STRING | Sí | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-t2v-250428"`<br>`"seedance-1-0-pro-fast-251015"` | El modelo de ByteDance a utilizar para la generación (valor predeterminado: `"seedance-1-0-pro-fast-251015"`). |
| `prompt` | STRING | Sí | - | La descripción de texto utilizada para generar el video. |
| `resolución` | STRING | Sí | `"480p"`<br>`"720p"`<br>`"1080p"` | La resolución del video de salida. |
| `relación_de_aspecto` | STRING | Sí | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | La relación de aspecto del video de salida. |
| `duración` | INT | Sí | 3 a 12 | La duración del video de salida en segundos (valor predeterminado: 5). |
| `semilla` | INT | No | 0 a 2147483647 | Semilla a utilizar para la generación (valor predeterminado: 0). |
| `cámara_fija` | BOOLEAN | No | - | Especifica si se debe fijar la cámara. La plataforma añade una instrucción para fijar la cámara a tu descripción, pero no garantiza el efecto real (valor predeterminado: False). |
| `marca_de_agua` | BOOLEAN | No | - | Indica si se debe añadir una marca de agua "generado por IA" al video (valor predeterminado: False). |
| `generate_audio` | BOOLEAN | No | - | Este parámetro se ignora para cualquier modelo excepto `seedance-1-5-pro-251215` (valor predeterminado: False). |

**Restricciones de parámetros:**

- El parámetro `prompt` debe contener al menos 1 carácter después de eliminar los espacios en blanco.
- El parámetro `prompt` no puede contener los siguientes parámetros de texto: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- El parámetro `duration` está limitado a valores entre 3 y 12 segundos. Para el modelo `seedance-1-5-pro-251215`, la duración mínima compatible es de 4 segundos.
- El parámetro `seed` acepta valores de 0 a 2,147,483,647.
- El parámetro `generate_audio` solo tiene efecto cuando el `model` está configurado como `seedance-1-5-pro-251215`; se ignora para todos los demás modelos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `output` | VIDEO | El archivo de video generado |

---
**Source fingerprint (SHA-256):** `44ea3e40b99b337340cc39be1c5b6c903680591f1de49b1f2e82f398979355c5`
