# Cargador de Parches de Modelo

El nodo ModelPatchLoader carga un archivo de parche de modelo desde la carpeta `model_patches` y lo prepara para su uso en un flujo de trabajo. Detecta automáticamente el tipo de parche contenido en el archivo, construye la arquitectura correspondiente, carga los pesos guardados y envuelve todo en un model patcher para poder aplicarlo a otros modelos. Admite numerosos formatos de parche especializados, incluidas ramas ControlNet adicionales, modelos de incorporación de características (feature embedder), adaptadores, módulos de guía de animación/LLLite y módulos similares.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `nombre` | El nombre de archivo del parche de modelo que se va a cargar desde la carpeta `model_patches`. Seleccione uno de los archivos de parche disponibles en la lista. | COMBO | Sí | Lista generada dinámicamente con todos los archivos de parche de modelo encontrados en la carpeta `model_patches` |

Nota: Este nodo está marcado como experimental. El tipo de parche se detecta automáticamente a partir del contenido del archivo, por lo que no se requiere seleccionar el tipo manualmente. El nodo lee los metadatos del checkpoint e inspecciona las claves de los pesos para decidir qué arquitectura construir (por ejemplo, Qwen Image block-wise ControlNet, Z-Image ControlNet, Wan Uni3C ControlNet, MiniMax H3 Fun ControlNet, SigLIP feature projection, Lightricks duration head, Anima LLLite, MultiTalk o SUPIR). Los pesos se cargan con la carga segura habilitada y el modelo se coloca en el dispositivo de offload dentro de un `CoreModelPatcher`, de modo que posteriormente pueda aplicarse a otro modelo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `MODEL_PATCH` | El parche de modelo cargado, envuelto en un model patcher y listo para aplicarse a un modelo en el flujo de trabajo | MODEL_PATCH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/es.md)

---
**Source fingerprint (SHA-256):** `069f40b1f108ecd74fc58c12aa2f74edff07f743aa1ed6352ff7bcf0c39341d4`
