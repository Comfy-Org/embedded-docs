> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ReferenceVideoNode/es.md)

El nodo Vidu2 de Generación de Video a partir de Referencia crea un video a partir de un mensaje de texto y múltiples imágenes de referencia. Puedes definir hasta siete sujetos, cada uno con su propio conjunto de imágenes de referencia, y hacer referencia a ellos en el mensaje usando `@subject{subject_id}`. El nodo genera un video con duración, relación de aspecto y movimiento configurables.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | `"viduq2"` | El modelo de IA a utilizar para la generación de video. |
| `sujetos` | AUTOGROW | Sí | N/A | Para cada sujeto, proporciona hasta 3 imágenes de referencia (7 imágenes en total entre todos los sujetos). Haz referencia a ellos en los mensajes mediante `@subject{subject_id}`. |
| `prompt` | STRING | Sí | N/A | La descripción textual utilizada para guiar la generación del video. Cuando el parámetro `audio` está habilitado, el video incluirá voz generada y música de fondo basada en este mensaje. |
| `audio` | BOOLEAN | No | N/A | Cuando está habilitado, el video contendrá voz generada y música de fondo basada en el mensaje (valor predeterminado: `False`). |
| `duración` | INT | No | 1 a 10 | La duración del video generado en segundos (valor predeterminado: `5`). |
| `semilla` | INT | No | 0 a 2147483647 | Número utilizado para controlar la aleatoriedad de la generación y obtener resultados reproducibles (valor predeterminado: `1`). |
| `relación_de_aspecto` | COMBO | No | `"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | La forma del cuadro de video. |
| `resolución` | COMBO | No | `"720p"`<br>`"1080p"` | La resolución en píxeles del video de salida. |
| `amplitud_de_movimiento` | COMBO | No | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | Controla la amplitud de movimiento de los objetos en el cuadro. |

**Restricciones:**

* El `prompt` debe tener entre 1 y 2000 caracteres de longitud.
* Puedes definir múltiples sujetos, pero el número total de imágenes de referencia entre todos los sujetos no debe superar 7.
* Cada sujeto individual puede tener un máximo de 3 imágenes de referencia.
* Cada imagen de referencia debe tener una relación ancho-alto entre 1:4 y 4:1.
* Cada imagen de referencia debe tener al menos 128 píxeles tanto de ancho como de alto.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `3e02b05a0e374442a6ca4ce6a3dbc182b4059e19b5ed7dfc2794e036de7beffd`
