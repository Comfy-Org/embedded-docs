# Cargar Depth Anything 3

Este nodo carga un modelo Depth Anything 3 desde un archivo, preparándolo para su uso en tareas de estimación de profundidad. Permite seleccionar el archivo del modelo y, opcionalmente, especificar la precisión numérica (tipo de dato) para los pesos del modelo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `model_name` | El nombre del archivo del modelo Depth Anything 3 a cargar. | STRING | Sí | Lista de archivos de modelo disponibles en la carpeta `geometry_estimation` |
| `weight_dtype` | La precisión numérica (tipo de dato) para los pesos del modelo. La opción "default" utiliza la precisión original del modelo. (predeterminado: "default") | STRING | No | `"default"`<br>`"fp16"`<br>`"bf16"`<br>`"fp32"` |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `DA3_MODEL` | El modelo Depth Anything 3 cargado, listo para usar en flujos de trabajo de estimación de profundidad. | DA3_MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadDA3Model/es.md)

---
**Source fingerprint (SHA-256):** `b1b3f4075cd9172bc1f274848b9300bca20d3cbd53b23d3c4a9f0986b36e409e`
