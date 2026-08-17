# Modelo de Parche Tome

El nodo TomePatchModel aplica la fusión de tokens (ToMe) a un modelo de difusión para reducir los requisitos computacionales durante la inferencia. Funciona fusionando selectivamente tokens similares en el mecanismo de atención, lo que permite que el modelo procese menos tokens mientras mantiene la calidad de la imagen. Esta técnica ayuda a acelerar la generación sin una pérdida significativa de calidad.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión al que se le aplicará la fusión de tokens | MODEL | Sí | - |
| `ratio` | La proporción de tokens a fusionar (predeterminado: 0.3, paso: 0.01). Valores más altos fusionan más tokens, lo que resulta en una mayor aceleración pero potencialmente menor calidad. | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo modificado con la fusión de tokens aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/es.md)

---
**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`
