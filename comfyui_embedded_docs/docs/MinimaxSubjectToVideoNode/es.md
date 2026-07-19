# MinimaxSubjectToVideoNode

Genera un video de forma sincrónica basado en una imagen de sujeto y un texto de instrucción utilizando la API de MiniMax. Este nodo toma una imagen de un sujeto y una descripción para crear un video que anime o muestre a dicho sujeto según la instrucción.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `subject` | Imagen del sujeto a referenciar para la generación del video | IMAGE | Sí | - |
| `prompt_text` | Texto de instrucción para guiar la generación del video (predeterminado: cadena vacía) | STRING | Sí | - |
| `model` | Modelo a utilizar para la generación del video (predeterminado: "S2V-01") | COMBO | No | "S2V-01" |
| `seed` | Semilla aleatoria utilizada para crear el ruido (predeterminado: 0) | INT | No | 0 a 18446744073709551615 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El video generado basado en la imagen de sujeto y la instrucción de entrada | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `69651367e6c452ec1f3a4765b74a28cc6b579288f3319ed70fa7c16a1ced0dbc`
