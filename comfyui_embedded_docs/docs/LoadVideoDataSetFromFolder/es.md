# Cargar Video (desde Carpeta)

Cargar un conjunto de datos de videos desde una carpeta especificada dentro del directorio de entrada de ComfyUI. El nodo escanea la carpeta en busca de archivos de video compatibles y devuelve referencias perezosas; los fotogramas reales se decodifican solo cuando son necesarios en etapas posteriores.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `folder` | La carpeta que contiene los archivos de video. Seleccione entre las subcarpetas disponibles dentro del directorio de entrada de ComfyUI. | STRING | Sí | *(poblado desde las subcarpetas de entrada)* |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `videos` | Una lista de referencias de video perezosas (una por archivo). Los fotogramas de video se decodifican solo cuando la salida es consumida por otro nodo. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/es.md)

---
**Source fingerprint (SHA-256):** `74017c46993c38a72e529cef59ea1282f7b88b6a33b9028cf200cb3eb37de395`
