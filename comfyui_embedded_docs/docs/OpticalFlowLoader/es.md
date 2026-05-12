> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/es.md)

## Vista General

Carga un modelo de flujo óptico desde la carpeta `models/optical_flow/`. Actualmente, solo se admite el formato RAFT-large de torchvision, que es el modelo utilizado por el nodo VOIDWarpedNoise. ComfyUI no descarga los pesos del flujo óptico automáticamente; debes colocar el archivo de checkpoint manualmente en el directorio `models/optical_flow/`.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model_name` | STRING | Sí | Lista de archivos en la carpeta `models/optical_flow/` | Modelo de flujo óptico a cargar. Los archivos deben colocarse en la carpeta `optical_flow`. Actualmente solo se admite `raft_large.pth` de torchvision. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `OPTICAL_FLOW` | MODEL | El modelo de flujo óptico cargado, envuelto en un ModelPatcher para su uso con otros nodos. |