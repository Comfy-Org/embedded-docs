El nodo CheckpointLoader carga un punto de control de un modelo preentrenado junto con su archivo de configuración. Toma un archivo de configuración y un archivo de punto de control como entradas y devuelve los componentes del modelo cargado, incluidos el modelo principal, el modelo CLIP y el modelo VAE para su uso en el flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `nombre_configuración` | El archivo de configuración que define la arquitectura y los ajustes del modelo | STRING | Sí | Archivos de configuración disponibles |
| `nombre_ckpt` | El archivo de punto de control que contiene los pesos y parámetros del modelo entrenado | STRING | Sí | Archivos de punto de control disponibles |

**Nota:** Este nodo requiere que se seleccionen tanto un archivo de configuración como un archivo de punto de control. El archivo de configuración debe coincidir con la arquitectura del archivo de punto de control que se está cargando.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `MODEL` | El componente del modelo principal cargado, listo para inferencia | MODEL |
| `CLIP` | El componente del modelo CLIP cargado para codificación de texto | CLIP |
| `VAE` | El componente del modelo VAE cargado para codificación y decodificación de imágenes | VAE |

**Nota importante:** Este nodo ha sido marcado como obsoleto y podría eliminarse en versiones futuras. Considere usar nodos de carga alternativos para nuevos flujos de trabajo.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/es.md)

---
**Source fingerprint (SHA-256):** `9977bda5e124a9d10566839cbee868c74fab120c454141f27ce145efa60105e9`
