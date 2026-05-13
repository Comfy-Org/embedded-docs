> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/es.md)

Genera un video de forma sincrónica basado en una imagen de sujeto y un texto de instrucción utilizando la API de MiniMax. Este nodo toma una imagen de un sujeto y una descripción para crear un video que anime o muestre a dicho sujeto según la instrucción.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `subject` | IMAGE | Sí | - | Imagen del sujeto a referenciar para la generación del video |
| `prompt_text` | STRING | Sí | - | Texto de instrucción para guiar la generación del video (predeterminado: cadena vacía) |
| `model` | COMBO | No | "S2V-01" | Modelo a utilizar para la generación del video (predeterminado: "S2V-01") |
| `seed` | INT | No | 0 a 18446744073709551615 | Semilla aleatoria utilizada para crear el ruido (predeterminado: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El video generado basado en la imagen de sujeto y la instrucción de entrada |

---
**Source fingerprint (SHA-256):** `69651367e6c452ec1f3a4765b74a28cc6b579288f3319ed70fa7c16a1ced0dbc`
