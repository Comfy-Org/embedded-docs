## Descripción general

Carga un modelo de flujo óptico desde la carpeta `models/optical_flow/`. Actualmente, solo se admite el formato RAFT-large de torchvision, que es el modelo utilizado por el nodo VOIDWarpedNoise. ComfyUI no descarga los pesos del flujo óptico automáticamente; debes colocar el archivo de checkpoint manualmente en el directorio `models/optical_flow/`.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model_name` | Modelo de flujo óptico a cargar. Los archivos deben colocarse en la carpeta `optical_flow`. Actualmente solo se admite `raft_large.pth` de torchvision. | STRING | Sí | Lista de archivos en la carpeta `models/optical_flow/` |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `OPTICAL_FLOW` | El modelo de flujo óptico cargado, envuelto en un ModelPatcher para su uso con otros nodos. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/es.md)

---
**Source fingerprint (SHA-256):** `94bab0bb7e2b9d9b3f343337799eccc744f79275b72a6fad9681b408b4a0820b`
