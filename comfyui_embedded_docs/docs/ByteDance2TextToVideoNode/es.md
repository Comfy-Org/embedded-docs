> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/es.md)

Este nodo utiliza la API Seedance 2.0 de ByteDance para generar un video a partir de una descripción textual. Envía tu indicación al modelo seleccionado, espera a que el video sea procesado y devuelve el resultado final.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | El modelo a utilizar para la generación de video. Al seleccionar un modelo, se mostrarán entradas adicionales obligatorias para la indicación, resolución, relación de aspecto, duración y generación de audio. "Seedance 2.0" es para máxima calidad; "Seedance 2.0 Fast" está optimizado para velocidad. |
| `semilla` | INT | No | 0 a 2147483647 | Un valor de semilla (predeterminado: 0). El nodo se volverá a ejecutar si este valor cambia, pero los resultados no son deterministas independientemente de la semilla. |
| `marca_de_agua` | BOOLEAN | No | Verdadero / Falso | Si se debe agregar una marca de agua al video (predeterminado: Falso). Esta es una configuración avanzada. |

**Nota:** El parámetro `model` es un combo dinámico. Cuando seleccionas un modelo, se mostrarán varios subparámetros obligatorios que deben completarse, incluyendo la indicación de texto, resolución, relación de aspecto, duración y si se debe generar audio. El texto de la indicación debe tener al menos 1 carácter después de eliminar los espacios en blanco.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `video` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `f8552e47667ff4b1ad3c8c1c074d70bdc45227b79b026b4b3c06986443655473`
