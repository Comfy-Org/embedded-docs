El nodo Ajustar Brillo modifica el brillo de una imagen de entrada. Funciona multiplicando el valor de cada píxel por un factor especificado y luego recortando los valores resultantes para que permanezcan dentro de un rango válido. Un factor de 1.0 deja la imagen sin cambios, los valores por debajo de 1.0 la oscurecen y los valores por encima de 1.0 la aclaran.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen de entrada a ajustar. | IMAGE | Sí | - |
| `factor` | Factor de brillo. 1.0 = sin cambios, <1.0 = más oscuro, >1.0 = más brillante. (predeterminado: 1.0) | FLOAT | No | 0.0 - 2.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `image` | La imagen de salida con el brillo ajustado. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/es.md)

---
**Source fingerprint (SHA-256):** `c8f2fbb5fa149812a2ecd1ff9fce7bd6d29bf4c48b929e9ebc0a95c9e46ec65e`
