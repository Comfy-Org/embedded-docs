# Modelo de Parche Tome

TomePatchModel aplica Token Merging (ToMe) a un modelo de difusión para reducir los requisitos computacionales durante la inferencia. Funciona fusionando selectivamente tokens similares en el mecanismo de atención, lo que permite al modelo procesar menos tokens mientras mantiene la calidad de imagen. Esta técnica ayuda a acelerar la generación sin una pérdida significativa de calidad.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de difusión al que se le aplicará la fusión de tokens | MODEL | Sí | - |
| `ratio` | La proporción de tokens a fusionar (predeterminado: 0.3). Los valores más altos fusionan más tokens, lo que resulta en una mayor aceleración pero potencialmente menor calidad. | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con la fusión de tokens aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/es.md)

---
**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`
