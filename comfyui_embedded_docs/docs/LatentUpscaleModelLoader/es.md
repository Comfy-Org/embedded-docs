# Cargar modelo de escalado Latent

```markdown
El nodo LatentUpscaleModelLoader carga un modelo especializado diseñado para el escalado de representaciones latentes. Lee un archivo de modelo desde la carpeta designada del sistema y detecta automáticamente su tipo (720p, 1080p u otro) para instanciar y configurar la arquitectura interna correcta del modelo. El modelo cargado queda listo para ser utilizado por otros nodos en tareas de superresolución en el espacio latente.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model_name` | El nombre del archivo de modelo de escalado latente a cargar. Las opciones disponibles se completan dinámicamente desde los archivos presentes en el directorio `latent_upscale_models` de su ComfyUI. | COMBO | Sí | Todos los archivos en la carpeta `latent_upscale_models` |

Nota: El nodo detecta automáticamente la arquitectura del modelo a partir del contenido del archivo. Los modelos que contienen capas de superresolución HunyuanVideo 720p se cargan como modelos 720p, los modelos con capas de escalado estilo 1080p se cargan como modelos 1080p, y los modelos con otras estructuras de capas se cargan como modelos LatentUpsampler.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo de escalado latente cargado, configurado y listo para usar. | LATENT_UPSCALE_MODEL |
```

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/es.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
