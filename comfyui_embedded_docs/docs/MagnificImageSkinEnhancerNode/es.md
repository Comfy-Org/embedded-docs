> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageSkinEnhancerNode/es.md)

El nodo Mejorador de Piel de Magnific Image aplica un procesamiento de IA especializado a imágenes de retratos para mejorar la apariencia de la piel. Ofrece tres modos distintos para diferentes objetivos de mejora: creativo para efectos artísticos, fiel para preservar el aspecto original y flexible para mejoras específicas como iluminación o realismo. El nodo carga la imagen a una API externa para su procesamiento y devuelve el resultado mejorado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de retrato a mejorar. |
| `sharpen` | INT | No | 0 a 100 | Nivel de intensidad de nitidez (predeterminado: 0). |
| `smart_grain` | INT | No | 0 a 100 | Nivel de intensidad de granulado inteligente (predeterminado: 2). |
| `mode` | COMBO | Sí | `"creative"`<br>`"faithful"`<br>`"flexible"` | El modo de procesamiento a utilizar. `"creative"` es para mejora artística, `"faithful"` para preservar la apariencia original y `"flexible"` para optimización específica. |
| `skin_detail` | INT | No | 0 a 100 | Nivel de mejora del detalle de la piel. Esta entrada solo está disponible y es obligatoria cuando el `mode` está configurado en `"faithful"` (predeterminado: 80). |
| `optimized_for` | COMBO | No | `"enhance_skin"`<br>`"improve_lighting"`<br>`"enhance_everything"`<br>`"transform_to_real"`<br>`"no_make_up"` | Objetivo de optimización de mejora. Esta entrada solo está disponible y es obligatoria cuando el `mode` está configurado en `"flexible"`. |

**Restricciones:**

* El nodo acepta exactamente una imagen de entrada.
* La imagen de entrada debe tener una altura y anchura mínimas de 160 píxeles.
* La relación de aspecto de la imagen de entrada debe estar entre 1:3 y 3:1 (validación no estricta).
* El parámetro `skin_detail` solo está activo cuando `mode` está configurado en `"faithful"`.
* El parámetro `optimized_for` solo está activo cuando `mode` está configurado en `"flexible"`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen de retrato mejorada. |

---
**Source fingerprint (SHA-256):** `e02cae2e119ddab931b790865889adf53f47a2ebb03d488477c289dfda7204f5`
