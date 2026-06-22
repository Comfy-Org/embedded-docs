# ByteDance Seedance 2.0 Texto a Video

Este nodo utiliza la API Seedance 2.0 de ByteDance para generar un video a partir de una descripción textual. Envía tu indicación al modelo seleccionado, espera a que el video sea procesado y devuelve el resultado final.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo a utilizar para la generación de video. Al seleccionar un modelo, se mostrarán entradas adicionales obligatorias para la indicación, resolución, relación de aspecto, duración y generación de audio. "Seedance 2.0" es para máxima calidad; "Seedance 2.0 Fast" está optimizado para velocidad. | COMBO | Sí | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` |
| `semilla` | Un valor de semilla (predeterminado: 0). El nodo se volverá a ejecutar si este valor cambia, pero los resultados no son deterministas independientemente de la semilla. | INT | No | 0 a 2147483647 |
| `marca_de_agua` | Si se debe agregar una marca de agua al video (predeterminado: Falso). Esta es una configuración avanzada. | BOOLEAN | No | Verdadero / Falso |

**Nota:** El parámetro `model` es un combo dinámico. Cuando seleccionas un modelo, se mostrarán varios subparámetros obligatorios que deben completarse, incluyendo la indicación de texto, resolución, relación de aspecto, duración y si se debe generar audio. El texto de la indicación debe tener al menos 1 carácter después de eliminar los espacios en blanco.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `f8552e47667ff4b1ad3c8c1c074d70bdc45227b79b026b4b3c06986443655473`
