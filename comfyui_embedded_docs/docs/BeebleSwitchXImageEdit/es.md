> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXImageEdit/es.md)

# BeebleSwitchXImageEdit

## Resumen

Edita una sola imagen con Beeble SwitchX. Este nodo puede cambiar cualquier elemento de la escena (fondo, iluminación, vestimenta) mientras preserva los píxeles del sujeto original. Proporciona una imagen de referencia y/o un prompt de texto para describir el nuevo aspecto. La resolución máxima es de aproximadamente 2,77 megapíxeles.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de origen a editar. |
| `prompt` | STRING | Sí | - | Una descripción textual del nuevo aspecto deseado (ej., "un caballero con armadura brillante"). |
| `modo_alpha` | COMBO | Sí | `"select"`<br>`"fill"`<br>`"custom"` | Cómo manejar el matte alfa. "select" usa un fotograma clave para seleccionar el sujeto, "fill" reemplaza toda la imagen sin un matte separado, "custom" usa una máscara proporcionada por el usuario. |
| `resolución_máxima` | COMBO | Sí | `"1080p"`<br>`"720p"` | La resolución máxima para la imagen de salida. Una resolución más alta consume más créditos. |
| `semilla` | INT | Sí | - | Un valor de semilla para reproducibilidad. |
| `imagen_de_referencia` | IMAGE | No | - | Una imagen de referencia opcional para guiar el estilo o la apariencia de los nuevos elementos de la escena. |

**Nota sobre `alpha_mode`:** Cuando `alpha_mode` está configurado en `"select"`, también debes proporcionar un `alpha_keyframe` (una imagen de fotograma clave usada para seleccionar el sujeto). Cuando está configurado en `"custom"`, debes proporcionar un `alpha_mask` (una máscara creada por el usuario). Cuando está configurado en `"fill"`, no se necesita entrada alfa.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `alfa` | IMAGE | La imagen editada con los elementos de la escena cambiados. |
| `alpha` | MASK | El matte alfa utilizado por Beeble. Vacío para el modo "fill", que no tiene matte separado. |

---
**Source fingerprint (SHA-256):** `41f23435686626e3ade28708fcb1da192ded347b210080ee9b17834ea8b727fb`
