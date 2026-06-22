# SUPIRApply

El nodo `SUPIRApply` aplica un parche del modelo SUPIR a un modelo de difusión. Utiliza el parche para modificar el comportamiento del modelo, permitiéndole incorporar guía de una imagen de entrada durante el proceso de muestreo. El nodo también proporciona controles para ajustar la intensidad de esta guía a lo largo del tiempo e incluye una función opcional para ayudar a mantener la fidelidad a la imagen original.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión base al que se aplicará el parche SUPIR. | MODEL | Sí | - |
| `model_patch` | El parche del modelo SUPIR que contiene los pesos y la configuración para modificar el modelo. | MODELPATCH | Sí | - |
| `vae` | El VAE (Autoencoder Variacional) utilizado para codificar la imagen de entrada en una representación latente. | VAE | Sí | - |
| `image` | La imagen de entrada utilizada para guiar el proceso de generación. Solo se utilizan los tres primeros canales de color (RGB). | IMAGE | Sí | - |
| `strength_start` | Intensidad de control al inicio del muestreo (sigma alto). La influencia de la guía de imagen comienza en este valor. (predeterminado: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `strength_end` | Intensidad de control al final del muestreo (sigma bajo). Se interpola linealmente desde el inicio. La influencia de la guía de imagen termina en este valor. (predeterminado: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `restore_cfg` | Atrae la salida denoizada hacia el latente de entrada. Un valor más alto implica mayor fidelidad a la entrada. Use 0 para deshabilitar. (predeterminado: 4.0) | FLOAT | No | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | Umbral de sigma por debajo del cual se deshabilita `restore_cfg`. (predeterminado: 0.05) | FLOAT | No | 0.0 - 1.0 |

*Nota:* La entrada `image` se procesa para extraer únicamente los canales RGB. Si se proporciona una imagen con un canal alfa, este se ignora.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo de difusión con el parche SUPIR aplicado y cualquier función adicional posterior a CFG configurada. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/es.md)

---
**Source fingerprint (SHA-256):** `32ba7a337060b52d4c9085a6a2bc209c737e374dee4291d431d2caf768fc2817`
