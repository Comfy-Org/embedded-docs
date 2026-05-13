> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/es.md)

El nodo TomePatchModel aplica Token Merging (ToMe) a un modelo de difusión para reducir los requisitos computacionales durante la inferencia. Funciona fusionando selectivamente tokens similares en el mecanismo de atención, lo que permite que el modelo procese menos tokens mientras mantiene la calidad de la imagen. Esta técnica ayuda a acelerar la generación sin una pérdida significativa de calidad.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo de difusión al que se aplicará la fusión de tokens |
| `ratio` | FLOAT | No | 0.0 - 1.0 | La proporción de tokens a fusionar (predeterminado: 0.3) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `modelo` | MODEL | El modelo modificado con la fusión de tokens aplicada |

---
**Source fingerprint (SHA-256):** `23d63ffa1b468a8a41533cc926125f4ef566b13edd1d95a6ef1ae63096a9d878`
