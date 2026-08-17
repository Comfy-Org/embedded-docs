# Cargar modelo de flujo óptico

## Resumen

Carga un modelo de flujo óptico desde la carpeta `models/optical_flow/`. Actualmente, solo se admite el formato RAFT-large de torchvision, que es el modelo utilizado por el nodo VOIDWarpedNoise. ComfyUI no descarga los pesos de flujo óptico automáticamente; debes colocar el archivo de checkpoint manualmente en el directorio `models/optical_flow/`.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model_name` | Modelo de flujo óptico a cargar. Los archivos deben colocarse en la carpeta `optical_flow`. Hoy en día solo se admite `raft_large.pth` de torchvision. | COMBO | Sí | Lista de archivos en la carpeta `models/optical_flow/` |

El archivo seleccionado debe ser un checkpoint RAFT-large de torchvision. El nodo verifica que el archivo contenga las claves RAFT esperadas (`feature_encoder.*`, `context_encoder.*` y `update_block.*`) y lanza un ValueError si el formato no es reconocido.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `OPTICAL_FLOW` | El modelo de flujo óptico cargado, envuelto en un ModelPatcher para usarlo con otros nodos. | OPTICAL_FLOW |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/es.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
