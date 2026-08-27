# Ajustar brillo

El nodo Adjust Brightness modifica el brillo de una imagen de entrada. Funciona multiplicando el valor de cada píxel por un factor especificado y luego limitando los valores resultantes para que se mantengan dentro de un rango válido. Un factor de 1.0 deja la imagen sin cambios, los valores inferiores a 1.0 la oscurecen y los valores superiores a 1.0 la aclaran.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen de entrada a ajustar. | IMAGE | Sí | - |
| `factor` | Factor de brillo. 1.0 = sin cambios, <1.0 = más oscuro, >1.0 = más brillante. (predeterminado: 1.0) | FLOAT | No | 0.0 - 2.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `imágenes` | La imagen de salida con el brillo ajustado. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/es.md)

---
**Source fingerprint (SHA-256):** `696fb3c0bfc8edccc2049dad8f44b4b056fe1caa95b0cc0126164269cb65ab1a`
