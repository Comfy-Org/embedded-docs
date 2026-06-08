El nodo BasicGuider crea un mecanismo de guía simple para el proceso de muestreo. Toma un modelo y datos de condicionamiento como entradas y produce un objeto guía que puede utilizarse para dirigir el proceso de generación durante el muestreo. Este nodo proporciona la funcionalidad de guía fundamental necesaria para una generación controlada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo que se utilizará para la guía | MODEL | Sí | - |
| `acondicionamiento` | Los datos de condicionamiento que dirigen el proceso de generación | CONDITIONING | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `GUIDER` | Un objeto guía que puede utilizarse durante el proceso de muestreo para dirigir la generación | GUIDER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/es.md)

---
**Source fingerprint (SHA-256):** `012171caea6aacfadaabacb746be104ca783ae5ea5834cc4a67088233b835654`
