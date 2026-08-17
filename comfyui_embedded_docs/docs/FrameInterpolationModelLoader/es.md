# Cargar modelo de interpolación de fotogramas

Este nodo carga un modelo de interpolación de fotogramas desde un archivo y lo prepara para su uso en el flujo de trabajo. Detecta automáticamente el tipo de modelo (FILM o RIFE) y lo configura para un rendimiento óptimo en su hardware.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model_name` | Seleccione un modelo de interpolación de fotogramas para cargar. Los modelos deben estar ubicados en la carpeta 'frame_interpolation'. | COMBO | Sí | Lista de archivos de modelo en la carpeta `frame_interpolation` |

Nota: Si el archivo seleccionado no es un modelo de interpolación de fotogramas FILM o RIFE reconocido, el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `FRAME_INTERPOLATION_MODEL` | El modelo de interpolación de fotogramas cargado y configurado, listo para usar en otros nodos. | INTERP_MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/es.md)

---
**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`
