> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/en.md)

## Resumen

Este nodo carga un modelo de interpolación de fotogramas desde un archivo y lo prepara para su uso en el flujo de trabajo. Detecta automáticamente el tipo de modelo (FILM o RIFE) y lo configura para un rendimiento óptimo en tu hardware.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model_name` | STRING | Sí | Lista de archivos de modelo en la carpeta `frame_interpolation` | Selecciona un modelo de interpolación de fotogramas para cargar. Los modelos deben colocarse en la carpeta 'frame_interpolation'. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `FRAME_INTERPOLATION_MODEL` | MODEL | El modelo de interpolación de fotogramas cargado y configurado, listo para usar en otros nodos. |

---
**Source fingerprint (SHA-256):** `497c20d5123bcbfd321dc4a659250ce3e0903e55c3a0274d3ed45710d75573d9`
