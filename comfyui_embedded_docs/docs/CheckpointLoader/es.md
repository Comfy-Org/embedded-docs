# Cargar Punto de Control Con Configuración (OBSOLETO)

El nodo CheckpointLoader carga un checkpoint de modelo preentrenado junto con su archivo de configuración. Toma un archivo de configuración y un archivo de checkpoint como entradas y devuelve los componentes del modelo cargado, incluidos el modelo principal, el modelo CLIP y el modelo VAE para su uso en el flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `config_name` | El archivo de configuración que define la arquitectura y los ajustes del modelo | STRING | Sí | Archivos de configuración disponibles |
| `ckpt_name` | El archivo de checkpoint que contiene los pesos y parámetros del modelo entrenado | STRING | Sí | Archivos de checkpoint disponibles |

**Nota:** Este nodo requiere que se seleccionen tanto un archivo de configuración como un archivo de checkpoint. El archivo de configuración debe coincidir con la arquitectura del archivo de checkpoint que se está cargando.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `MODEL` | El componente de modelo principal cargado, listo para inferencia | MODEL |
| `CLIP` | El componente de modelo CLIP cargado para codificación de texto | CLIP |
| `VAE` | El componente de modelo VAE cargado para codificación y decodificación de imágenes | VAE |

**Nota importante:** Este nodo ha sido marcado como obsoleto y puede eliminarse en versiones futuras. Considere utilizar nodos de carga alternativos para nuevos flujos de trabajo.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/es.md)

---
**Source fingerprint (SHA-256):** `820cd9f7a5ccd5a70d2b29906c8deca3632d2ccba84ca51022717e061afb72b3`
