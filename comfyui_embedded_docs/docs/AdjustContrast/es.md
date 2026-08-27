# Ajustar contraste

El nodo Adjust Contrast modifica el nivel de contraste de una imagen de entrada. Funciona ajustando la diferencia entre las áreas claras y oscuras de la imagen. Un factor de 1.0 deja la imagen sin cambios, los valores por debajo de 1.0 reducen el contraste y los valores por encima de 1.0 lo aumentan.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen de entrada cuyo contraste se ajustará. | IMAGE | Sí | - |
| `factor` | Factor de contraste. 1.0 = sin cambios, <1.0 = menos contraste, >1.0 = más contraste. (por defecto: 1.0) | FLOAT | No | 0.0 - 2.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `imágenes` | La imagen resultante con el contraste ajustado. Los valores de píxeles se limitan al rango 0.0–1.0. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/es.md)

---
**Source fingerprint (SHA-256):** `1f5fbd0f0b739492bc171d3c43ea2150a3ca76dc3ede9bf63cb97c45a90b9e44`
