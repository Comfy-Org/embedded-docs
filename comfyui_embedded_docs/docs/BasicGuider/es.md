# GuíaBásica

El nodo BasicGuider crea un mecanismo de guiado simple para el proceso de muestreo. Toma un modelo y datos de condicionamiento como entradas y produce un objeto guía que puede utilizarse para guiar el proceso de generación durante el muestreo. Este nodo proporciona la funcionalidad de guiado fundamental necesaria para la generación controlada.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo que se utilizará para el guiado | MODEL | Sí | - |
| `conditioning` | Los datos de condicionamiento que guían el proceso de generación | CONDITIONING | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `GUIDER` | Un objeto guía que puede utilizarse durante el proceso de muestreo para guiar la generación | GUIDER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/es.md)

---
**Source fingerprint (SHA-256):** `8ea6b56be58ae99baaf13a04c4fadbf8ad921801d8f2ce2aecce768cc34a3b20`
