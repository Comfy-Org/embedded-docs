# LatentApplyOperationCFG

El nodo LatentApplyOperationCFG aplica una operación latente para modificar el proceso de guiado de condicionamiento en un modelo. Funciona interceptando las salidas de condicionamiento durante el proceso de muestreo de la guía sin clasificador (CFG) y aplicando la operación especificada a las representaciones latentes antes de que se utilicen para la generación. Cuando el muestreador produce dos salidas de condicionamiento, la operación se aplica a la diferencia entre ambas, y la segunda salida se suma de nuevo al resultado.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al que se le aplicará la operación CFG | MODEL | Sí | - |
| `operación` | La operación latente que se aplicará durante el proceso de muestreo CFG | LATENT_OPERATION | Sí | - |

Nota: Este nodo está marcado como experimental. La operación se aplica a las salidas de condicionamiento del modelo durante el proceso de muestreo CFG. Cuando hay dos salidas de condicionamiento, la operación se aplica a la diferencia entre la primera y la segunda salida, y la segunda salida se suma de nuevo. Cuando solo hay una salida de condicionamiento, la operación se aplica directamente a ella.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo modificado con la operación CFG aplicada a su proceso de muestreo | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/es.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
