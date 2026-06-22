# Cargar modelo de escalado Latent

El nodo LatentUpscaleModelLoader carga un modelo especializado diseñado para escalar representaciones latentes. Lee un archivo de modelo desde la carpeta designada del sistema y detecta automáticamente su tipo (720p, 1080p u otro) para instanciar y configurar la arquitectura interna correcta del modelo. El modelo cargado está listo para ser utilizado por otros nodos en tareas de superresolución en el espacio latente.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model_name` | El nombre del archivo del modelo de escalado latente a cargar. Las opciones disponibles se completan dinámicamente a partir de los archivos presentes en el directorio `latent_upscale_models` de tu ComfyUI. | STRING | Sí | *Todos los archivos en la carpeta `latent_upscale_models`* |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo de escalado latente cargado, configurado y listo para usar. | LATENT_UPSCALE_MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/es.md)

---
**Source fingerprint (SHA-256):** `bd97f3ec1422aaabbd60779aa4112be44791daddc6307de53ae0e4219a90ab0e`
