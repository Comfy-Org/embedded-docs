> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/es.md)

El nodo CheckpointLoader carga un checkpoint de modelo preentrenado junto con su archivo de configuración. Toma un archivo de configuración y un archivo de checkpoint como entradas y devuelve los componentes del modelo cargados, incluyendo el modelo principal, el modelo CLIP y el modelo VAE para su uso en el flujo de trabajo.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `nombre_configuración` | STRING | COMBO | - | Archivos de configuración disponibles | El archivo de configuración que define la arquitectura y configuraciones del modelo |
| `nombre_ckpt` | STRING | COMBO | - | Archivos de checkpoint disponibles | El archivo de checkpoint que contiene los pesos y parámetros entrenados del modelo |

**Nota:** Este nodo requiere que se seleccionen tanto un archivo de configuración como un archivo de checkpoint. El archivo de configuración debe coincidir con la arquitectura del archivo de checkpoint que se está cargando.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `MODEL` | MODEL | El componente del modelo principal cargado, listo para inferencia |
| `CLIP` | CLIP | El componente del modelo CLIP cargado para codificación de texto |
| `VAE` | VAE | El componente del modelo VAE cargado para codificación y decodificación de imágenes |

**Nota importante:** Este nodo ha sido marcado como obsoleto y podría eliminarse en versiones futuras. Considere utilizar nodos de carga alternativos para nuevos flujos de trabajo.