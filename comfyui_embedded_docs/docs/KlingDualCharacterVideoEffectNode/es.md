El Nodo de Efecto de Video de Doble Personaje Kling crea videos con efectos especiales basados en la escena seleccionada. Toma dos imágenes y posiciona la primera imagen en el lado izquierdo y la segunda imagen en el lado derecho del video compuesto. Se aplican diferentes efectos visuales dependiendo de la escena de efecto elegida.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen_izquierda` | Imagen del lado izquierdo | IMAGE | Sí | - |
| `imagen_derecha` | Imagen del lado derecho | IMAGE | Sí | - |
| `effect_scene` | El tipo de escena de efecto especial a aplicar en la generación del video | COMBO | Sí | `"chat"`<br>`"dance"`<br>`"hug"`<br>`"kill"`<br>`"kiss"`<br>`"pat"`<br>`"punch"`<br>`"shrug"`<br>`"slap"`<br>`"tickle"` |
| `model_name` | El modelo a utilizar para los efectos de personaje (predeterminado: "kling-v1") | COMBO | No | `"kling-v1"`<br>`"kling-v1-5"`<br>`"kling-v1-6"` |
| `modo` | El modo de generación de video (predeterminado: "std") | COMBO | No | `"std"`<br>`"pro"` |
| `duración` | La duración del video generado en segundos | COMBO | Sí | `"5"`<br>`"10"` |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `duración` | El video generado con efectos de doble personaje | VIDEO |
| `duración` | La información de duración del video generado | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/es.md)

---
**Source fingerprint (SHA-256):** `4ee0c3cd834e1c70e41b40b66ac98d15a8b88993e7dc9d9df9fb4fadb868f079`
