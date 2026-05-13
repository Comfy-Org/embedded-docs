> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/es.md)

El nodo LatentApplyOperationCFG aplica una operación latente para modificar el proceso de guiado de condicionamiento en un modelo. Funciona interceptando las salidas de condicionamiento durante el proceso de muestreo de guiado sin clasificador (CFG) y aplicando la operación especificada a las representaciones latentes antes de que se utilicen para la generación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que se aplicará la operación CFG |
| `operation` | LATENT_OPERATION | Sí | - | La operación latente a aplicar durante el proceso de muestreo CFG |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `model` | MODEL | El modelo modificado con la operación CFG aplicada a su proceso de muestreo |

---
**Source fingerprint (SHA-256):** `9fbcc9183abf89bb93e55263bb655e931549360c05a561f7dacae8723db62e52`
