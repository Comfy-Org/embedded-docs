> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/es.md)

El nodo SUPIRApply aplica un parche de modelo SUPIR a un modelo de difusión. Utiliza el parche para modificar el comportamiento del modelo, permitiéndole incorporar orientación de una imagen de entrada durante el proceso de muestreo. El nodo también proporciona controles para ajustar la intensidad de esta orientación a lo largo del tiempo e incluye una función opcional para ayudar a mantener la fidelidad a la entrada original.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de difusión base al que se aplicará el parche SUPIR. |
| `model_patch` | MODELPATCH | Sí | - | El parche de modelo SUPIR que contiene los pesos y la configuración para modificar el modelo. |
| `vae` | VAE | Sí | - | El VAE (Autoencoder Variacional) utilizado para codificar la imagen de entrada en una representación latente. |
| `image` | IMAGE | Sí | - | La imagen de entrada utilizada para guiar el proceso de generación. Solo se utilizan los primeros tres canales de color (RGB). |
| `strength_start` | FLOAT | No | 0.0 - 10.0 | Intensidad de control al inicio del muestreo (sigma alto). La influencia de la orientación de la imagen comienza en este valor. (predeterminado: 1.0) |
| `strength_end` | FLOAT | No | 0.0 - 10.0 | Intensidad de control al final del muestreo (sigma bajo). Se interpola linealmente desde el inicio. La influencia de la orientación de la imagen termina en este valor. (predeterminado: 1.0) |
| `restore_cfg` | FLOAT | No | 0.0 - 20.0 | Atrae la salida desruidizada hacia el latente de entrada. Mayor valor = mayor fidelidad a la entrada. 0 para desactivar. (predeterminado: 4.0) |
| `restore_cfg_s_tmin` | FLOAT | No | 0.0 - 1.0 | Umbral de sigma por debajo del cual se desactiva `restore_cfg`. (predeterminado: 0.05) |

*Nota:* La entrada `image` se procesa para extraer solo los canales RGB. Si se proporciona una imagen con un canal alfa, este se ignora.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo de difusión con el parche SUPIR aplicado y cualquier función post-CFG adicional configurada. |