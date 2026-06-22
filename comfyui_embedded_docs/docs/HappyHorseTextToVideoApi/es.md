# HappyHorse Texto a Video

Genera un video basado en un texto de instrucción utilizando el modelo HappyHorse. Este nodo envía su instrucción y configuración a la API de HappyHorse, espera a que se genere el video y luego descarga el resultado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | Un diccionario que contiene la selección del modelo y sus parámetros asociados. El modelo debe ser `"happyhorse-1.0-t2v"`. Este diccionario incluye los siguientes subparámetros:<br><br>**`prompt`** (STRING): La descripción textual del video que desea generar. Compatible con inglés y chino. (predeterminado: "").<br>**`resolution`** (COMBO): La resolución del video de salida. Opciones: `"720P"`, `"1080P"`.<br>**`ratio`** (COMBO): La relación de aspecto del video de salida. Opciones: `"16:9"`, `"9:16"`, `"1:1"`, `"4:3"`, `"3:4"`.<br>**`duration`** (INT): La duración del video en segundos. (predeterminado: 5, mínimo: 3, máximo: 15, paso: 1). | DICT | Sí | Ver Descripción |
| `semilla` | Semilla a utilizar para la generación. Usar la misma semilla con las mismas entradas producirá el mismo resultado. (predeterminado: 0). | INT | Sí | 0 a 2147483647 |
| `marca de agua` | Si se debe agregar una marca de agua de IA generada al resultado. (predeterminado: False). | BOOLEAN | No | True / False |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `VIDEO` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/es.md)

---
**Source fingerprint (SHA-256):** `8c6a7c0c2b10bbc65ca54abc991e1f12e8846b31701ed65b49c5d71f1b2a63ec`
