> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/en.md)

## Resumen

Carga un modelo MoGe (Geometría Monocular) desde un archivo y lo prepara para su uso en tareas de estimación geométrica. Este nodo lee un archivo de modelo de la carpeta `geometry_estimation` e inicializa el modelo MoGe con sus pesos entrenados.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model_name` | STRING | Sí | Lista de archivos de modelo disponibles en la carpeta `geometry_estimation` | El nombre del archivo del modelo MoGe a cargar. Selecciona entre los archivos de modelo disponibles en tu instalación de ComfyUI. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `MOGE_MODEL` | MOGE_MODEL | La instancia del modelo MoGe cargada, lista para usar en flujos de trabajo de estimación geométrica. |

---
**Source fingerprint (SHA-256):** `4707002565181ca17936ecf87ea8059630c97c44c17facfecd04053d9581b7d1`
