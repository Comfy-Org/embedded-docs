> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/es.md)

El Nodo de Efecto de Video de Doble Personaje Kling crea videos con efectos especiales basados en la escena seleccionada. Toma dos imágenes y posiciona la primera imagen en el lado izquierdo y la segunda imagen en el lado derecho del video compuesto. Se aplican diferentes efectos visuales dependiendo de la escena de efecto elegida.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `imagen_izquierda` | IMAGE | Sí | - | Imagen del lado izquierdo |
| `imagen_derecha` | IMAGE | Sí | - | Imagen del lado derecho |
| `effect_scene` | COMBO | Sí | `"chat"`<br>`"dance"`<br>`"hug"`<br>`"kill"`<br>`"kiss"`<br>`"pat"`<br>`"punch"`<br>`"shrug"`<br>`"slap"`<br>`"tickle"` | El tipo de escena de efecto especial a aplicar en la generación del video |
| `model_name` | COMBO | No | `"kling-v1"`<br>`"kling-v1-5"`<br>`"kling-v1-6"` | El modelo a utilizar para los efectos de personaje (predeterminado: "kling-v1") |
| `modo` | COMBO | No | `"std"`<br>`"pro"` | El modo de generación de video (predeterminado: "std") |
| `duración` | COMBO | Sí | `"5"`<br>`"10"` | La duración del video generado en segundos |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `duración` | VIDEO | El video generado con efectos de doble personaje |
| `duración` | STRING | La información de duración del video generado |

---
**Source fingerprint (SHA-256):** `4ee0c3cd834e1c70e41b40b66ac98d15a8b88993e7dc9d9df9fb4fadb868f079`
