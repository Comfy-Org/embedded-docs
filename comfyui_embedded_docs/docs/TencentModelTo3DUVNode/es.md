> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentModelTo3DUVNode/es.md)

Este nodo utiliza la API Tencent Hunyuan3D para realizar el desplegado UV de un modelo 3D. Toma un archivo de modelo 3D como entrada, lo envía a la API para su procesamiento y devuelve el modelo procesado en formatos OBJ y FBX junto con una imagen de textura UV generada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Sí | GLB<br>OBJ<br>FBX | Modelo 3D de entrada (GLB, OBJ o FBX). El modelo debe tener menos de 30000 caras. |
| `seed` | INT | No | 0 a 2147483647 | Un valor de semilla (por defecto: 1). Esto controla si el nodo debe volver a ejecutarse, pero los resultados no son deterministas independientemente del valor de la semilla. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `OBJ` | FILE3D | El archivo del modelo 3D procesado en formato OBJ. |
| `FBX` | FILE3D | El archivo del modelo 3D procesado en formato FBX. |
| `Image` | IMAGE | La imagen de textura UV generada. |
