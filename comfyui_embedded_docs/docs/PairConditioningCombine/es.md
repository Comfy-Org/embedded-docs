> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/es.md)

El nodo PairConditioningCombine fusiona dos pares de condicionamiento separados (cada uno compuesto por un condicionamiento positivo y uno negativo) en un único par combinado. Toma el condicionamiento positivo y negativo de dos fuentes diferentes y los combina utilizando la lógica interna de ComfyUI, generando un condicionamiento positivo final y un condicionamiento negativo final. Este nodo es experimental y está diseñado para flujos de trabajo avanzados de manipulación de condicionamiento.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positive_A` | CONDITIONING | Sí | - | Primera entrada de condicionamiento positivo |
| `negative_A` | CONDITIONING | Sí | - | Primera entrada de condicionamiento negativo |
| `positive_B` | CONDITIONING | Sí | - | Segunda entrada de condicionamiento positivo |
| `negative_B` | CONDITIONING | Sí | - | Segunda entrada de condicionamiento negativo |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `positive` | CONDITIONING | Salida de condicionamiento positivo combinado |
| `negative` | CONDITIONING | Salida de condicionamiento negativo combinado |

---
**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`
