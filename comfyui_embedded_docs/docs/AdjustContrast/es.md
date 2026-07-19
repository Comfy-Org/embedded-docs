# Ajustar contraste

El nodo Ajustar Contraste modifica el nivel de contraste de una imagen de entrada. Funciona ajustando la diferencia entre las áreas claras y oscuras de la imagen. Un factor de 1.0 deja la imagen sin cambios, los valores por debajo de 1.0 reducen el contraste y los valores por encima de 1.0 lo aumentan.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen de entrada a la que se le ajustará el contraste. | IMAGE | Sí | - |
| `factor` | Factor de contraste. 1.0 = sin cambios, <1.0 = menos contraste, >1.0 = más contraste. (predeterminado: 1.0) | FLOAT | No | 0.0 - 2.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `imágenes` | La imagen resultante con el contraste ajustado. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/es.md)

---
**Source fingerprint (SHA-256):** `01148cdd9d951e78c712c1c3159c5562a680a5147bd4a76e33d91543d5245854`
