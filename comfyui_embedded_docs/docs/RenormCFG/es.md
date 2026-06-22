# RenormCFG

El nodo RenormCFG modifica el proceso de guía libre de clasificador (CFG) en modelos de difusión aplicando escalado condicional y normalización. Ajusta el proceso de eliminación de ruido según umbrales de paso temporal especificados y factores de renormalización para controlar la influencia de las predicciones condicionales frente a las incondicionales durante la generación de imágenes.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de difusión al que se aplicará la CFG renormalizada | MODEL | Sí | - |
| `cfg_trunc` | Umbral de paso temporal para aplicar el escalado CFG. Cuando el paso temporal actual está por debajo de este valor, se aplica el escalado CFG; de lo contrario, solo se utiliza la predicción condicional (predeterminado: 100.0) | FLOAT | No | 0.0 - 100.0 |
| `renorm_cfg` | Factor de renormalización que limita la norma máxima de la predicción escalada por CFG en relación con la predicción condicional original. Un valor de 0.0 desactiva la renormalización (predeterminado: 1.0) | FLOAT | No | 0.0 - 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `modelo` | El modelo modificado con la función CFG renormalizada aplicada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/es.md)

---
**Source fingerprint (SHA-256):** `b59929606f7519574b7ad14a3caacee51e4f141dd6be3abb594217bcfdbc401e`
