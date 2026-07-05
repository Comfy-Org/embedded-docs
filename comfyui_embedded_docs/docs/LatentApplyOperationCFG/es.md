# LatentApplyOperationCFG

El nodo LatentApplyOperationCFG aplica una operación latente para modificar el proceso de guiado de condicionamiento en un modelo. Funciona interceptando las salidas de condicionamiento durante el proceso de muestreo de guiado sin clasificador (CFG) y aplicando la operación especificada a las representaciones latentes antes de que se utilicen para la generación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al que se aplicará la operación CFG | MODEL | Sí | - |
| `operación` | La operación latente a aplicar durante el proceso de muestreo CFG | LATENT_OPERATION | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `modelo` | El modelo modificado con la operación CFG aplicada a su proceso de muestreo | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/es.md)

---
**Source fingerprint (SHA-256):** `9fbcc9183abf89bb93e55263bb655e931549360c05a561f7dacae8723db62e52`
