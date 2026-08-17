# SUPIRApply

El nodo SUPIRApply aplica un parche de modelo SUPIR a un modelo de difusión. Utiliza el parche para modificar el comportamiento del modelo, permitiéndole incorporar la guía de una imagen de entrada durante el proceso de muestreo. El nodo también proporciona controles para ajustar la fuerza de esta guía a lo largo del tiempo e incluye una función opcional para ayudar a mantener la fidelidad a la entrada original.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión base al que se aplicará el parche SUPIR. | MODEL | Sí | - |
| `model_patch` | El parche de modelo SUPIR que contiene los pesos y la configuración para modificar el modelo. | MODELPATCH | Sí | - |
| `vae` | El VAE (autoencoder variacional) utilizado para codificar la imagen de entrada en una representación latente. | VAE | Sí | - |
| `image` | La imagen de entrada utilizada para guiar el proceso de generación. Solo se utilizan los primeros tres canales de color (RGB). | IMAGE | Sí | - |
| `strength_start` | Fuerza de control al inicio del muestreo (sigma alto). La influencia de la guía de imagen comienza en este valor. (predeterminado: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `strength_end` | Fuerza de control al final del muestreo (sigma bajo). Se interpola linealmente desde el inicio. La influencia de la guía de imagen termina en este valor. (predeterminado: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `restore_cfg` | Atrae la salida denoizada hacia el latente de entrada. Mayor valor = mayor fidelidad a la entrada. 0 para desactivar. (predeterminado: 4.0) | FLOAT | No | 0.0 - 20.0 |
| `restore_cfg_s_tmin` | Umbral de sigma por debajo del cual se desactiva restore_cfg. (predeterminado: 0.05) | FLOAT | No | 0.0 - 1.0 |

*Nota:* La entrada `image` se procesa para extraer solo los canales RGB. Si se proporciona una imagen con canal alfa, se ignora el canal alfa.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo de difusión con el parche SUPIR aplicado y cualquier función post-CFG adicional configurada. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/es.md)

---
**Source fingerprint (SHA-256):** `fa9f67f63777160863c44c620d8de11e92f79245c3f5b60e138975dfd0cc65c7`
